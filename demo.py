from alterpy.data_loader import DataLoader
from alterpy.data_processor import DataProcessor
from alterpy.data_analyzer import Analyzer
from alterpy.data_visualizer import Visualizer
from alterpy.report_generator import ReportGenerator

# Load data
loader = DataLoader('sample.csv')
data = loader.load_csv()

# Process data
processor = DataProcessor(data)
clean_data = processor.drop_nulls()

# Analyze data
analyzer = Analyzer(clean_data)
avg = analyzer.calculate_average_attendance()
print(f"Average Attendance: {avg}%")

# Visualize data
visualizer = Visualizer(clean_data)
visualizer.plot_bar('Name', 'Attendance')

# Generate report
report_gen = ReportGenerator(clean_data)
report_gen.generate_report('attendance_report.pdf')
