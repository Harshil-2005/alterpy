import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from alterpy.report_generator import ReportGenerator
import pandas as pd

def test_generate_pdf():
    df = pd.DataFrame({"Name": ["A"], "Attendance": [90]})
    rg = ReportGenerator(df)
    rg.generate_pdf("test_report.pdf")