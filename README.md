# 📊 Customer Churn Analysis

This project performs exploratory data analysis (EDA) on a telecom customer churn dataset to uncover key factors driving customer attrition.

> **Churn** means a customer who has left the service.

---

## 📁 Project Overview

- Cleaned and transformed the dataset to prepare it for analysis.
- Generated meaningful visualizations to identify churn patterns.
- Derived actionable business insights.
- Created this interactive notebook to be accessible to both technical and non-technical users.

---

## 🧼 Data Cleaning & Transformation

- `TotalCharges` column had blank entries → Replaced with `0` and converted to `float`.
- No missing/null values or duplicates found.
- `customerID` is unique across all entries.
- `SeniorCitizen` column converted from `0/1` to `No/Yes` for better readability.

---

## 📈 Key Insights

### 🔹 Overall Churn Rate
- **26.5%** of customers have churned.
- **73.5%** are retained.
> More than 1 in 4 customers are leaving — signals urgent need for retention strategies.

### 🔹 Churn by Gender
| Gender | Churn Rate |
|--------|------------|
| Male   | 26.2%      |
| Female | 26.9%      |
> Gender does **not significantly** affect churn.

### 🔹 Churn by Senior Citizen Status
| Category        | Churn Rate |
|----------------|------------|
| Senior Citizen | 41.9%      |
| Non-Senior     | 24.0%      |
> Senior Citizens are nearly **2× more likely** to churn.

### 🔹 Churn by Tenure
| Tenure Range     | Churn Rate     |
|------------------|----------------|
| 0–12 months      | 45–60%         |
| 36+ months       | <10%           |
> Longer-tenure customers show strong loyalty.

### 🔹 Churn by Contract Type
| Contract Type  | Churn Rate |
|----------------|------------|
| Month-to-Month | 43.9%      |
| One-Year       | 11.5%      |
| Two-Year       | 2.8%       |
> Long-term contracts **drastically reduce** churn.

### 🔹 Churn by Services Used
- Lack of services like **Online Security**, **Backup**, and **Tech Support** results in **45%+ churn**.
- Customers using these services churn far less.

### 🔹 Churn by Payment Method
| Payment Method     | Churn Rate |
|--------------------|------------|
| Electronic Check   | 45.0%      |
| Other Methods      | 15–20%     |
> Indicates possible **friction with billing methods**.

---

## ✅ Strategic Recommendations

1. 🎯 **Target Senior Citizens** with personalized care and support.
2. 🤝 **Promote long-term contracts** through loyalty rewards or discounts.
3. 🔒 **Encourage use of Online Security** and **Tech Support** services.
4. 🧲 **Engage customers early** in their tenure via onboarding and offers.
5. 💳 **Transition users away from Electronic Checks** to auto-payment methods.
6. 📦 **Bundle services** to improve retention and increase stickiness.

---

## 📊 Visual Output

You can explore full visualizations and charts in the notebook:
- 📍 Churn by Gender, Tenure, Senior Citizen status
- 📍 Distribution by Contract, Payment Method, Services Used

---

## 🔗 Live Notebook (Open in Colab)

> Click below to open the full analysis with code + charts:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/usha-bharadwaj/customer-churn-analysis/blob/main/Untitled0.ipynb)


---

## 💡 Tech Stack

- Python (Pandas, NumPy)
- Seaborn, Matplotlib (Visualization)
- Google Colab (Interactive Notebook)

---

## 🙌 Author

Made with ❤️ by **Usha-Bharadwaj**  
Let's connect on [GitHub](https://github.com/usha-bharadwaj)

---

## 📌 License

This project is open-source and free to use.

