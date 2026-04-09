# Data Preprocessing & Visualization – Automobile Data

---

### Step 1: Install Libraries (Run once)

Open your terminal / command prompt and run:

```bash
pip install pandas matplotlib seaborn
```

---

### Step 2: Import the Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Make plots look nice
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
```

---

### Step 3: Load the Dataset

The original file uses “?” for missing values and has no header row.

```python
# URL of the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# Column names (official order)
columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration",
           "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base",
           "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders",
           "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
           "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Load data and treat "?" as NaN
df = pd.read_csv(url, header=None, names=columns, na_values='?')

print("Dataset loaded successfully!")
print("Shape:", df.shape)          # (205, 26)
print("Columns:", df.columns.tolist())
```

---

### Step 4: Basic Exploration (Understand your data)

```python
# First few rows
df.head()

# Data types and missing values
df.info()

# Summary statistics
df.describe(include='all')

# Count of missing values per column
missing = df.isnull().sum()
print(missing[missing > 0])   # Shows only columns with missing values
```

**What you will see:**
- 5 numeric columns are stored as `object` because of the “?” values.
- Missing values in: `normalized-losses` (~41), `price` (4), `horsepower` (2), etc.

---

### Step 5: Data Preprocessing (Cleaning)

#### 5.1 Convert data types

```python
# Columns that should be numeric
numeric_cols = ['normalized-losses', 'bore', 'stroke', 'horsepower', 
                'peak-rpm', 'price']

df[numeric_cols] = df[numeric_cols].astype(float)
```

#### 5.2 Handle missing values (Beginner approach)

```python
# 1. Drop rows where price is missing (price is usually our target variable)
df = df.dropna(subset=['price'])

# 2. Fill remaining missing values with median (robust to outliers)
df['normalized-losses'] = df['normalized-losses'].fillna(df['normalized-losses'].median())
df['bore']               = df['bore'].fillna(df['bore'].median())
df['stroke']             = df['stroke'].fillna(df['stroke'].median())
df['horsepower']         = df['horsepower'].fillna(df['horsepower'].median())
df['peak-rpm']           = df['peak-rpm'].fillna(df['peak-rpm'].median())

print("Missing values after cleaning:", df.isnull().sum().sum())  # Should be 0
```

#### 5.3 Check for duplicates

```python
print("Duplicate rows:", df.duplicated().sum())
# df = df.drop_duplicates()   # Uncomment if any duplicates exist
```

#### 5.4 (Optional) Create a useful new column

```python
# Average mileage
df['avg-mpg'] = (df['city-mpg'] + df['highway-mpg']) / 2
```

**Your data is now clean and ready for visualization!**

---

### Step 6: Visualization with Matplotlib & Seaborn

#### 6.1 Univariate Analysis (Single variable)

```python
# 1. Distribution of Price
plt.figure(figsize=(10,6))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribution of Car Prices')
plt.xlabel('Price (USD)')
plt.ylabel('Count')
plt.show()

# 2. Boxplot of Price (helps see outliers)
plt.figure(figsize=(8,5))
sns.boxplot(x=df['price'])
plt.title('Boxplot of Car Prices')
plt.show()

# 3. Countplot of Car Makes (most popular brands)
plt.figure(figsize=(12,6))
sns.countplot(data=df, y='make', order=df['make'].value_counts().index, palette='viridis')
plt.title('Number of Cars by Make')
plt.xlabel('Count')
plt.ylabel('Make')
plt.show()
```

#### 6.2 Bivariate Analysis (Relationship between two variables)

```python
# 4. Engine Size vs Price (strong positive correlation)
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='engine-size', y='price', hue='fuel-type', size='curb-weight', alpha=0.7)
plt.title('Engine Size vs Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.show()

# 5. Price by Body Style
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='body-style', y='price')
plt.title('Price Distribution by Body Style')
plt.xticks(rotation=45)
plt.show()

# 6. Horsepower vs City MPG
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='horsepower', y='city-mpg', hue='fuel-type')
plt.title('Horsepower vs City MPG')
plt.show()
```

#### 6.3 Multivariate / Correlation Analysis

```python
# 7. Correlation Heatmap (only numeric columns)
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(12,10))
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# 8. Pairplot (small selection of important columns)
cols = ['price', 'engine-size', 'curb-weight', 'horsepower', 'avg-mpg']
sns.pairplot(df[cols], diag_kind='kde', corner=True)
plt.show()
```

#### 6.4 Categorical Analysis

```python
# 9. Price by Fuel Type & Aspiration
plt.figure(figsize=(10,6))
sns.barplot(data=df, x='fuel-type', y='price', hue='aspiration')
plt.title('Average Price by Fuel Type and Aspiration')
plt.show()

# 10. Drive Wheels vs Price
plt.figure(figsize=(8,5))
sns.violinplot(data=df, x='drive-wheels', y='price')
plt.title('Price Distribution by Drive Wheels')
plt.show()
```

---

### Step 7: Save Your Work (Optional)

```python
# Save cleaned dataset
df.to_csv('cleaned_automobile_data.csv', index=False)

# Save any plot
plt.savefig('price_distribution.png', dpi=300, bbox_inches='tight')
```

---

### Summary of What You Learned

| Step                  | Tools Used          | Key Skills Practiced                     |
|-----------------------|---------------------|------------------------------------------|
| Loading data          | pandas              | `read_csv`, handling missing-value symbols |
| Exploration           | pandas              | `info()`, `describe()`, `isnull()`       |
| Cleaning              | pandas              | type conversion, `fillna`, `dropna`      |
| Visualization         | seaborn + matplotlib | histplot, boxplot, scatterplot, heatmap  |

You now have a **complete beginner-level pipeline** for any tabular dataset!

**Next Level Ideas (after you finish this):**
- Build a simple regression model to predict price
- Create interactive plots with Plotly
- Try the same steps on any Kaggle car dataset

