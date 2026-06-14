# Automatic File Organizer

A Python script that automatically organizes files into categorized folders based on their file extensions. Runs continuously in the background and sorts new files every 10 seconds.

## Features
- Automatically sorts files into folders by type
- Runs continuously, checking for new files every 10 seconds
- Creates folders automatically if they don't exist
- Skips subfolders, only moves files

## Folder Structure
PyFiles/

├── Python_Files/    → .py,

├── Photos/          → .jpg, .jpeg, .png, .bmp

├── Videos/          → .mp4, .mkv, .avi, .mov, .wmv, .flv, .webm, .m4v

├── Documents/       → .pdf, .docx, .doc, .xlsx, .xls, .pptx, .ppt, .csv, .odt

├── Archives/        → .zip, .rar, .7z, .tar, .gz, .iso

├── Text/            → .txt

└── Other/           → anything else

## How to Run
1. Clone the repository
2. Run the script:
   python file.py
3. Drop any files into the PyFiles folder
4. Files will be automatically sorted every 10 seconds

## Requirements
- Python 3.x
- No external libraries needed (uses built-in os, shutil, time)

## What I Learned
- os module for file and folder management
- shutil module for moving files
- while loops for continuous execution
- Handling different file types and extensions
