"""
file_utils.py

Contains helper functions used by the Dataset Organizer.
"""

# Built-in library for working with files and folders
import os

# Built-in library for moving files
import shutil


# Dictionary that maps file extensions to folder names
FILE_TYPES = {

    ".csv": "CSV",
    ".xlsx": "Excel",
    ".xls": "Excel",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".pdf": "PDF",

    ".txt": "Text",

    ".json": "JSON",

    ".zip": "ZIP",

    ".py": "Python"
}


def get_folder_name(extension):
    """
    Return the folder name based on the file extension.

    If the extension is unknown,
    return 'Others'.
    """

    return FILE_TYPES.get(extension.lower(), "Others")


def create_folder(path):
    """
    Create a folder if it does not already exist.
    """

    if not os.path.exists(path):
        os.makedirs(path)


def move_file(source, destination):
    """
    Move a file from one location to another.
    """

    shutil.move(source, destination)





