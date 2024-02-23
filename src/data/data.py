import os

import pandas as pd
import numpy as np

np.random.seed(123)

data = {
    "Column1": np.random.randint(0, 10, size=100000),
    "Column2": np.random.choice(["A", "B", "C"], size=100000),
    "Column3": np.random.rand(100000),
}

# Create a dataframe
df = pd.DataFrame(data)


rows, columns = df.shape
print(f"Rows: %d, Columns: %d" % (rows, columns))

export_dir = os.path.dirname(os.path.abspath(__file__))

# CSV
df.to_csv(f"{export_dir}/dataframe.csv")

# Pickle
df.to_pickle(f"{export_dir}/dataframe.pkl")
