# Scholar-Forge
VITyarthi Project - Introduction to Problem Solving (CSE1021)


## A Personal Academic & Intellectual Management System

Scholar's Forge is a beginner-friendly Python-based personal management system designed to organize different aspects of learning and personal development in one place.

Learning is a lifelong process that extends beyond formal education. Whether it involves completing academic responsibilities, tracking performance, reading books, or exploring an independent field of interest, keeping track of these activities can become difficult when they are managed separately.

Scholar's Forge brings these activities together through a simple console-based application.

---

## Problem Statement

Learning does not end with formal education, yet the process of learning is often scattered across different tools, notes, and systems.

Tasks, academic performance, reading goals, and independent learning objectives may be tracked separately, making it difficult to maintain a clear view of what needs to be done, what has been accomplished, and what should be learned next.

Scholar's Forge addresses this problem by providing a unified system for organizing tasks, tracking performance, managing books, and building a personal learning curriculum.

---

## Objectives

The main objectives of Scholar's Forge are:

- To organize tasks and responsibilities in one place.
- To track academic subjects and examination performance.
- To maintain a personal book library and reading progress.
- To organize independent learning interests into a personal curriculum.
- To monitor completion and progress.
- To apply Python programming concepts to a meaningful real-world problem.
- To provide a simple and easy-to-use console-based system.

---

## Features

### 1. To-Do List

The To-Do List module allows users to:

- Add tasks
- Store task name, subject and deadline
- View all tasks
- Mark tasks as completed
- Delete tasks
- Calculate task completion progress

---

### 2. Subject Performance

The Subject Performance module allows users to:

- Add subjects
- View available subjects
- Enter examination results
- Store multiple results for a subject
- Calculate average marks
- Delete subjects

---

### 3. Book Tracker

The Book Tracker module allows users to:

- Add books
- Store title, author and genre
- View the personal book library
- Change reading status
- Categorize books as:
  - Want to Read
  - Reading
  - Completed
- Find books from the personal library by genre
- View reading statistics
- Delete books

---

### 4. Personal Curriculum

The Personal Curriculum module is designed for independent and lifelong learning.

Users can:

- Add learning topics
- Specify the field of a topic
- Record why they want to study it
- Add learning objectives
- Mark objectives as completed
- View learning progress
- Delete learning topics

This module allows users to create a learning path based on their own interests rather than being limited to a formal academic curriculum.

---

## Requirements

Before running Scholar's Forge, make sure the following are available:

- Python 3.x
- Git (optional, if cloning the repository)
- A terminal or command prompt
- A code editor or IDE such as VS Code, PyCharm, or IDLE

### Dependencies

Scholar's Forge uses Python's built-in features and does not require any external Python packages.

Therefore, no `pip install` command or `requirements.txt` file is required.

---

## Setup and Installation

Follow the steps below to set up Scholar's Forge on your system.

### Step 1: Install Python

Download and install Python 3.x on your system.

After installation, open a terminal or command prompt and verify that Python is installed:

```bash
python --version

---

## System Structure

The project is divided into separate Python modules:

```text
Scholar-Forge/
│
├── menu.py
├── tasks.py
├── subjects.py
├── books.py
├── curriculum.py
├── README.md
└── statement.md
