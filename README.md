# 🔎 File Organizer by Extension (with Empty Folder Cleanup)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-Stable-brightgreen)]()
[![Maintained](https://img.shields.io/badge/maintained-yes-blue)]()

This tool scans a selected folder and all its subdirectories, and **organizes every file into subfolders based on their file extensions**.  
After the files are moved, it **automatically deletes all empty folders**, leaving your workspace clean and categorized.

---

## 🧠 Features

- ✅ Recursive scan of folders and subfolders
- 📦 Moves files to extension-based subfolders (e.g., `/pdf`, `/zip`)
- 🧹 Deletes all empty folders after organization
- 📝 Generates a log file of all actions taken
- 💡 Simple and interactive: no setup needed

---

## 📁 Example

Before:

```
Downloads/
├── reports/
│   └── invoice.pdf
├── archives/
│   └── backup.zip
└── photo.jpg
```

After running the script:

```
Downloads/
├── pdf/
│   └── invoice.pdf
├── zip/
│   └── backup.zip
├── jpg/
│   └── photo.jpg
```

> Folders `reports/` and `archives/` are removed if they become empty.

---

## 🚀 How to Use

### 1. Install Python (if not already installed)

Download from [https://python.org](https://python.org)

### 2. Run the script

```bash
python classificador_com_remocao.py
```

A folder selection dialog will appear. Pick the folder (e.g., Downloads) and let the magic happen!

---

## 📄 Output

- Files organized into folders like `/pdf`, `/csv`, `/zip`, etc.
- Empty folders removed
- A log file named `_log_extensoes_YYYYMMDD_HHMMSS.txt` is saved in the root of the selected folder.

---

## 🧩 Optional Enhancements

Feel free to fork and customize:

- Filter by modified date
- Add GUI with progress bar
- Auto-run daily with Task Scheduler or cron
- Add whitelist/blacklist by extension

---

## 📜 License

This project is licensed under the MIT License.
