ASPOS - Adaptive Study and Performance Optimization System

Authors:
Vassey Konneh and Leocalis Quezada

Project Description:
ASPOS is a Python-based academic analytics system that reads student learning trajectory data from a CSV file and helps users explore study behavior, attendance, fatigue, quiz scores, assignment scores, and overall performance index. The program uses pandas for data processing and tkinter for a graphical user interface.

Files Included:
1. ASPOS.py - main program file
2. GUI.py - graphical user interface
3. Analytics.py - data loading and analysis class
4. Student.py - student class definition
5. test_aspos.py - pytest unit tests
6. student_learning_trajectory.csv - dataset file

How to Run the Program:
1. Make sure Python 3.12 or later is installed.
2. Install pandas if needed:
   python -m pip install pandas
3. Place all project files in the same folder.
4. Run the program:
   python ASPOS.py

How to Run the Tests:
1. Install pytest if needed:
   python -m pip install pytest
2. Run the test file:
   pytest test_aspos.py

Main GUI Interactions:
- View Dataset
- Average Performance
- Average Study Hours
- Weekly Trends
- At-Risk Students
- Top Performers
- Filter By Week
- Filter By Student ID
- Summary Statistics
- Clear Output
- Exit Program
- Save Student Data

How the Requirements Are Met:
- The program is written in Python.
- The project includes multiple .py files.
- The project includes two meaningful classes: Student and Analytics.
- The program uses a tkinter GUI as the main user interface.
- The GUI contains more than five interactive elements.
- The program reads meaningful data from a CSV file.
- The project uses pandas as the advanced module for data and processing.
- The project includes at least five pytest tests.
- Instructions are included in this README file.
