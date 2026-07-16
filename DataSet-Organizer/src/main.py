"""
main.py

Entry point of the Dataset Organizer.
"""

# Built-in library for checking folders
import os

# Import organizer function
from organizer import organize_files


def main():
    """
    Main function of the program.
    """

    print("=" * 50)
    print("        DATASET ORGANIZER")
    print("=" * 50)

    # Automatically locate the sample_files folder
    current_file = os.path.dirname(__file__)          # src/
    project_folder = os.path.dirname(current_file)    # Dataset-Organizer/
    folder_path = os.path.join(project_folder, "sample_files")

    # Check whether the sample_files folder exists
    if not os.path.exists(folder_path):
        print("\nSample folder not found!")
        return

    print("\nOrganizing files...\n")

    # Call organizer
    organize_files(folder_path)

    print("\nDone!")


if __name__ == "__main__":
    main()