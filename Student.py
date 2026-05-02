# Author: Vassey Konneh and Leocalis Quezada
# Date: 04/10/2026
# Description: Student class definition for ASPOS.

class Student:
    """Represents one student data point for one week in the ASPOS dataset."""

    def __init__(self):
        """Initialize all student attributes with default values."""
        self.ID = 0
        self.week = 0
        self.study_hours = 0.0
        self.sleep_hours = 0.0
        self.stress_level = 0.0
        self.attendance = 0.0
        self.screen_time = 0.0
        self.caffeine_intake = 0.0
        self.learning_efficiency = 0.0
        self.fatigue_index = 0.0
        self.quiz_score = 0.0
        self.assignment_score = 0.0
        self.performance_index = 0.0

    def getID(self):
        """Return the student ID."""
        return self.ID

    def getWeek(self):
        """Return the week number."""
        return self.week

    def getStudyHours(self):
        """Return the study hours."""
        return self.study_hours

    def getSleepHours(self):
        """Return the sleep hours."""
        return self.sleep_hours

    def getStressLevel(self):
        """Return the stress level."""
        return self.stress_level

    def getAttendance(self):
        """Return the attendance rate."""
        return self.attendance

    def getScreenTime(self):
        """Return the screen time hours."""
        return self.screen_time

    def getCaffeineIntake(self):
        """Return the caffeine intake."""
        return self.caffeine_intake

    def getLearningEfficiency(self):
        """Return the learning efficiency."""
        return self.learning_efficiency

    def getFatigueIndex(self):
        """Return the fatigue index."""
        return self.fatigue_index

    def getQuizScore(self):
        """Return the quiz score."""
        return self.quiz_score

    def getAssignmentScore(self):
        """Return the assignment score."""
        return self.assignment_score

    def getPerformanceIndex(self):
        """Return the performance index."""
        return self.performance_index

    def setID(self, ID):
        """Set the student ID."""
        self.ID = int(ID)

    def setWeek(self, week):
        """Set the week number."""
        self.week = int(week)

    def setStudyHours(self, study_hours):
        """Set the study hours."""
        self.study_hours = float(study_hours)

    def setSleepHours(self, sleep_hours):
        """Set the sleep hours."""
        self.sleep_hours = float(sleep_hours)

    def setStressLevel(self, stress_level):
        """Set the stress level."""
        self.stress_level = float(stress_level)

    def setAttendance(self, attendance):
        """Set the attendance rate."""
        self.attendance = float(attendance)

    def setScreenTime(self, screen_time):
        """Set the screen time hours."""
        self.screen_time = float(screen_time)

    def setCaffeineIntake(self, caffeine_intake):
        """Set the caffeine intake."""
        self.caffeine_intake = float(caffeine_intake)

    def setLearningEfficiency(self, learning_efficiency):
        """Set the learning efficiency."""
        self.learning_efficiency = float(learning_efficiency)

    def setFatigueIndex(self, fatigue_index):
        """Set the fatigue index."""
        self.fatigue_index = float(fatigue_index)

    def setQuizScore(self, quiz_score):
        """Set the quiz score."""
        self.quiz_score = float(quiz_score)

    def setAssignmentScore(self, assignment_score):
        """Set the assignment score."""
        self.assignment_score = float(assignment_score)

    def setPerformanceIndex(self, performance_index):
        """Set the performance index."""
        self.performance_index = float(performance_index)

    def isAtRisk(self):
        """Return True if the student appears to be at risk."""
        attendance_cutoff = 0.75 if self.attendance <= 1 else 75
        return self.performance_index < 70 or self.attendance < attendance_cutoff

    def __str__(self):
        """Return a readable string for the student record."""
        return (
            f"Student ID: {self.ID}, Week: {self.week}, Study Hours: {self.study_hours:.2f}, "
            f"Sleep Hours: {self.sleep_hours:.2f}, Stress Level: {self.stress_level:.2f}, "
            f"Attendance: {self.attendance:.2f}, Screen Time: {self.screen_time:.2f}, "
            f"Caffeine Intake: {self.caffeine_intake:.2f}, "
            f"Learning Efficiency: {self.learning_efficiency:.2f}, "
            f"Fatigue Index: {self.fatigue_index:.2f}, Quiz Score: {self.quiz_score:.2f}, "
            f"Assignment Score: {self.assignment_score:.2f}, "
            f"Performance Index: {self.performance_index:.2f}"
        )
