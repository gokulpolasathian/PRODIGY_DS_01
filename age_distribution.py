import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Create histogram
plt.figure(figsize=(8,6))

plt.hist(df["age"].dropna(), bins=20)

plt.title("Age Distribution of Titanic Passengers", fontsize=16)
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()