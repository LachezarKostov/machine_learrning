import pandas as pd

pd.options.display.max_columns = 6

# Data-frame
df = pd.read_csv(r"http://sololearn.com/uploads/files/titanic.csv")
# r"C:\Users\dream\Desktop\Python\machine_learning\machine_learrning\titanic.csv"

# Table
# print(df.describe())

# Panda Series
# col = df["Fare"]
# print(col)

# Small Data-frame
# small_df =df[["Age", "Sex", "Survived"]]
# print(small_df.head())

# Creating a Column
df["male"] = df["Sex"] == "male"
print(df.head())