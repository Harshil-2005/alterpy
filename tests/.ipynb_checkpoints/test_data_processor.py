import unittest
import pandas as pd
from alterpy.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def test_drop_nulls(self):
        df = pd.DataFrame({'Name': ['A', None], 'Attendance': [90, None]})
        processor = DataProcessor(df)
        cleaned_df = processor.drop_nulls()
        self.assertFalse(cleaned_df.isnull().values.any())

    def test_fill_nulls(self):
        df = pd.DataFrame({'Name': ['A', None], 'Attendance': [90, None]})
        processor = DataProcessor(df)
        filled_df = processor.fill_nulls("Unknown")
        self.assertFalse(filled_df.isnull().values.any())

if __name__ == '__main__':
    unittest.main()