"""
organizer.py

Contains the main logic for organizing files.
"""

# Built-in library for working with files and folders
import os

# Import helper functions
from file_utils import (
    get_folder_name,
    create_folder,
    move_file
)


def organize_files(folder_path):
    """
    Organize all files inside the given folder.
    """

    # Counter for moved files
    moved_files = 0

    # Loop through every item inside the folder
    for file_name in os.listdir(folder_path):

        # Full path of the current file
        file_path = os.path.join(folder_path, file_name)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Split filename and extension
        _, extension = os.path.splitext(file_name)

        # Find the correct folder name
        folder_name = get_folder_name(extension)

        # Create destination folder path
        destination_folder = os.path.join(folder_path, folder_name)

        # Create folder if it doesn't exist
        create_folder(destination_folder)

        # Final destination of the file
        destination_file = os.path.join(destination_folder, file_name)

        # Move the file
        move_file(file_path, destination_file)

        moved_files += 1

        print(f"Moved: {file_name} → {folder_name}")

    print("\nOrganization Complete!")
    print(f"Total Files Moved: {moved_files}")

