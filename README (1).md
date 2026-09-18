# Attendance-Grades-and-Marks
# Attendance & Marks Management System

A simple Python-based console application to manage **students, attendance, and marks** using CSV file storage. This project is ideal for beginners learning file handling, functions, and basic data processing in Python.

---

## 📌 Features

* **Add Student:** Stores roll number, name, and class.
* **List Students:** Displays all registered students.
* **Mark Attendance:** Allows marking Present/Absent for each student.
* **Attendance Percentage:** Calculates attendance percentage for a selected student.
* **Add Marks:** Add marks for multiple subjects.
* **View Marks & Grade:** Displays marks, total, average, and final grade.
* **CSV Storage:** All data is stored in CSV files (students.csv, attendance.csv, marks.csv).

---

## 📁 Files Used

The project automatically creates the following files if they do not exist:

| File Name          | Purpose                                 |
| ------------------ | --------------------------------------- |
| **students.csv**   | Stores roll, name, and class            |
| **attendance.csv** | Stores attendance date and status (P/A) |
| **marks.csv**      | Stores subject-wise marks               |

---

## 🛠️ How It Works

1. **Run the program.**
2. A menu will appear with 7 options.
3. Choose the task you want to perform (Add student, mark attendance, etc.).
4. Data will be saved in CSV files for future use.

---

## 📖 Menu Options

```
1. Add Student
2. List Students
3. Mark Attendance
4. View Attendance Percentage
5. Add Marks
6. View Marks & Grade
7. Exit
```

---

## ⭐ Grade Criteria

| Average Marks | Grade |
| ------------- | ----- |
| 90+           | S     |
| 80–89         | A     |
| 70–79         | B     |
| 60–69         | C     |
| 50–59         | D     |
| Below 50      | F     |

---

## ▶️ How to Run

1. Make sure **Python 3** is installed.
2. Save the script as `main.py`.
3. Open a terminal and run:

```bash
python main.py
```

---

## 📌 Requirements

* Python 3.x
* No external libraries required (uses built-in `csv` and `os` modules).

---

## 📚 Project Description

This project is made to help students learn:

* Python **file handling**
* **CSV read/write operations**
* **Conditional statements** and **loops**
* **Functions and modular programming**
* Basic **grade and percentage calculation**

---

## ✔️ Output Example

**Marking Attendance Example:**

```
1 - Raju (P/A): P
2 - Kiran (P/A): A
Attendance Saved!
```

**Grade Calculation Example:**

```
Total: 245
Average: 81.66
Grade: A
```

---

## 🙌 Author

This project was created as part of a Python learning assignment.

You can modify or extend this project easily to add more features like:

* Attendance reports
* Highest scoring student
* GUI interface
* Database storage

---

## 🏁 End

Thank you for using the Attendance & Marks System! 🎓
