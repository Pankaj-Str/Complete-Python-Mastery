# Credit Card Transactions Analysis
## Questions

#### https://github.com/Pankaj-Str/Complete-Python-Mastery/issues/14
 
It assumes the two CSV files (`credit_card_transactions.csv` and `customer_info.csv`) are in the same directory. The code includes reasonable handling for missing values, date parsing, and the fraud indicators.

```python
import pandas as pd
from datetime import timedelta

# ========================== 1️⃣ Data Exploration and Cleaning ==========================
df = pd.read_csv('credit_card_transactions.csv')

print("First 5 rows:")
print(df.head())

print("\nShape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nSummary statistics:")
print(df.describe())

# Identify missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Handle missing values based on data type
numeric_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')

# Convert Transaction_Date to datetime and extract components
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
df['Year'] = df['Transaction_Date'].dt.year
df['Month'] = df['Transaction_Date'].dt.month
df['Day'] = df['Transaction_Date'].dt.day

print("\nData types after datetime conversion:")
print(df.dtypes)

# ========================== 2️⃣ Data Selection and Indexing ==========================
# All transactions in January 2024
jan_2024 = df[(df['Month'] == 1) & (df['Year'] == 2024)]
print("\nTransactions in January 2024:", jan_2024.shape[0])

# Amount > 1000 and Online
high_amount_online = df[(df['Amount'] > 1000) & (df['Transaction_Type'] == "Online")]
print("Transactions with Amount > 1000 & Online:", len(high_amount_online))

# Only Approved transactions
approved = df[df['Transaction_Status'].str.lower() == 'approved']

# ========================== 3️⃣ Data Manipulation and Feature Engineering ==========================
# Discounted_Amount (5% off if > $500)
df['Discounted_Amount'] = df['Amount'].apply(lambda x: x * 0.95 if x > 500 else x)

# Categorize Amount
def categorize_amount(amt):
    if amt < 100:
        return 'Low'
    elif 100 <= amt <= 500:
        return 'Medium'
    else:
        return 'High'

df['Amount_Category'] = df['Amount'].apply(categorize_amount)

# Drop Merchant if > 30% missing (checked on original data before filling)
original_missing_merchant = pd.read_csv('credit_card_transactions.csv')['Merchant'].isnull().mean()
if original_missing_merchant > 0.3:
    df = df.drop(columns=['Merchant'])
    print("Merchant column dropped (missing > 30%).")

# ========================== 4️⃣ Aggregation and Insights ==========================
total_per_category = df.groupby('Category')['Amount'].sum()
print("\nTotal transaction amount per Category:\n", total_per_category)

declined_per_mode = df[df['Transaction_Status'].str.lower() == 'declined'].groupby('Payment_Mode').size()
print("\nDeclined transactions per Payment_Mode:\n", declined_per_mode)

top_merchants = df['Merchant'].value_counts().head(5)
print("\nTop 5 most frequent merchants:\n", top_merchants)

avg_per_location = df.groupby('Location')['Amount'].mean()
print("\nAverage transaction amount per Location:\n", avg_per_location)

# ========================== 5️⃣ Fraud Detection Indicators ==========================
# Customers with >10 transactions in a single day
df['Date_Only'] = df['Transaction_Date'].dt.date
daily_tx = df.groupby(['Customer_ID', 'Date_Only']).size().reset_index(name='Count')
potential_fraud = daily_tx[daily_tx['Count'] > 10]['Customer_ID'].unique()
print("\nCustomers with >10 transactions in a single day (potential fraud):", potential_fraud)

# Same Customer_ID, different locations within 5 minutes
df_sorted = df.sort_values(['Customer_ID', 'Transaction_Date']).copy()
df_sorted['Time_Diff'] = df_sorted.groupby('Customer_ID')['Transaction_Date'].diff()
df_sorted['Loc_Diff'] = df_sorted.groupby('Customer_ID')['Location'].transform(lambda x: x != x.shift())

suspicious = df_sorted[
    (df_sorted['Time_Diff'] < timedelta(minutes=5)) &
    df_sorted['Loc_Diff'] &
    df_sorted['Time_Diff'].notna()
]
print("Suspicious transactions (same customer, different locations <5 min):", len(suspicious))

# High-risk: Amount > $5000 and Online
high_risk = df[(df['Amount'] > 5000) & (df['Transaction_Type'] == "Online")]
print("High-risk transactions (Amount > $5000 & Online):", len(high_risk))

# ========================== 6️⃣ Data Merging and Joining ==========================
customer_df = pd.read_csv('customer_info.csv')
merged_df = pd.merge(df, customer_df, on='Customer_ID', how='left')

# Average transaction amount per Age group
if 'Age' in merged_df.columns:
    merged_df['Age_Group'] = pd.cut(merged_df['Age'],
                                    bins=[0, 25, 40, 60, 100],
                                    labels=['Young', 'Adult', 'Middle-Aged', 'Senior'])
    avg_per_age_group = merged_df.groupby('Age_Group')['Amount'].mean()
    print("\nAverage transaction amount per Age Group:\n", avg_per_age_group)
```

**How to run**  
1. Save the script as `credit_card_analysis.py`.  
2. Place both CSV files in the same folder.  
3. Run `python credit_card_analysis.py`.

The script prints all required results directly to the console. You can also assign the DataFrames (`jan_2024`, `high_amount_online`, `total_per_category`, etc.) to variables for further use or export (`to_csv` / `to_excel`).  

This covers every bullet point in the case study with clear, production-ready Pandas code. Let me know if you need any modifications (e.g., specific date format, different missing-value strategy, or visualization with Matplotlib/Seaborn)!