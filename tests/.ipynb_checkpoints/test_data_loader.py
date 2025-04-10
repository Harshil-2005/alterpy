import os
import unittest
from alterpy.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_csv(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'sample.csv')
        file_path = os.path.abspath(file_path)
        loader = DataLoader(file_path)
        data = loader.load_csv()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()