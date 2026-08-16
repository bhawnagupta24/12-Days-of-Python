# 🐍 Day 9 – File & Folder Management

## 📚 Topics Covered

* `pathlib` Module
* `os` Module
* `Path`
* File & Folder Listing
* File Creation
* Reading Files
* Updating Files
* Renaming Files
* Appending Content
* Deleting Files
* Exception Handling
* Functions

---

## 📂 Files

| File           | Description                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------- |
| `file_hand.py` | A menu-driven program for creating, reading, updating, renaming, appending, and deleting files |

---

## 💡 Features

### 1. Create File

* Takes a file name from the user.
* Creates a new file.
* Allows the user to write content into the file.

### 2. Read File

* Takes the file name from the user.
* Checks whether the file exists.
* Reads and displays the file content.

### 3. Update File

Provides three options:

* Rename the file
* Overwrite existing content
* Append new content

### 4. Delete File

* Checks whether the file exists.
* Removes the selected file using `os.remove()`.

## The program also lists files and folders using `Path.rglob()` and handles errors using `try-except`.

## 🎯 What I Learned

* How to work with files and folders using Python.
* How to use `pathlib.Path`.
* How to check whether a path exists.
* How to create and read files.
* How to rename and delete files.
* How to overwrite and append file content.
* How to use `os.remove()` for file deletion.
* How to organize file operations into functions.
* How to create a menu-driven file management program.

---

## 🚀 Outcome

Successfully built a **menu-driven File Management Program** that can create, read, update, rename, append, and delete files using Python.

✅ Day 9 Completed!
