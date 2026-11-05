### **Case Study: Analyzing IPL Matches with Pandas and Matplotlib**

#### **Problem Statement:**
You are a data analyst tasked with exploring trends in IPL matches. Your goal is to analyze a dataset of IPL matches to uncover insights like:
- Total matches played per season
- Most frequent match venues
- Toss decision patterns (fielding vs batting)
- Relationship between winning the toss and winning the match
- Top players with the most "Player of the Match" awards

---

### **Tools Used:**
1. **Pandas**: For loading, cleaning, and analyzing data.
2. **Matplotlib**: For creating visualizations.

---

### **Dataset:**
- **Source**: [Kaggle IPL Dataset](https://www.kaggle.com/nowke9/ipldata) (Download `matches.csv`).
- **Columns**: `id`, `season`, `city`, `date`, `team1`, `team2`, `toss_winner`, `toss_decision`, `result`, `winner`, etc.

---

### **Step-by-Step Analysis:**

#### **1. Install and Import Libraries**
```python
# Install libraries (run in terminal if needed)
# !pip install pandas matplotlib

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
```

#### **2. Load the Dataset**
```python
# Load the CSV file (update the path)
df = pd.read_csv('matches.csv')

# Display first 5 rows
print(df.head())
```
**Explanation**: `read_csv` loads the dataset, and `head()` shows the first 5 rows to preview the data.

---

#### **3. Explore the Data**
```python
# Check dataset shape (rows, columns)
print("Shape:", df.shape)

# Check column data types and missing values
print(df.info())
```
**Output**:  
- The dataset has 756 rows and 18 columns.  
- Columns like `city` and `winner` have missing values (we’ll handle this later).

---

#### **4. Clean the Data**
```python
# Drop rows with missing 'winner' (critical for analysis)
df.dropna(subset=['winner'], inplace=True)

# Drop unnecessary columns
df = df.drop(['id', 'date', 'umpire1'], axis=1)
```
**Explanation**:  
- `dropna` removes rows where the `winner` is missing.  
- `drop` removes columns irrelevant to our analysis.

---

#### **5. Analyze Matches Per Season**
```python
# Count matches per season
matches_per_season = df['season'].value_counts().sort_index()

# Plot results
plt.figure(figsize=(10, 5))
matches_per_season.plot(kind='bar', color='skyblue')
plt.title('Matches Played Per Season')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.show()
```
**Insight**:  
- The number of matches increased from 2008 to 2019 due to more teams.

---

#### **6. Top 10 Venues**
```python
# Get top 10 venues
top_venues = df['venue'].value_counts().head(10)

# Plot
plt.figure(figsize=(12, 6))
top_venues.plot(kind='bar', color='orange')
plt.title('Top 10 IPL Venues')
plt.xlabel('Venue')
plt.ylabel('Matches Played')
plt.xticks(rotation=45)
plt.show()
```
**Insight**:  
- **Eden Gardens** and **Wankhede Stadium** host the most matches.

---

#### **7. Toss Decisions (Bat vs Field)**
```python
# Calculate toss decision counts
toss_decisions = df['toss_decision'].value_counts()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(toss_decisions, labels=toss_decisions.index, autopct='%1.1f%%')
plt.title('Toss Decisions')
plt.show()
```
**Insight**:  
- Teams prefer **fielding first** (61.2%) after winning the toss.

---

#### **8. Toss Winner vs Match Winner**
```python
# Calculate how often toss winner is the match winner
toss_win_match_win = df[df['toss_winner'] == df['winner']].shape[0]
total_matches = df.shape[0]
percentage = (toss_win_match_win / total_matches) * 100

print(f"{percentage:.2f}% of matches were won by the toss winner.")
```
**Output**:  
- **52.89%** of matches are won by the toss winner.

---

#### **9. Top Players of the Match**
```python
# Get top 10 players
top_players = df['player_of_match'].value_counts().head(10)

# Plot
plt.figure(figsize=(12, 6))
top_players.plot(kind='bar', color='green')
plt.title('Top 10 Players of the Match')
plt.xlabel('Player')
plt.ylabel('Awards')
plt.show()
```
**Insight**:  
- **Chris Gayle** and **AB de Villiers** have the most awards.

---
