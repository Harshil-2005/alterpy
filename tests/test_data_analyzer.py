import pandas as pd
from alterpy.data_analyzer import Analyzer

def test_attendance_summary_and_percentage():
    df = pd.DataFrame({
        "StudentID": ["1", "1", "2", "2", "2"],
        "Status": ["Present", "Absent", "Present", "Present", "Absent"],
        "Date": ["2024-01-01"] * 5
    })
    analyzer = Analyzer(df)

    summary = analyzer.attendance_summary("Status")
    assert summary.get("Present", 0) == 3

    percent = analyzer.attendance_percentage("StudentID", "Status")
    assert "Percentage" in percent.columns
