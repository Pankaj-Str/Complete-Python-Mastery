# Visualizing Data with Matplotlib  
**PS4 Sales Analysis**  
*Discovering Matplotlib Basics + Enhancing Visuals*

This complete, hands-on tutorial uses a realistic **PS4 games sales dataset** (10 popular titles with regional and global sales in millions). You'll learn Matplotlib from scratch and then level up your charts with professional enhancements.

## Step 0: Setup & Load the Dataset

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the sample dataset (copy-paste this!)
data = {
    'Game': ['The Last of Us Part II', 'God of War', 'Marvel\'s Spider-Man', 'Horizon Zero Dawn', 'Uncharted 4: A Thief\'s End', 
             'Persona 5', 'Death Stranding', 'Red Dead Redemption 2', 'Final Fantasy VII Remake', 'The Witcher 3: Wild Hunt'],
    'Year': [2020, 2018, 2018, 2017, 2016, 2016, 2019, 2018, 2020, 2015],
    'Genre': ['Action-Adventure', 'Action-Adventure', 'Action-Adventure', 'Action-RPG', 'Action-Adventure',
              'Role-Playing', 'Action-Adventure', 'Action-Adventure', 'Role-Playing', 'Action-RPG'],
    'Publisher': ['Sony Interactive Entertainment', 'Sony Interactive Entertainment', 'Sony Interactive Entertainment', 
                  'Sony Interactive Entertainment', 'Sony Interactive Entertainment', 'Atlus', 
                  'Sony Interactive Entertainment', 'Rockstar Games', 'Square Enix', 'CD Projekt RED'],
    'North America': [3.5, 4.5, 6.0, 2.8, 4.0, 1.2, 1.5, 5.5, 1.8, 2.0],
    'Europe': [2.0, 3.0, 4.0, 2.5, 3.5, 0.8, 1.0, 4.0, 1.2, 1.5],
    'Japan': [0.5, 0.8, 0.3, 1.0, 0.4, 2.5, 0.6, 0.2, 1.5, 0.3],
    'Rest of World': [1.0, 1.5, 2.0, 1.2, 1.5, 0.5, 0.8, 2.0, 0.7, 0.8],
    'Global': [7.0, 9.8, 12.3, 7.5, 9.4, 5.0, 3.9, 11.7, 5.2, 4.6]
}

df = pd.DataFrame(data)
print(df)
```

**Your dataset is ready!** (You can also save it with `df.to_csv('ps4_sales.csv', index=False)` and load later with `df = pd.read_csv('ps4_sales.csv')`.)

## Part 1: Discovering Matplotlib Basics

### 1.1 Your First Chart – Basic Bar Plot  
Global sales by game (the most common starting visualization).

```python
plt.figure(figsize=(10, 6))
plt.bar(df['Game'], df['Global'])
plt.title('Basic Bar Chart: Global Sales by Game')
plt.xlabel('Game')
plt.ylabel('Global Sales (millions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()   # or plt.savefig('my_chart.png')
```

**What you get:**



### 1.2 Basic Line Plot – Sales Trend Over Years

```python
sales_by_year = df.groupby('Year')['Global'].sum().sort_index()

plt.figure(figsize=(8, 5))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o')
plt.title('Basic Line Plot: Total Global Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Global Sales (millions)')
plt.grid(True)
plt.xticks(sales_by_year.index)
plt.show()
```

**What you get:**



### 1.3 Basic Pie Chart – Sales by Genre

```python
genre_sales = df.groupby('Genre')['Global'].sum()

plt.figure(figsize=(8, 8))
plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%')
plt.title('Basic Pie Chart: Global Sales by Genre')
plt.axis('equal')
plt.show()
```

**What you get:**



**Basics learned:** `plt.figure()`, `plt.bar()`, `plt.plot()`, `plt.pie()`, titles, labels, and `plt.show()` / `savefig()`.

## Part 2: Enhancing Visuals with Matplotlib

Now we turn basic charts into publication-ready visuals.

### 2.1 Enhanced Bar Chart (colors, sorting, value labels, grid)

```python
df_sorted = df.sort_values('Global', ascending=False)

plt.figure(figsize=(12, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(df_sorted)))
bars = plt.bar(df_sorted['Game'], df_sorted['Global'], color=colors)

plt.title('Enhanced Bar Chart: Global Sales by Game (Sorted)', fontsize=14, pad=20)
plt.xlabel('Game', fontsize=12)
plt.ylabel('Global Sales (millions)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.3, f'{height:.1f}', 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
```

**What you get (much cleaner and more informative):**



### 2.2 Enhanced Line Plot (color, annotations, thicker lines)

```python
plt.figure(figsize=(8, 5))
plt.plot(sales_by_year.index, sales_by_year.values, 
         marker='o', linestyle='-', color='#e74c3c', linewidth=2.5, 
         markersize=10, markerfacecolor='white', markeredgewidth=2)

plt.title('Enhanced Line Plot: Total Global Sales by Year', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Global Sales (millions)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(sales_by_year.index)

# Annotate each point
for x, y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x, y + 0.4, f'{y:.1f}', ha='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()
```

**What you get:**



### 2.3 Enhanced Pie Chart (colors, explode, shadow, legend)

```python
plt.figure(figsize=(10, 8))
colors_pie = ['#3498db', '#2ecc71', '#e74c3c', '#f1c40f']
explode = [0.1 if genre == 'Role-Playing' else 0 for genre in genre_sales.index]

plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%', 
        colors=colors_pie, startangle=90, explode=explode, shadow=True)

plt.title('Enhanced Pie Chart: Global Sales by Genre', fontsize=14)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1))
plt.axis('equal')
plt.tight_layout()
plt.show()
```

**What you get:**



### 2.4 Advanced: Stacked Bar Chart – Regional Sales by Genre

```python
region_by_genre = df.groupby('Genre')[['North America', 'Europe', 'Japan', 'Rest of World']].sum()

plt.figure(figsize=(10, 6))
region_by_genre.plot(kind='bar', stacked=True, colormap='tab20')

plt.title('Stacked Bar Chart: Regional Sales Breakdown by Genre')
plt.xlabel('Genre')
plt.ylabel('Sales (millions)')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
```

**What you get:**



## Next Steps & Pro Tips

- **Style everything at once**: `plt.style.use('seaborn-v0_8')` or `ggplot`
- **Subplots**: Use `fig, axes = plt.subplots(2, 2)` for multiple charts in one figure
- **Save high-quality images**: `plt.savefig('sales_analysis.png', dpi=300, bbox_inches='tight')`
- **Interactive**: Try `plt.show(block=False)` or export to HTML with Plotly later

You now have a complete PS4 sales analysis dashboard built purely with Matplotlib!  

