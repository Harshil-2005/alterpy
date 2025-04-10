import unittest
import pandas as pd
from alterpy.data_visualizer import Visualizer

class TestVisualizer(unittest.TestCase):
    def test_plot_bar_chart(self):
        df = pd.DataFrame({'Name': ['A', 'B'], 'Attendance': [85, 90]})
        vis = Visualizer(df)
        try:
            vis.plot_bar('Name', 'Attendance')
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()