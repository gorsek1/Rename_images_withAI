# 🖼️ Smart Image Renamer

**Turn cryptic filenames into meaningful descriptions using AI**

This tool uses advanced artificial intelligence to analyze your images and give them descriptive names based on what's actually in them. No more folders full of "IMG_2345.jpg" or random strings of numbers!

![Version](https://img.shields.io/badge/Version-1.0-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)

## ✨ What It Does

Drop your images in a folder, run this tool, and watch as AI:

1. Looks at each image and understands what's in it
2. Creates a meaningful, descriptive name
3. Saves a copy in a new "Renamed with AI" subfolder
4. Preserves all your original files

## 🚀 Quick Start Guide

### Windows Users

1. **Download** this package
2. **Double-click** `Rename_images_withAI.bat`
3. **Wait** while the AI analyzes your images
4. **Done!** Find your renamed images in the "Renamed with AI" folder

Want to see what would happen first? Run `Preview_AI_renaming.bat` instead.

### Everyone Else

```bash
# Install requirements
pip install -r requirements.txt

# Run the tool
python Rename_images_withAI.py
```

## 🧠 The AI Technology

This tool uses BLIP (Bootstrapping Language-Image Pre-training), a state-of-the-art AI model from Salesforce that can "see" what's in your images and describe it in natural language.

Unlike basic image classifiers that might just say "cat" or "mountain", BLIP can generate detailed descriptions like:

- "a black cat sleeping on a windowsill"
- "mountain landscape with snow and pine trees at sunset"
- "vintage red sports car parked on a beach"

## 🛠️ Advanced Usage

### Command Line Options

```bash
# Process JPG files in a specific folder
python Rename_images_withAI.py --dir /path/to/photos --pattern "*.jpg"

# Just see what would happen without making changes
python Rename_images_withAI.py --dry-run

# Process all image types in current folder
python Rename_images_withAI.py --pattern "*.jpg" "*.png" "*.jpeg"
```

### Full Options List

| Option | Description |
|--------|-------------|
| `--dir PATH` | Folder containing images (default: current folder) |
| `--pattern PATTERN` | File types to process (default: *.webp) |
| `--dry-run` | Preview without changing files |

## 📋 Features

- **Intelligent Naming**: Uses AI that understands image content
- **Safe Operation**: Always preserves original files
- **Organized Results**: Puts renamed files in their own folder
- **Unique Names**: Adds a small unique code to prevent duplicates
- **Flexible Format Support**: Works with WebP, JPEG, PNG, and other formats
- **Preview Mode**: See results before committing

## ⚠️ Important Notes

- First run takes longer as it downloads the AI model (~1GB)
- Processing high-resolution or many images may take time
- The AI works best with clear, well-lit photos
- While the AI is very good, it might occasionally misinterpret complex or unusual images

## 💡 Use Cases

- **Photographers**: Organize shoots based on content
- **Digital Artists**: Sort AI-generated images automatically
- **Web Developers**: Create meaningful filenames for content
- **Collectors**: Organize digital art collections
- **Anyone**: Turn chaotic image folders into organized collections

## 🤝 Credits

- BLIP model: Developed by Salesforce Research
- Built with Python, PyTorch, and Transformers

---

*"The best filename is one that tells you what's in the image without having to open it."* 