# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Load the dataset
df = pd.read_csv("Project/Customer Churn.csv")

# ---------------------- Data Cleaning ----------------------

# Replace blank strings in 'TotalCharges' with "0" and convert to float
# Reason: Customers with 0 tenure shouldn't have any charges
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0").astype(float)

# Confirming no null values
# print(df.isnull().sum().sum())  # Should return 0

# Check for duplicate rows
# print(df.duplicated().sum())  # Should return 0
# print(df["customerID"].duplicated().sum())  # Ensures customerID is unique

# Convert 'SeniorCitizen' column from 0/1 to "No"/"Yes" for better readability
df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})

# ---------------------- Exploratory Data Analysis (EDA) ----------------------

# 1. Churn Count
'''
plt.figure(figsize=(4, 5))
ax = sns.countplot(x='Churn', data=df)
ax.bar_label(ax.containers[0])
plt.title("Customer Churn Count")
plt.show()
'''

# 2. Churn Percentage (Pie Chart)
'''
churn_counts = df["Churn"].value_counts()
plt.figure(figsize=(4, 4))
plt.pie(churn_counts, labels=churn_counts.index, autopct="%1.2f%%", startangle=90)
plt.title("Customer Churn Percentage")
plt.show()
'''

# 3. Churn by Gender
'''
plt.figure(figsize=(4, 4))
sns.countplot(x="gender", data=df, hue="Churn")
plt.title("Churn Distribution by Gender")
plt.show()
'''

# 4. Senior Citizen Count
'''
plt.figure(figsize=(4, 4))
ax = sns.countplot(x="SeniorCitizen", data=df)
ax.bar_label(ax.containers[0])
plt.title("Senior Citizen Count")
plt.show()
'''

# 5. Churn by Senior Citizen (Stacked Bar)
'''
churn_by_senior = df.groupby("SeniorCitizen")["Churn"].value_counts(normalize=True).unstack() * 100
fig, ax = plt.subplots(figsize=(6, 5))
churn_by_senior.plot(kind="bar", stacked=True, ax=ax)

# Adding percentage labels
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_y() + p.get_height() / 2,
            f'{p.get_height():.1f}%', ha='center', va='center')

plt.title("Churn Percentage by Senior Citizen")
plt.ylabel("Percentage (%)")
plt.legend(title="Churn", bbox_to_anchor=(1.05, 1))
plt.show()
'''

# 6. Tenure vs Churn
'''
plt.figure(figsize=(9, 4))
sns.histplot(data=df, x="tenure", hue="Churn", bins=72)
plt.title("Churn Distribution by Tenure")
plt.xlabel("Tenure (Months)")
plt.show()
'''

# 7. Churn by Contract Type
'''
plt.figure(figsize=(5, 4))
ax = sns.countplot(x="Contract", data=df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.show()
'''

# 8. Churn by Services
'''
service_cols = [
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
]

n_cols = 3
n_rows = -(-len(service_cols) // n_cols)  # Ceiling division to calculate rows

fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 4))
axes = axes.flatten()

for i, col in enumerate(service_cols):
    sns.countplot(x=col, data=df, hue="Churn", ax=axes[i])
    axes[i].set_title(f'Churn by {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Count")

# Remove unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
'''

# 9. Churn by Payment Method
'''
plt.figure(figsize=(6, 4))
ax = sns.countplot(x="PaymentMethod", data=df, hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churn by Payment Method")
plt.xticks(rotation=45)
plt.show()
'''

# ---------------------- Insights ----------------------
# - Around 26.5% of customers have churned.
# - Month-to-month contract customers are more likely to churn.
# - Senior citizens have a higher churn rate.
# - Electronic check payment method correlates with higher churn.
# - Customers with longer tenure churn less.
# - Lack of internet-related services (like TechSupport, OnlineSecurity) increases churn likelihood.
