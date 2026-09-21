# File Organizer

A simple Python project that automatically organizes files into different folders based on their file extensions.

### What it does

The program checks files inside `Test_Files` and moves them into folders like:

* Images
* Documents
* Audio
* Videos
* Data
* Archives
* Others

It also handles duplicate filenames by adding `_1`, `_2`, etc. instead of overwriting an existing file.

### How It Works

1. The program checks the files inside `Test_Files`.
2. It gets the extension of each file.
3. It decides which category the file belongs to.
4. It creates the category folder if it doesn't exist.
5. It moves the file to that folder.
6. If the same filename already exists, it gives the new file a different name.

### Built With

* Python
* `os`
* `shutil`

### Files

* `organizer.py` — main file organizer
* `test_files.py` — creates sample files for testing
* `Test_Files` — folder containing files to organize

### What I Practiced

File handling, folders, extensions, functions, loops, `os`, `shutil`, and handling duplicate filenames.
