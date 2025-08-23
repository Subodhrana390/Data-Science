import pandas as pd
import numpy as np
import random

# df = pd.read_csv("sales_data_sample.csv",encoding="latin-1")
# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")

print(df)


names = ["Ram", "Shyam", "Geeta", "Sita", "Aman", "Ravi", "Neha", "Pooja", "Ankit", "Divya"]
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderabad"]

num_rows = 10

data = {
    "Name": random.choices(names, k=num_rows),
    "Age": np.random.randint(18, 60, size=num_rows),
    "City": random.choices(cities, k=num_rows)
}

df = pd.DataFrame(data)

print(df)

# df.to_csv("output.csv",index=False)
# df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)

