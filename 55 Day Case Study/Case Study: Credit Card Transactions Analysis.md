# Case Study: Credit Card Transactions Analysis




## Beginner Credit Card Transactions Analysis  


```python
# -------------------------------------------------
# 1. IMPORT LIBRARIES
# -------------------------------------------------
# pandas   → work with tables (DataFrames)
# numpy    → fast numbers & random data
# matplotlib & seaborn → make pretty charts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Make plots look nice
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
```

---

```python
# -------------------------------------------------
# 2. CREATE A SMALL FAKE DATASET
# -------------------------------------------------
# (In real life you would load a CSV. Here we make one so you can run the code instantly.)

np.random.seed(42)                     # same random numbers every time
n = 1000                               # 1000 transactions

data = {
    "Transaction_ID": range(1, n+1),
    "Customer_ID"   : np.random.randint(100, 110, n),   # 10 different customers
    "Transaction_Date": pd.date_range("2023-01-01", periods=n, freq="6H"), # every 6 hours
    "Transaction_Type": np.random.choice(["Online", "POS", "ATM"], n),
    "Merchant"        : np.random.choice(["Amazon", "Walmart", "Starbucks", np.nan], n, p=[0.4,0.3,0.2,0.1]),
    "Category"        : np.random.choice(["Groceries","Electronics","Travel","Dining"], n),
    "Amount"          : np.round(np.random.exponential(80), 2),   # average ~80 USD
    "Payment_Mode"    : np.random.choice(["Credit Card","Debit Card"], n, p=[0.7,0.3]),
    "Transaction_Status": np.random.choice(["Approved","Declined","Pending"], n, p=[0.85,0.1,0.05]),
    "Location"        : np.random.choice(["New York","Los Angeles","Chicago"], n)
}

df = pd.DataFrame(data)                # create the table
df.to_csv("credit_card_transactions.csv", index=False)   # save for later
print("Fake dataset created! 1000 rows.")
```

---

```python
# -------------------------------------------------
# 3. LOAD & EXPLORE THE DATA
# -------------------------------------------------
df = pd.read_csv("credit_card_transactions.csv")

# 3.1 First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 3.2 Shape (rows, columns)
print(f"\nShape → {df.shape[0]} rows, {df.shape[1]} columns")

# 3.3 Column names
print("\nColumns:", list(df.columns))

# 3.4 Quick statistics
print("\nSummary (numbers):")
print(df.describe())
```

---

```python
# -------------------------------------------------
# 4. CLEAN THE DATA (Beginner level)
# -------------------------------------------------

# 4.1 Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 4.2 Fill missing Merchant with "Unknown"
df["Merchant"] = df["Merchant"].fillna("Unknown")

# 4.3 Convert date column to real datetime
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

# 4.4 Add helpful columns: year, month, day
df["Year"]  = df["Transaction_Date"].dt.year
df["Month"] = df["Transaction_Date"].dt.month
df["Day"]   = df["Transaction_Date"].dt.day

print("\nCleaned! New columns added.")
print(df[["Transaction_Date","Year","Month","Day"]].head())
```

---

```python
# -------------------------------------------------
# 5. SIMPLE FILTERING (Selection)
# -------------------------------------------------

# 5.1 January 2024 transactions
jan_2024 = df[(df["Year"] == 2024) & (df["Month"] == 1)]
print(f"\nJanuary 2024 → {len(jan_2024)} transactions")

# 5.2 Online transactions > $1000
high_online = df[(df["Amount"] > 1000) & (df["Transaction_Type"] == "Online")]
print(f"High‑value online → {len(high_online)} transactions")

# 5.3 Only Approved transactions
approved = df[df["Transaction_Status"] == "Approved"]
print(f"Approved → {len(approved)} transactions")
```

---

```python
# -------------------------------------------------
# 6. ADD NEW COLUMNS (Feature Engineering)
# -------------------------------------------------

# 6.1 Discounted Amount: 5% off if > $500
df["Discounted_Amount"] = df["Amount"]
mask = df["Amount"] > 500
df.loc[mask, "Discounted_Amount"] = df["Amount"] * 0.95

# 6.2 Amount Category: Low / Medium / High
def amount_cat(x):
    if x < 100:  return "Low"
    elif x <= 500: return "Medium"
    else:        return "High"

df["Amount_Category"] = df["Amount"].apply(amount_cat)

print("\nNew columns preview:")
print(df[["Amount","Discounted_Amount","Amount_Category"]].head())
```

