import unittest
import pandas as pd
from alterpy.data_analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def test_attendance_summary(self):
        df = pd.DataFrame({'Name': ['A', 'B'], 'Attendance': [85, 90]})
        analyzer = Analyzer(df)
        result = analyzer.calculate_average_attendance()
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    unittest.main()