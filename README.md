# 📚 Library Management System - Python Console Project

A fully-featured **Library Management System** built in Python using console-based UI and nested dictionaries. This project provides admin-level control to manage books, issue/return, search, and analyze book popularity, all with formatted output and robust validations.

---

## 🚀 Features

### 🔐 Admin Access

* Only admins with the correct password (`admin@123`) can access and manage the system.
* Prevents unauthorized access to library data.

### 💘 Add New Book

* Admin can add a new book with:

  * Book Name
  * Author Name
  * Popularity Index (defaults to `0`)

### 📚 Display All Books

* Shows a neat tabular display of all books with:

  * Code (auto-incremented)
  * Name
  * Author
  * Category
  * Status
  * Popularity Index
* Uses a custom formatting function (`center_align`) for alignment.

### 🏷️ Issue a Book

* Issues a selected book by its code.
* Automatically changes the status to **Issued**.
* Increases the **Popularity Index** of the book by 1.
* Prevents issuing already issued books.

### 🔄 Return a Book

* Returns a selected book by its code.
* Changes status from **Issued → Available**.
* Prevents returning books that are already available.

### 🏆 Most Popular Books

* Ranks books in descending order based on their **Popularity Index**.
* Displays:

  * The **most popular book** with a banner.
  * All books sorted by popularity.

### 📂 Display Issued Books

* Lists only the books with status marked as **Issued**.

### ❌ Remove a Book

* Removes a book by code from the system.
* Prevents deletion of non-existent or already deleted books.

### ✅ Input Validation

* Handles edge cases like:

  * Invalid book codes
  * Empty inputs
  * Book not found
  * Invalid options in menu
* Ensures the system doesn’t crash on wrong inputs.

---

## 🧱 Project Structure

* `record_dict` → Master dictionary holding all book data.
* Nested dictionaries for each book:
* 
* Modular functions handle:

  * Adding books
  * Displaying formatted tables
  * Issuing/returning books
  * Admin login
  * Searching/filtering
  * Popularity sorting

---

## 🛠️ Tech Stack

* **Language**: Python 3.x
* **Interface**: Console-based (CLI)
* **Data Storage**: In-memory (dictionary, no external database)

---

## 🏁 Getting Started

### ✅ Prerequisites

* Python 3 installed
* Basic understanding of dictionaries and functions

---

## 🔒 Admin Password

> Default password: **admin\@123**

You can change it by editing the variable at the top of the script.

---

## ⭐ GitHub Tags

`#python` `#library-system` `#console-app` `#student-project` `#dictionary` `#beginner-friendly`

---
## Author
Pranay Authankar
