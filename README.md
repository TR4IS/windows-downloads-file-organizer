# 🧹 Windows File Organizer (Python)

A simple and effective Python script that automatically organizes your Windows **Downloads** folder into categorized subfolders like `zip`, `image`, `video`, `pdf`, `sound`, `os`, and `random`.

---

## 🚀 Features

- Automatically creates folders for:
  - 📁 Zip files (`.zip`, `.rar`)
  - 🖼️ Images (`.jpg`, `.png`, `.gif`, etc.)
  - 🎞️ Videos (`.mp4`, `.mkv`, `.avi`, etc.)
  - 📄 PDFs (`.pdf`)
  - 🎧 Audio files (`.mp3`, `.wav`, `.ogg`, etc.)
  - 💿 OS images (`.iso`, `.img`)
  - 🧪 Random/unknown files
- Only uses the Python standard library (no dependencies)
- Safe, simple, readable code

---

## 📂 How It Works

The script:
1. Scans your `Downloads` folder.
2. Identifies each file’s extension.
3. Moves the file to its corresponding category folder.
4. Creates folders if they don’t exist.

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/tr4is/windows-downloads-file-organizer.git
   cd windows-downloads-file-organizer
2. Run the Script
   ```bash
   python files.py

💡 Note: You must be on Windows and have Python installed.

## 🛠 Requirements

  - Windows OS

  - Python 3.x

## 🙋‍♂️ Author

  - TR4IS

  - GitHub: @tr4is

## 📝 To-Do / Ideas

    Add config file support (custom categories) - working on it !

    Schedule as a daily background task  - 

    Build a simple GUI -