---

```python
# -------------------------------------------------
# 7. BASIC GROUP‑BY (Aggregations)
# -------------------------------------------------

# 7.1 Total amount per Category
total_cat = df.groupby("Category")["Amount"].sum()
print("\nTotal amount per Category:")
print(total_cat)

# 7.2 Count of Declined per Payment Mode
declined = df[df["Transaction_Status"] == "Declined"]
declined_by_mode = declined["Payment_Mode"].value_counts()
print("\nDeclined transactions per Payment Mode:")
print(declined_by_mode)

# 7.3 Top 5 Merchants
top_merchants = df["Merchant"].value_counts().head(5)
print("\nTop 5 Merchants:")
print(top_merchants)
```

---

```python
# -------------------------------------------------
# 8. FRAUD FLAGS (Simple rules)
# -------------------------------------------------

# 8.1 Customers with >5 transactions on the same day
df["Date"] = df["Transaction_Date"].dt.date
daily = df.groupby(["Customer_ID","Date"]).size()
many_per_day = daily[daily > 5].reset_index(name="Count")
print(f"\nPotential fraud (more than 5 txns/day): {len(many_per_day)} cases")
print(many_per_day.head())

# 8.2 High‑risk: Online + > $3000
df["High_Risk"] = (df["Amount"] > 3000) & (df["Transaction_Type"] == "Online")
print(f"High‑risk transactions → {df['High_Risk'].sum()}")
```

---

```python
# -------------------------------------------------
# 9. MERGE WITH CUSTOMER INFO
# -------------------------------------------------

# Create a tiny customer table
cust = pd.DataFrame({
    "Customer_ID": range(100,110),
    "Age"        : [25,34,42,29,51,38,45,31,27,63],
    "Gender"     : ["F","M","M","F","F","M","F","M","F","M"],
    "Account_Status": ["Active","Active","Premium","Active","Inactive",
                       "Active","Premium","Active","Active","Premium"]
})
cust.to_csv("customer_info.csv", index=False)

# Merge
df_full = df.merge(cust, on="Customer_ID", how="left")
print("\nMerged! New columns: Age, Gender, Account_Status")
```

---

```python
# -------------------------------------------------
# 10. PLOTS (Matplotlib + Seaborn)
# -------------------------------------------------

# 10.1 Amount distribution
plt.figure()
sns.histplot(df["Amount"], bins=30, kde=True, color="skyblue")
plt.title("How much do people spend? (Amount distribution)")
plt.xlabel("Amount (USD)")
plt.xlim(0, 1000)
plt.show()

# 10.2 Total per Category (bar chart)
plt.figure()
total_cat.plot(kind="bar", color="salmon")
plt.title("Total Money Spent per Category")
plt.ylabel("USD")
plt.xticks(rotation=45)
plt.show()

# 10.3 High‑risk by Age (scatter)
plt.figure()
sns.scatterplot(data=df_full, x="Age", y="Amount", hue="High_Risk", palette=["lightgray","red"])
plt.title("High‑Risk Transactions by Customer Age")
plt.show()
```

---

## What You Learned (Beginner Checklist)

| Check | Skill |
|-------|-------|
| Check | Load / save CSV |
| Check | `df.head()`, `df.shape`, `df.describe()` |
| Check | Handle missing values (`fillna`) |
| Check | Convert strings → dates (`pd.to_datetime`) |
| Check | Filter rows (`df[condition]`) |
| Check | Create new columns (`df["new"] = …`) |
| Check | `groupby` + `sum`, `count` |
| Check | Simple fraud rules |
| Check | `merge` two tables |
| Check | Histograms, bar charts, scatter plots |

---

### Ready to try on **your own data**?

1. Replace the **fake data** section with:  

   ```python
   df = pd.read_csv("your_file.csv")
   ```

2. Run the rest of the notebook – it will work the same!

---

