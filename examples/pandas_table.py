from rich import print
from rich.table import Table
import pandas as pd

data = {
    "Name": ["John", "Jane", "Boby"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
    "Occupation": ["Engineer", "Student", "Artist"],
}

df = pd.DataFrame(data)
table = Table.from_pandas(df)
print(table)
