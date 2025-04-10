import unittest
import pandas as pd
from alterpy.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        df = pd.DataFrame({'Name': ['A'], 'Attendance': [85]})
        rg = ReportGenerator(df)
        try:
            rg.generate_report("test_report.pdf")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()