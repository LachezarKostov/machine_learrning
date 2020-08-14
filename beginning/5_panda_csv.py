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
# df["male"] = df["Sex"] == "male"
# print(df.head())

# Creating an Array
# array = df['Fare'].values
# print(array)

# DataFrame to a Numpy
# two_dim_array = df[["Pclass", "Sex", "Fare"]].values
# print(two_dim_array)

# Numpy Shape
arr = df[["Pclass", "Fare", "Age"]].values
shape = arr.shape
# print(shape)
# print(arr[0, 1])
# print(arr[1])
# print(arr[:, 1])

# Mask
mask = arr[:, 2] < 18
# kids = arr[mask]
# kids = arr[arr[:, 2] < 18]
sum_of_kids = sum(mask)  # mask.sum()
print(sum_of_kids)
