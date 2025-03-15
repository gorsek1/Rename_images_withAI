#!/usr/bin/env python3
# Demo script to run the image processor in dry-run mode

import subprocess
import sys
import os

def main():
    print("AI Image Recognition and Naming Demo")
    print("====================================")
    print("This demo shows how the script would analyze your images and save them")
    print("with AI-generated descriptive names to a 'Renamed with AI' subfolder.")
    print("This is a preview only - no files will be created or modified.")
    print()
    print("Press Enter to continue or Ctrl+C to cancel...")
    try:
        input()
    except KeyboardInterrupt:
        print("\nDemo cancelled.")
        return

    # Check if the required Python packages are installed
    try:
        print("Checking dependencies...")
        import transformers
        import torch
        import PIL
        print("All dependencies are installed.")
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    # Run the processor in dry-run mode
    print("\nRunning the image analyzer in demonstration mode...\n")
    script_path = os.path.join(os.path.dirname(__file__), "Rename_images_withAI.py")
    subprocess.call([sys.executable, script_path, "--dry-run"])
    
    print("\nDemo completed. To actually process your files, run:")
    print("python Rename_images_withAI.py")
    print()
    print("This will create a 'Renamed with AI' subfolder with copies of your images")
    print("renamed according to their content. Your original files will be preserved.")
    print()
    print("You can also specify different options. See README.md for details.")

if __name__ == "__main__":
    main() 