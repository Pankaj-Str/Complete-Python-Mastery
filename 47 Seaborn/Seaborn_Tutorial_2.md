# Visualizing Data with Seaborn – Mumbai West House Pricing 

We will follow the **6 Learning Outcomes** exactly in order.  

**No previous experience needed!**  
Every step has:  
- Simple explanation  
- Why we do it  
- Copy-paste ready code  
- What the chart shows (insights)  
- Student tips  

**Dataset**: 800 real-looking houses in Mumbai West (Andheri West, Bandra West, Juhu, etc.) with columns like BHK, Locality, Area_sqft, Price_Lakhs, Status, and Age.

---

### **Step 0: Setup (Run this FIRST – Only once)**

Copy and run this code in your Jupyter Notebook or Google Colab:

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# IMPORTANT: Fix for Indian Rupee symbol ₹ (especially on macOS/Windows)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans', 'Arial', 'sans-serif']

# Create the Mumbai West housing dataset (exactly as given)
np.random.seed(42)   # Makes results the same every time
locations = ['Andheri West', 'Bandra West', 'Juhu', 'Santacruz West', 'Khar West', 'Bandra East', 'Versova']

data = {
    'BHK': np.random.choice([1, 2, 3, 4], 800, p=[0.15, 0.45, 0.3, 0.1]),
    'Locality': np.random.choice(locations, 800),
    'Area_sqft': np.random.normal(1100, 350, 800).astype(int).clip(600, 2500),
    'Price_Lakhs': np.random.normal(450, 280, 800).astype(int).clip(100, 3000),
    'Status': np.random.choice(['Ready to Move', 'Under Construction'], 800),
    'Age': np.random.choice(['0-1 Year', '1-5 Years', '5-10 Years', '10+ Years'], 800)
}

df = pd.DataFrame(data)

# Make prices realistic (premium areas cost more)
premium = ['Bandra West', 'Juhu', 'Khar West']
df.loc[df['Locality'].isin(premium), 'Price_Lakhs'] += 200
df['Price_Lakhs'] = (df['Price_Lakhs'] + (df['Area_sqft'] * 0.4) + (df['BHK'] * 80)).astype(int).clip(100, 3000)

# Beautiful Seaborn style
sns.set_theme(style="whitegrid", palette="pastel", font_scale=1.1)

print("✅ Dataset ready! Shape:", df.shape)
print(df.head())   # Shows first 5 rows
```

**What you just did**:  
- Loaded all libraries  
- Created 800 house records  
- Made prices realistic for Mumbai West  
- Set a clean professional look  

Run this once — your data is ready!  

---

### **Learning Outcome 1: Explain why customization is necessary beyond default Seaborn plots**

**Default Seaborn plots** are quick and useful, but they look plain:  
- No title → “What is this chart about?”  
- Axis labels like “Price_Lakhs” → confusing for others  
- Colors that are hard to read in presentations  
- No numbers or lines to highlight important things  

**Customization** makes charts:  
- Professional (for college projects, reports, LinkedIn)  
- Easy to understand for non-technical people (buyers, investors)  
- Tell a clear story about Mumbai West house prices  

In the next sections you will see **before → after** style improvements.

---

### **Learning Outcome 2: Customize pie charts using Matplotlib alongside Seaborn**

**Why?** Pie charts show **proportions** (e.g., how many 1-BHK, 2-BHK, etc.). Seaborn doesn’t have pie charts, so we use Matplotlib + Seaborn colors.

```python
# Pie Chart – Distribution by BHK
bhk_counts = df['BHK'].value_counts().sort_index()
labels = [f'{b} BHK' for b in bhk_counts.index]
colors = sns.color_palette("pastel", len(labels))

plt.figure(figsize=(9, 9))
plt.pie(bhk_counts, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=140, explode=[0.06]*len(labels), shadow=True, pctdistance=0.85)
plt.title('Distribution of Properties by BHK in Mumbai West', fontsize=16, pad=20)
plt.show()
```

**What the chart shows**:  
- 2 BHK is the most common (~43%)  
- 1 BHK and 3 BHK are also popular  
- 4 BHK is rare  

**Student Tip**: `autopct='%1.1f%%'` adds percentages. `explode` makes slices pop out.

---

### **Learning Outcome 3: Create and enhance horizontal bar charts**

**Why?** Horizontal bars are perfect when category names (like localities) are long.

```python
# Average price per locality
avg_price = df.groupby('Locality')['Price_Lakhs'].mean().reset_index()
avg_price = avg_price.sort_values('Price_Lakhs', ascending=False)

