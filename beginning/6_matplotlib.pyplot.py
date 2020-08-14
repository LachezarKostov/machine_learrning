import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"http://sololearn.com/uploads/files/titanic.csv")
arr = df[["Pclass", "Fare", "Age"]].values
# plt.figure(figsize=(5, 10))
# plt.axes([0, 100, 0, 500])
plt.scatter(df["Age"], df["Fare"], c=df["Pclass"])

plt.title("Age-Fare Graph", c="g", fontsize=10)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
