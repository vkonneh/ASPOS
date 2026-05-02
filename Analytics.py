# Author: Vassey Konneh and Leocalis Quezada
# Date: 04/10/2026
# Description: Analytics class for ASPOS that loads, processes, and summarizes data.

import pandas as pd
from Student import Student

import pandas as pd
from Student import Student


class Analytics:
    """Loads and analyzes the student learning trajectory dataset."""

    REQUIRED_COLUMNS = [
        "student_id",
        "week",
        "study_hours",
        "sleep_hours",
        "stress_level",
        "attendance_rate",
        "screen_time_hours",
        "caffeine_intake",
        "learning_efficiency",
        "fatigue_index",
        "quiz_score",
        "assignment_score",
        "performance_index"
    ]

    def __init__(self, file_name):
        """Initialize the Analytics object and load the CSV file."""
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

        self._validate_columns()
        self._clean_data()
        self.student_objects = self.createStudentObjects()

    def _validate_columns(self):
        """Check that the CSV file contains all required columns."""
        missing_columns = [
            column for column in self.REQUIRED_COLUMNS
            if column not in self.df.columns
        ]

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

    def _clean_data(self):
        """Convert important columns to numeric values and remove invalid rows."""
        numeric_columns = [
            "student_id",
            "week",
            "study_hours",
            "sleep_hours",
            "stress_level",
            "attendance_rate",
            "screen_time_hours",
            "caffeine_intake",
            "learning_efficiency",
            "fatigue_index",
            "quiz_score",
            "assignment_score",
            "performance_index"
        ]

        for column in numeric_columns:
            self.df[column] = pd.to_numeric(self.df[column], errors="coerce")

        self.df = self.df.dropna(subset=self.REQUIRED_COLUMNS)

        self.df["student_id"] = self.df["student_id"].astype(int)
        self.df["week"] = self.df["week"].astype(int)

    def createStudentObjects(self):
        """Convert each dataset row into a Student object."""
        student_objects = []

        for _, row in self.df.iterrows():
            student = Student()
            student.setID(int(row["student_id"]))
            student.setWeek(int(row["week"]))
            student.setStudyHours(float(row["study_hours"]))
            student.setSleepHours(float(row["sleep_hours"]))
            student.setStressLevel(float(row["stress_level"]))
            student.setAttendance(float(row["attendance_rate"]))
            student.setScreenTime(float(row["screen_time_hours"]))
            student.setCaffeineIntake(float(row["caffeine_intake"]))
            student.setLearningEfficiency(float(row["learning_efficiency"]))
            student.setFatigueIndex(float(row["fatigue_index"]))
            student.setQuizScore(float(row["quiz_score"]))
            student.setAssignmentScore(float(row["assignment_score"]))
            student.setPerformanceIndex(float(row["performance_index"]))
            student_objects.append(student)

        return student_objects

    def getDataset(self):
        """Return the full DataFrame."""
        return self.df

    def getAveragePerformance(self):
        """Return the average performance index across the dataset."""
        return float(self.df["performance_index"].mean())

    def getAverageStudyHours(self):
        """Return the average study hours across the dataset."""
        return float(self.df["study_hours"].mean())

    def getWeeklyTrends(self):
        """Return weekly average performance and quiz score."""
        return self.df.groupby("week")[["performance_index", "quiz_score"]].mean()

    def getAtRiskStudents(self):
        """Return rows that represent students who may be at risk."""
        max_attendance = self.df["attendance_rate"].max()

        if max_attendance <= 1:
            attendance_cutoff = 0.75
        else:
            attendance_cutoff = 75

        return self.df[
            (self.df["performance_index"] < 70) |
            (self.df["attendance_rate"] < attendance_cutoff)
            ]

    def getTopPerformers(self, count=10):
        """Return the top rows based on performance index."""
        return self.df.sort_values(by="performance_index", ascending=False).head(count)

    def filterByWeek(self, week):
        """Return all rows for a specific week."""
        return self.df[self.df["week"] == int(week)]

    def filterByStudentID(self, student_id):
        """Return all rows for a specific student ID."""
        return self.df[self.df["student_id"] == int(student_id)]

    def getSummaryStatistics(self):
        """Return descriptive statistics for the most important columns."""
        columns = [
            "study_hours",
            "sleep_hours",
            "attendance_rate",
            "quiz_score",
            "assignment_score",
            "performance_index"
        ]
        return self.df[columns].describe()

