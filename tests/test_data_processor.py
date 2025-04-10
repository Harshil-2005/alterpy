import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from alterpy.data_processor import DataProcessor
import pandas as pd

def test_drop_and_fill_nulls():
    df = pd.DataFrame({"A": [1, None], "B": [None, 2]})
    dp = DataProcessor(df)
    processed = dp.drop_nulls().fill_nulls(0).get_data()
    assert processed is not None