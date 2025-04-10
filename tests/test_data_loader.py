import pandas as pd
from alterpy.data_loader import DataLoader

def test_loader_csv(tmp_path):
    test_csv = tmp_path / "test.csv"
    df = pd.DataFrame({"Name": ["A", "B"], "Status": ["Present", "Absent"]})
    df.to_csv(test_csv, index=False)

    loader = DataLoader(str(test_csv))
    loaded = loader.load_csv()
    assert loaded is not None
    assert loaded.shape == (2, 2)
