#!/usr/bin/env python3
# Rename_images_withAI.py - Renames images based on AI image recognition

import os
import glob
import uuid
import argparse
import shutil
from pathlib import Path
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import re

def clean_name(text, max_length=40):
    """Clean text to be usable as a filename and limit the length."""
    # Remove invalid filename characters and replace spaces with underscores
    cleaned = re.sub(r'[\\/*?:"<>|]', '', text)
    cleaned = cleaned.replace(' ', '_').lower()
    
    # Limit the length while preserving words
    if len(cleaned) > max_length:
        words = cleaned.split('_')
        result = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= max_length:  # +1 for the underscore
                result.append(word)
                current_length += len(word) + 1
            else:
                break
                
        cleaned = '_'.join(result)
        
    return cleaned

def generate_caption(image_path, model, processor):
    """Use AI model to generate a caption for the image."""
    try:
        raw_image = Image.open(image_path).convert('RGB')
        
        # Prepare inputs
        inputs = processor(raw_image, return_tensors="pt")
        
        # Generate caption
        with torch.no_grad():
            generated_ids = model.generate(**inputs, max_length=30)
            caption = processor.decode(generated_ids[0], skip_special_tokens=True)
            
        return caption
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return "unrecognized_image"

def generate_name(caption):
    """Generate a good short name based on the image caption."""
    if not caption or caption == "unrecognized_image":
        return "unnamed"
    
    # Remove common phrases that don't add value to filenames
    caption = caption.lower()
    caption = re.sub(r'^a photo of ', '', caption)
    caption = re.sub(r'^an image of ', '', caption)
    caption = re.sub(r'^photo of ', '', caption)
    caption = re.sub(r'^picture of ', '', caption)
    caption = re.sub(r'^this is ', '', caption)
    caption = re.sub(r'^there is ', '', caption)
        
    return clean_name(caption)

def process_images(directory, model, processor, pattern="*.webp", dry_run=False):
    """Process all images in the directory based on AI recognition and save to a new subfolder."""
    image_paths = glob.glob(os.path.join(directory, pattern))
    processed_count = 0
    
    # Create the output directory if it doesn't exist
    output_dir = os.path.join(directory, "Renamed with AI")
    if not dry_run:
        os.makedirs(output_dir, exist_ok=True)
        print(f"Created output directory: {output_dir}")
    else:
        print(f"Would create output directory: {output_dir}")
    
    for image_path in image_paths:
        print(f"Processing: {os.path.basename(image_path)}")
        caption = generate_caption(image_path, model, processor)
        
        if caption:
            new_name = generate_name(caption)
            
            # Add a random suffix to ensure uniqueness
            unique_suffix = str(uuid.uuid4())[:6]
            file_ext = os.path.splitext(image_path)[1]
            new_filename = f"{new_name}_{unique_suffix}{file_ext}"
            new_path = os.path.join(output_dir, new_filename)
            
            print(f"  → AI caption: \"{caption}\"")
            print(f"  → New name: {new_filename}")
            
            if not dry_run:
                try:
                    shutil.copy2(image_path, new_path)
                    processed_count += 1
                    print(f"  → Copied to: {os.path.relpath(new_path, directory)}")
                except Exception as e:
                    print(f"  Error copying file: {e}")
            else:
                processed_count += 1
                print(f"  → Would copy to: {os.path.relpath(new_path, directory)}")
    
    return processed_count

def main():
    parser = argparse.ArgumentParser(description="Rename images based on AI recognition and save to 'Renamed with AI' subfolder")
    parser.add_argument("--dir", default=".", help="Directory containing images (default: current directory)")
    parser.add_argument("--pattern", default="*.webp", help="File pattern to match (default: *.webp)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without processing files")
    args = parser.parse_args()
    
    print("Loading advanced AI image captioning model (this might take a moment)...")
    # Load BLIP model - a powerful image captioning model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    print(f"\nLooking for images matching '{args.pattern}' in '{args.dir}'")
    processed = process_images(args.dir, model, processor, args.pattern, args.dry_run)
    
    mode = "Would process" if args.dry_run else "Processed"
    print(f"\n{mode} {processed} images.")
    if not args.dry_run and processed > 0:
        print(f"All processed images were saved to the 'Renamed with AI' subfolder.")
    if args.dry_run:
        print("Run without --dry-run to actually process the files.")

if __name__ == "__main__":
    main()
