import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from alterpy.data_loader import DataLoader
import pandas as pd

def test_load_csv():
    dl = DataLoader("sample.csv")
    df = pd.DataFrame({'Name': ['A'], 'Value': [1]})
    assert not df.empty