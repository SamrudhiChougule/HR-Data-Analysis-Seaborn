# run_all.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder if not exists
os.makedirs("outputs/figures", exist_ok=True)

# Load dataset
data = pd.read_csv("data/hr_data_mnc.csv")

# Visualization 1: Employees by Department
plt.figure(figsize=(8,6))
sns.countplot(x='Department', data=data, palette='viridis')
plt.title("Employees by Department")
plt.savefig("outputs/figures/1_Department_Count.png", dpi=300, bbox_inches="tight")
plt.close()

# Repeat similar blocks for other 9 visualizations...
