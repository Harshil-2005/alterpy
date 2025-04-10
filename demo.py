from alterpy.data_loader import DataLoader
from alterpy.data_processor import DataProcessor
from alterpy.data_analyzer import Analyzer
from alterpy.data_visualizer import Visualizer
from alterpy.report_generator import ReportGenerator

def main():
    loader = DataLoader('sample.csv')
    data = loader.load_csv()

    processor = DataProcessor(data)
    cleaned_data = processor.remove_duplicates()

    analyzer = Analyzer(cleaned_data)
    attendance_summary = analyzer.calculate_attendance_summary()

    visualizer = Visualizer(cleaned_data)
    visualizer.plot_attendance_trend()

    report = ReportGenerator(cleaned_data)
    report.generate_summary_report('summary.txt')

    print("Demo completed.")

if __name__ == "__main__":
    main()
