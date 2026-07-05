import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Count males and females
gender_count = df["sex"].value_counts()

# Create figure
plt.figure(figsize=(8,6))

# Draw bar chart
bars = plt.bar(gender_count.index, gender_count.values)

# Add title and labels
plt.title("Distribution of Passengers by Gender", fontsize=16)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)

# Display values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 5,
        str(int(height)),
        ha="center",
        fontsize=12
    )

plt.show()