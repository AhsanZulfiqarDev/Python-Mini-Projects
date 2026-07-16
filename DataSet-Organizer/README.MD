# 📂 Dataset Organizer

This project was built to practice Python fundamentals such as file handling, modules, functions, loops, conditional statements, and working with directories using the `os` and `shutil` libraries.

---

## 🚀 Features

- Automatically organizes files by extension.
- Creates folders if they do not already exist.
- Supports multiple file types.
- Places unknown file types into an **Others** folder.
- Displays every moved file.
- Shows the total number of files organized.

---

## 📁 Project Structure

```
Dataset-Organizer/
│
├── sample_files/
│   ├── CSV/
│   ├── Excel/
│   ├── Images/
│   ├── JSON/
│   ├── PDF/
│   ├── Python/
│   ├── Text/
│   ├── ZIP/
│   └── Others/
│
├── src/
│   ├── file_utils.py
│   ├── organizer.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📌 Supported File Types

| File Extension | Destination Folder |
|----------------|--------------------|
| .csv | CSV |
| .xlsx | Excel |
| .xls | Excel |
| .jpg | Images |
| .jpeg | Images |
| .png | Images |
| .pdf | PDF |
| .txt | Text |
| .json | JSON |
| .zip | ZIP |
| .py | Python |
| Any other extension | Others |

---

## 🛠 Technologies Used

- Python 3
- os
- shutil

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Python-mini-projects.git
```

### Navigate to the project

```bash
cd Python-mini-projects/Dataset-Organizer
```

### Run the project

```bash
python src/main.py
```

The program automatically organizes all files inside the `sample_files` folder.

---

## 📸 Example Output

```
==================================================
        DATASET ORGANIZER
==================================================

Organizing files...

Moved: sales.csv -> CSV
Moved: report.pdf -> PDF
Moved: image.jpg -> Images
Moved: notes.txt -> Text
Moved: script.py -> Python

Organization Complete!
Total Files Moved: 5

Done!
```

---

## 👨‍💻 Author

**Ahsan Zulfiqar**

Computer Science Graduate | Aspiring Data Scientist & Machine Learning Engineer

GitHub: https://github.com/AhsanZulfiqarDev

---

