# Author: Vassey Konneh and Leocalis Quezada
# Date: 04/10/2026
# Description: Pytest tests for ASPOS, including LoginSystem and Student changes.

import os
import json
import pandas as pd
import pytest
from Student import Student
from Analytics import Analytics
from LoginSystem import LoginSystem


@pytest.fixture
def sample_csv(tmp_path):
    """Create a temporary CSV file for testing."""
    file_path = tmp_path / 'sample_students.csv'

    dataframe = pd.DataFrame({
        'student_id': [1, 1, 2],
        'week': [1, 2, 1],
        'study_hours': [8.0, 10.0, 6.0],
        'sleep_hours': [7.0, 7.5, 6.5],
        'stress_level': [4.0, 3.0, 8.0],
        'attendance_rate': [90.0, 85.0, 70.0],
        'screen_time_hours': [4.0, 3.5, 6.0],
        'caffeine_intake': [2.0, 1.0, 4.0],
        'learning_efficiency': [85.0, 88.0, 60.0],
        'fatigue_index': [20.0, 18.0, 45.0],
        'quiz_score': [82.0, 87.0, 60.0],
        'assignment_score': [85.0, 90.0, 62.0],
        'performance_index': [84.0, 89.0, 65.0]
    })

    dataframe.to_csv(file_path, index=False)
    return str(file_path)


def testStudentIsAtRisk():
    """Check the Student risk logic."""
    student = Student()
    student.setAttendance(70)
    student.setPerformanceIndex(65)
    assert student.isAtRisk() is True


def testLoadAnalyticsData(sample_csv):
    """Check that the analytics class loads the CSV correctly."""
    analytics = Analytics(sample_csv)
    assert len(analytics.getDataset()) == 3


def testAveragePerformance(sample_csv):
    """Check average performance calculation."""
    analytics = Analytics(sample_csv)
    assert analytics.getAveragePerformance() == pytest.approx(79.3333333333)


def testFilterByWeek(sample_csv):
    """Check filtering by week."""
    analytics = Analytics(sample_csv)
    filtered = analytics.filterByWeek(1)
    assert len(filtered) == 2


def testFilterByStudentID(sample_csv):
    """Check filtering by student ID."""
    analytics = Analytics(sample_csv)
    filtered = analytics.filterByStudentID(1)
    assert len(filtered) == 2


def testAtRiskStudentsFunction(sample_csv):
    """Check at-risk student filtering."""
    analytics = Analytics(sample_csv)
    filtered = analytics.getAtRiskStudents()
    assert len(filtered) == 1


def testStudentToDict():
    """Check that the Student toDict method returns a valid dictionary."""
    student = Student()
    student.setID(1)
    student.setWeek(2)
    student.setStudyHours(8.5)

    student_dict = student.toDict()
    assert student_dict["ID"] == 1
    assert student_dict["week"] == 2
    assert student_dict["study_hours"] == 8.5


def testSaveStudentData(tmp_path):
    """Check that student data is saved properly using LoginSystem."""
    test_file = tmp_path / "test_student_data.mec"
    login_sys = LoginSystem()

    sample_data = {"ID": 1, "week": 1, "study_hours": 8.0}
    success, message = login_sys.saveStudentData(1, sample_data, filename=str(test_file))

    assert success is True
    assert os.path.exists(test_file)

    # Check that data was properly saved to the dictionary/JSON file
    with open(test_file, "r") as f:
        saved_data = json.load(f)
        assert "1" in saved_data
        assert len(saved_data["1"]) == 1
        assert saved_data["1"][0]["study_hours"] == 8.0
