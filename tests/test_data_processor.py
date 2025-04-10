import pandas as pd
from alterpy.data_processor import DataProcessor  # adjust this import based on your structure

def test_data_processing():
    df = pd.DataFrame({
        "StudentID": [1, 1, 2],
        "Name": ["A", "A", "B"],
        "Date": ["2024-01-01", "2024-01-02", "2024-01-01"],
        "Status": ["Present", "Absent", "Present"]
    })

    processor = DataProcessor(df)
    processed = processor.drop_duplicates().fill_nulls().sort_by_date().get_data()

    # Test if rows are sorted by date
    assert list(processed["Date"]) == sorted(processed["Date"])

    # Test attendance summary structure
    summary = processor.attendance_summary()
    assert "Present" in summary.columns or "Absent" in summary.columns

    # Test attendance percentage
    percentage = processor.attendance_percentage()
    assert "Percentage" in percentage.columns

    # Check filtering
    present_df = processor.filter_by_status("Present")
    assert all(present_df["Status"] == "Present")