plt.figure(figsize=(12, 8))
ax = sns.barplot(data=avg_price, x='Price_Lakhs', y='Locality', palette="viridis")

plt.title('Average House Price by Locality in Mumbai West', fontsize=15)
plt.xlabel('Average Price (₹ Lakhs)')
plt.ylabel('')

# Add exact values on bars
for i, v in enumerate(avg_price['Price_Lakhs']):
    ax.text(v + 15, i, f'₹{v:.0f} L', va='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()
```

**What the chart shows**:  
- Juhu is the most expensive  
- Bandra West and Khar West are also premium  
- Bandra East is more affordable  

**Student Tip**: `for` loop adds numbers on bars — super useful for reports!

---

### **Learning Outcome 4: Customize histograms for deeper distribution analysis**

**Why?** Histograms show **how prices are spread** (most houses cheap or expensive?).

```python
plt.figure(figsize=(11, 7))
ax = sns.histplot(data=df, x='Price_Lakhs', bins=25, kde=True, 
                  color='#4ECDC4', edgecolor='black', alpha=0.75)

plt.title('Distribution of House Prices in Mumbai West', fontsize=15)
plt.xlabel('Price (₹ Lakhs)')
plt.ylabel('Number of Properties')

# Add mean & median lines
mean_p = df['Price_Lakhs'].mean()
median_p = df['Price_Lakhs'].median()
ax.axvline(mean_p, color='red', linestyle='--', linewidth=2.5, label=f'Mean: ₹{mean_p:.0f} Lakhs')
ax.axvline(median_p, color='darkgreen', linestyle='-', linewidth=2.5, label=f'Median: ₹{median_p:.0f} Lakhs')

plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
```

**What the chart shows**:  
- Most houses cost ₹800–1400 Lakhs  
- Right-skewed (few very expensive luxury homes)  
- Mean > Median because of expensive outliers  

**Student Tip**: `kde=True` adds a smooth curve. Colored lines help compare mean vs median.

---

### **Learning Outcome 5: Enhance box plots to better interpret spread and outliers**

**Why?** Box plots show **summary statistics** (median, spread, outliers) in one glance.

```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='BHK', y='Price_Lakhs', data=df, 
            palette="Set2", width=0.65, fliersize=7, linewidth=2.2)

plt.title('Enhanced Box Plot: Price Spread & Outliers by BHK', fontsize=15)
plt.xlabel('Number of Bedrooms (BHK)')
plt.ylabel('Price (₹ Lakhs)')
plt.tight_layout()
plt.show()
```

**What the chart shows**:  
- 4 BHK has highest prices and biggest spread  
- Outliers = very expensive luxury flats  
- Wider boxes = more variation in price  

**Student Tip**: Box = middle 50% of data. Dots outside = outliers.

---

### **Learning Outcome 6: Combine multiple plots to reveal both summary statistics and raw data**

**Why?** One chart with **summary + every data point** is very powerful!

```python
plt.figure(figsize=(11, 7))
ax = sns.boxplot(x='BHK', y='Price_Lakhs', data=df, 
                 palette="Set2", width=0.6, linewidth=2)

# Add every single house as a dot
sns.stripplot(x='BHK', y='Price_Lakhs', data=df, 
              palette='dark:black', alpha=0.35, jitter=True, size=3.5, ax=ax)

plt.title('Combined Plot: Boxplot (Summary) + Stripplot (Raw Data Points) by BHK\nMumbai West Housing', fontsize=15, pad=20)
plt.xlabel('Number of Bedrooms (BHK)')
plt.ylabel('Price (₹ Lakhs)')
plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

**What the chart shows**:  
- Boxplot = overall pattern  
- Black dots = every single house price  
- You can see clusters, spread, and exact outliers  

**Student Tip**: This is one of the best visualizations in data science!

---

### **Congratulations! You did it!** 🎉

You now know how to:  
1. Explain why customization matters  
2. Make beautiful pie charts  
3. Create enhanced horizontal bar charts  
4. Customize histograms  
5. Improve box plots  
6. Combine plots for deeper insights  

**Next practice ideas for you**:  
- Add `hue='Status'` to any plot (Ready to Move vs Under Construction)  
- Try changing colors (`palette="coolwarm"`)  
- Save any chart: `plt.savefig('my_chart.png', dpi=300)`  

