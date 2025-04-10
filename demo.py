import pandas as pd
from alterpy.data_loader import DataLoader
from alterpy.data_processor import DataProcessor
from alterpy.data_analyzer import Analyzer
from alterpy.visualizer import Visualizer
from alterpy.report_generator import ReportGenerator

def main():
    # Load the data
    loader = DataLoader("sample_attendance.csv")
    df = loader.load_csv()
    print("\n--- Preview Loaded Data ---")
    print(loader.preview_data(df))

    # Process the data
    processor = DataProcessor(df)
    processor.drop_duplicates().fill_nulls().sort_by_date()
    processed_df = processor.get_data()
    print("\n--- Processed Data ---")
    print(processed_df)

    # Analyze the data
    analyzer = Analyzer(processed_df)
    summary_series = analyzer.attendance_summary("Status")
    print("\n--- Attendance Summary ---")
    print(summary_series)

    percentage_df = analyzer.attendance_percentage("StudentID", "Status")
    print("\n--- Attendance Percentage ---")
    print(percentage_df)

    # Prepare summary for visualization
    summary = summary_series.reset_index()
    summary.columns = ['Status', 'count']

    # Visualize the data
    visualizer = Visualizer(summary)
    visualizer.pie_chart("Status", "count", save_path="outputs/status_pie_chart.png", show=True)
    visualizer.bar_chart("Status", "count", title="Attendance Count by Status", save_path="outputs/status_bar_chart.png", show=True)

    # Generate PDF Report
    report = ReportGenerator(percentage_df)
    report.generate_pdf("outputs/attendance_report.pdf")

if __name__ == "__main__":
    main()
