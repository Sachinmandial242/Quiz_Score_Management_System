# Quiz & Score Management System Using Python

## 📌 Project Overview

The **Quiz & Score Management System** is a Python-based mini project developed to conduct multiple-choice quizzes and manage quiz scores.

The system allows users to select a quiz category, answer multiple-choice questions, receive their result automatically, save their scores, view previous scores, and check the leaderboard.

The project uses **Python, Object-Oriented Programming (OOP), Randomization, and File Handling**.

---

## 🎯 Objectives

* To conduct quizzes using multiple-choice questions.
* To provide different quiz categories.
* To randomly arrange quiz questions.
* To automatically check answers.
* To calculate score and percentage.
* To assign grades based on performance.
* To display Pass/Fail status.
* To save quiz results in a file.
* To view previous quiz scores.
* To display a leaderboard based on scores.

---

## ✨ Features

* User name input
* Category selection
* Python quiz
* Data Science quiz
* DBMS quiz
* Random question order
* Multiple-choice questions
* Answer validation
* Automatic score calculation
* Percentage calculation
* Grade calculation
* Pass/Fail result
* Result saving using file handling
* Previous score history
* Leaderboard
* OOP implementation
* Simple menu-driven interface

---

## 📚 Quiz Categories

The system currently provides three categories:

1. **Python**
2. **Data Science**
3. **DBMS**

Each category contains multiple-choice questions with four options: A, B, C, and D.

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Concepts Used:**

  * Functions
  * Lists
  * Dictionaries
  * Conditional Statements
  * Loops
  * Classes and Objects
  * Object-Oriented Programming
  * Random Module
  * File Handling
  * Exception Handling

---

## 📁 Project Structure

```text
Quiz_Management_System
│
├── main.py
├── questions.py
├── quiz.py
├── results.py
├── scores.py
├── scores.txt
└── README.md
```

### File Description

| File           | Description                                              |
| -------------- | -------------------------------------------------------- |
| `main.py`      | Controls the main menu and connects all modules          |
| `questions.py` | Contains quiz questions, options, answers and categories |
| `quiz.py`      | Contains quiz logic and OOP implementation               |
| `results.py`   | Calculates percentage, grade and Pass/Fail result        |
| `scores.py`    | Displays previous scores and leaderboard                 |
| `scores.txt`   | Stores quiz results                                      |
| `README.md`    | Contains project documentation                           |

---

## ⚙️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

Check Python version using:

```bash
python --version
```

### Step 2: Open Project Folder

Open the `Quiz_Management_System` folder in VS Code.

### Step 3: Open Terminal

Open the terminal in VS Code.

### Step 4: Run the Project

Execute:

```bash
python main.py
```

---

## 🖥️ Main Menu

After running the program, the following menu is displayed:

```text
==========================================
     QUIZ & SCORE MANAGEMENT SYSTEM
==========================================
1. Start Quiz
2. View Previous Scores
3. View Leaderboard
4. Exit
```

---

## 📝 Quiz Process

1. Enter the user's name.
2. Select a quiz category.
3. Questions are displayed in random order.
4. Select an answer from A, B, C, or D.
5. The system checks the answer automatically.
6. The score is calculated.
7. Percentage and grade are calculated.
8. Pass/Fail status is displayed.
9. The result is saved in `scores.txt`.

---

## 🏆 Grading System

| Percentage   | Grade | Result |
| ------------ | ----- | ------ |
| 80% or above | A     | PASS   |
| 60% - 79%    | B     | PASS   |
| 40% - 59%    | C     | PASS   |
| Below 40%    | D     | FAIL   |

---

## 💾 File Handling

The project uses file handling to store quiz results.

The results are saved in:

```text
scores.txt
```

Example:

```text
Sachin | Python | 5/6 | 83.33% | Grade A | PASS
```

This allows the system to maintain previous quiz records even after the program is closed.

---

## 🏅 Leaderboard

The leaderboard reads the saved scores from `scores.txt` and displays users according to their correct answers.

Example:

```text
================================
           LEADERBOARD
================================

1 . Sachin - Python - 5 points
2 . Rahul - DBMS - 4 points
================================
```

---

## 🔐 Input Validation

The system validates quiz answers.

Only the following inputs are accepted:

```text
A
B
C
D
```

If an invalid option is entered, the system asks the user to enter a valid option.

---

## 🧩 Object-Oriented Programming

The project uses a `Quiz` class to manage quiz-related information and operations.

The class stores:

* Questions
* User name
* Quiz category
* Score

This makes the project more organized and demonstrates the use of **classes and objects in Python**.

---

## 🌟 Advantages

* Easy to use
* Simple menu-driven interface
* Automatic result calculation
* Randomized questions
* Multiple quiz categories
* Stores previous results
* Leaderboard functionality
* Demonstrates important Python concepts
* Useful for basic quiz management

---

## ⚠️ Limitations

* Questions are stored directly in a Python file.
* The project currently uses a text file instead of a database.
* It is a console-based application.
* There is no separate admin panel.
* The number of questions is currently fixed for each category.

---

## 🚀 Future Scope

The project can be improved in the future by adding:

* Graphical User Interface (GUI)
* Database connectivity
* Admin panel
* Login and registration
* More quiz categories
* More questions
* Timer for each question
* Difficulty levels
* Detailed performance reports
* Web-based interface

---

## 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

* Python programming
* Functions
* Lists and dictionaries
* Loops and conditions
* Classes and objects
* Object-Oriented Programming
* Randomization
* File handling
* Exception handling
* Modular programming
* Basic project development

---

## 👨‍💻 Project Information

**Project Name:** Quiz & Score Management System Using Python

**Project Type:** Mini Project

**Technology:** Python

**Platform:** VS Code / Python

**Developer:** Sachin Mandial

---

## 📌 Conclusion

The **Quiz & Score Management System** provides a simple and effective way to conduct multiple-choice quizzes and manage quiz results. It demonstrates the practical use of Python programming concepts such as OOP, file handling, randomization, functions, conditional statements, loops, and exception handling.

The project can further be extended into a database-based or web-based quiz management application.
