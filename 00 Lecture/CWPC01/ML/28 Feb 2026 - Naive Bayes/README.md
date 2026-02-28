
# Naive Bayes Machine Learning

Welcome to this easy-to-follow tutorial on **Naive Bayes**, a simple yet powerful machine learning algorithm used for classification tasks. By the end of this tutorial, you’ll understand what Naive Bayes is, how it works, its types, and how to implement it in Python with a real-world example.

---

## Table of Contents
1. What is Naive Bayes?
2. Bayes' Theorem (The Math Behind It)
3. Types of Naive Bayes Classifiers
4. Naive Bayes Classifier Explained
5. Step-by-Step Example: Predicting Email Spam
   - Step 1: Import Libraries
   - Step 2: Load and Prepare Data
   - Step 3: Train the Naive Bayes Model
   - Step 4: Make Predictions
   - Step 5: Evaluate the Model
6. Pros and Cons of Naive Bayes
7. Conclusion

---

## 1. What is Naive Bayes?

**Naive Bayes** is a classification algorithm based on probability. It’s called "naive" because it assumes that all features (or inputs) in your data are independent of each other, which simplifies calculations. Despite this assumption, it works surprisingly well for many real-world problems, like:

- **Spam email detection** (Is an email spam or not?)
- **Sentiment analysis** (Is a movie review positive or negative?)
- **Document classification** (Which category does a news article belong to?)

It’s fast, easy to understand, and great for beginners!

---

## 2. Bayes' Theorem (The Math Behind It)

Naive Bayes is built on **Bayes' Theorem**, a rule from probability theory. Don’t worry—it’s simpler than it sounds! Bayes' Theorem helps us calculate the probability of an event based on prior knowledge.

### Bayes' Theorem Formula:
![image](https://github.com/user-attachments/assets/c2c347b1-df68-4a5f-820e-bc724a58a69d)


In Naive Bayes, we use this to predict the class (e.g., spam or not spam) that’s most likely based on the input features.

### Why "Naive"?
The algorithm assumes features (like words in an email) are independent. For example, it assumes the word "free" and "win" in an email don’t influence each other’s probability. This isn’t always true in real life, but it makes the math easier and still gives good results.

---

## 3. Types of Naive Bayes Classifiers

There are three main types of Naive Bayes classifiers, depending on the type of data you’re working with:

1. **Gaussian Naive Bayes**:
   - Used when your features are continuous (e.g., numbers like height, weight).
   - Assumes the data follows a normal (Gaussian) distribution.

2. **Multinomial Naive Bayes**:
   - Used for discrete data, like word counts in text (e.g., how many times "free" appears in an email).
   - Common in text classification tasks like spam detection.

3. **Bernoulli Naive Bayes**:
   - Used for binary/boolean data (e.g., whether a word appears in an email or not, 0 or 1).
   - Also used in text classification but focuses on presence/absence of features.

We’ll use **Multinomial Naive Bayes** in our example because it’s great for text data.

---

## 4. Naive Bayes Classifier Explained

A **Naive Bayes Classifier** predicts the class of an item by:
1. Calculating the probability of each class based on the input features.
2. Picking the class with the highest probability.

For example, in spam detection:
- Input: An email with words like "free," "win," and "offer."
- Classes: Spam or Not Spam.
- The classifier calculates:
  - Probability the email is Spam given these words.
  - Probability the email is Not Spam given these words.
- It chooses the class with the higher probability.

It’s like a detective weighing evidence to make a decision!

---

## 5. Step-by-Step Example: Predicting Email Spam

Let’s build a Naive Bayes model to classify emails as **Spam** or **Not Spam** using Python. We’ll use a small dataset and the `scikit-learn` library, which is perfect for beginners.

### Prerequisites
- Install Python and the following libraries:
  ```bash
  pip install scikit-learn pandas numpy
  ```
- Basic understanding of Python (don’t worry, we’ll keep the code simple!).

### Step 1: Import Libraries

```python
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
```

- **pandas**: To handle data.
- **scikit-learn**: For machine learning tools like Naive Bayes and text processing.
- **CountVectorizer**: Converts text into numbers (word counts).

### Step 2: Load and Prepare Data

For simplicity, we’ll create a small dataset of emails and their labels (Spam or Not Spam).

```python
# Create a sample dataset
data = {
    'email': [
        'Win a free lottery now',
        'Hi, how are you today',
        'Free offer just for you',
        'Meeting at 10 AM tomorrow',
        'Get rich quick free',
        'Your invoice is ready'
    ],
    'label': ['Spam', 'Not Spam', 'Spam', 'Not Spam', 'Spam', 'Not Spam']
}

# Convert to a pandas DataFrame
df = pd.DataFrame(data)

# Show the dataset
print("Dataset:")
print(df)
```

**Output**:
```
   email                       label
0  Win a free lottery now      Spam
1  Hi, how are you today       Not Spam
2  Free offer just for you     Spam
3  Meeting at 10 AM tomorrow   Not Spam
4  Get rich quick free         Spam
5  Your invoice is ready       Not Spam
```

Now, we need to convert the text (emails) into numbers so the algorithm can understand it.

```python
# Convert text to numbers using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['email'])

# Labels (Spam or Not Spam)
y = df['label']

# Show the feature names (words)
print("\nFeature names (words):")
print(vectorizer.get_feature_names_out())
```

**Explanation**:
- **CountVectorizer** turns each email into a vector of word counts (e.g., how many times "free" appears).
- `X` is the numerical representation of emails.
- `y` is the labels (Spam or Not Spam).

### Step 3: Train the Naive Bayes Model

We’ll split the data into training and testing sets, then train a **Multinomial Naive Bayes** model.

```python
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

print("\nModel trained successfully!")
```

**Explanation**:
- `train_test_split`: Splits data so we can test the model on unseen emails.
- `MultinomialNB`: The Naive Bayes classifier for text data.
- `model.fit`: Trains the model on the training data.

### Step 4: Make Predictions

Let’s predict whether new emails are Spam or Not Spam.

```python
# New emails to classify
new_emails = [
    'Free money for you',
    'Let’s have a meeting tomorrow'
]

# Convert new emails to numbers
new_emails_transformed = vectorizer.transform(new_emails)

# Predict
predictions = model.predict(new_emails_transformed)

# Show predictions
print("\nPredictions for new emails:")
for email, prediction in zip(new_emails, predictions):
    print(f"Email: {email} -> Predicted: {prediction}")
```

**Output** (may vary slightly):
```
Predictions for new emails:
Email: Free money for you -> Predicted: Spam
Email: Let’s have a meeting tomorrow -> Predicted: Not Spam
```

**Explanation**:
- We converted the new emails into numbers using the same `vectorizer`.
- The model predicted their classes based on what it learned.

### Step 5: Evaluate the Model

Let’s check how well the model performs on the test set.

```python
# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy on test set: {accuracy*100:.2f}%")

# Show confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=['Spam', 'Not Spam'])
print("\nConfusion Matrix:")
print(pd.DataFrame(cm, index=['Actual Spam', 'Actual Not Spam'], columns=['Predicted Spam', 'Predicted Not Spam']))
```

**Output** (example):
```
Accuracy on test set: 100.00%

Confusion Matrix:
                  Predicted Spam  Predicted Not Spam
Actual Spam                   1                  0
Actual Not Spam               0                  1
```

**Explanation**:
- **Accuracy**: Percentage of correct predictions.
- **Confusion Matrix**: Shows true vs. predicted labels (e.g., how many Spams were correctly predicted).

---

## 6. Pros and Cons of Naive Bayes

### Pros:
- **Fast and efficient**: Works well with large datasets.
- **Simple to understand**: Great for beginners.
- **Good for text data**: Excels in tasks like spam detection and sentiment analysis.
- **Handles small datasets**: Performs well even with limited data.

### Cons:
- **Naive assumption**: Assumes features are independent, which isn’t always true.
- **Limited for complex problems**: May not perform as well as advanced models like neural networks.
- **Sensitive to imbalanced data**: Needs balanced classes for best results.

---

## 7. Conclusion

Congratulations! You’ve learned about **Naive Bayes**, its foundation in Bayes' Theorem, the different types of classifiers, and how to build a Naive Bayes model in Python. You even classified emails as Spam or Not Spam!

To practice more:
- Try a larger dataset, like the [SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection).
- Experiment with **Gaussian** or **Bernoulli** Naive Bayes for different types of data.
- Explore other text preprocessing techniques, like removing stop words (e.g., "the," "is").

Keep coding, and you’ll master machine learning in no time!

---

### Full Python Code

Here’s the complete code for reference:

```python
# Import libraries
 polystyrene
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Create a sample dataset
data = {
    'email': [
        'Win a free lottery now',
        'Hi, how are you today',
        'Free offer just for you',
        'Meeting at 10 AM tomorrow',
        'Get rich quick free',
        'Your invoice is ready'
    ],
    'label': ['Spam', 'Not Spam', 'Spam', 'Not Spam', 'Spam', 'Not Spam']
}
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['email'])
y = df['label']
print("\nFeature names (words):")
print(vectorizer.get_feature_names_out())

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)
print("\nModel trained successfully!")

# Predict on new emails
new_emails = [
    'Free money for you',
    'Let’s have a meeting tomorrow'
]
new_emails_transformed = vectorizer.transform(new_emails)
predictions = model.predict(new_emails_transformed)
print("\nPredictions for new emails:")
for email, prediction in zip(new_emails, predictions):
    print(f"Email: {email} -> Predicted: {prediction}")

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy on test set: {accuracy*100:.2f}%")
cm = confusion_matrix(y_test, y_pred, labels=['Spam', 'Not Spam'])
print("\nConfusion Matrix:")
print(pd.DataFrame(cm, index=['Actual Spam', 'Actual Not Spam'], columns=['Predicted Spam', 'Predicted Not Spam']))
```

---

# Naive Bayes Classification : Fever Prediction Example

---

```python
# Naive Bayes Classification: Fever Prediction Example
# ====================================================
# This is a complete Python script for implementing Naive Bayes classification
# using the example from the tutorial (predicting Fever based on Flu and COVID symptoms).
# We'll use scikit-learn for the machine learning part, pandas for data handling,
# and matplotlib for charting.
#
# Key Steps in the Code:
# 1. Import necessary libraries.
# 2. Prepare the dataset: Create a pandas DataFrame from the training data.
# 3. Encode categorical data: Convert 'Yes'/'No' to 1/0 for features and target.
# 4. Split data: Although the dataset is small, we'll simulate train/test split.
# 5. Train the model: Use CategoricalNB (suitable for categorical features).
# 6. Make predictions: Predict for new data (Flu=Yes, COVID=Yes).
# 7. Evaluate: Compute accuracy and confusion matrix.
# 8. Visualize: Create a bar chart for predicted probabilities and a heatmap for confusion matrix.
#
# Requirements:
# - Python 3.x
# - Install libraries if needed: pip install pandas scikit-learn matplotlib seaborn
#
# Run this script in a Python environment (e.g., Jupyter Notebook or VS Code) to see the output and charts.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step 1: Prepare the Dataset
# The dataset has 10 patients with features: Flu (Yes/No), COVID (Yes/No), and target: Fever (Yes/No)
data = {
    'Flu': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No'],
    'COVID': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No'],
    'Fever': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

# Step 2: Encode Categorical Data
# Convert 'Yes' to 1 and 'No' to 0 for machine learning
df_encoded = df.copy()
df_encoded['Flu'] = df_encoded['Flu'].map({'Yes': 1, 'No': 0})
df_encoded['COVID'] = df_encoded['COVID'].map({'Yes': 1, 'No': 0})
df_encoded['Fever'] = df_encoded['Fever'].map({'Yes': 1, 'No': 0})

print("\nEncoded Dataset:")
print(df_encoded)

# Step 3: Split Data into Features (X) and Target (y)
X = df_encoded[['Flu', 'COVID']]  # Features
y = df_encoded['Fever']          # Target

# Simulate train/test split (80% train, 20% test). For small data, this is for demonstration.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining Features (X_train):")
print(X_train)
print("\nTraining Target (y_train):")
print(y_train)

# Step 4: Train the Naive Bayes Model
# Using CategoricalNB, which handles categorical features and applies Laplace smoothing by default (alpha=1.0)
model = CategoricalNB()
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# Step 5: Make Predictions
# Predict on test data
y_pred = model.predict(X_test)

# New data example: Flu=Yes (1), COVID=Yes (1)
new_data = pd.DataFrame({'Flu': [1], 'COVID': [1]})
new_pred = model.predict(new_data)
new_prob = model.predict_proba(new_data)  # Get probabilities for each class

print("\nPrediction on Test Data:")
print(y_pred)
print("\nPrediction for New Data (Flu=Yes, COVID=Yes):")
print("Predicted Fever:", 'Yes' if new_pred[0] == 1 else 'No')
print("Probabilities [No, Yes]:", new_prob[0])

# Step 6: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("Confusion Matrix:")
print(conf_matrix)

# Step 7: Visualize the Results
# Chart 1: Bar Chart for Predicted Probabilities on New Data
classes = ['No Fever (0)', 'Fever (1)']
plt.figure(figsize=(8, 5))
plt.bar(classes, new_prob[0], color=['blue', 'green'])
plt.title('Predicted Probabilities for New Data (Flu=Yes, COVID=Yes)')
plt.ylabel('Probability')
plt.ylim(0, 1)
plt.grid(axis='y')
for i, v in enumerate(new_prob[0]):
    plt.text(i, v + 0.01, f"{v:.2f}", ha='center')
plt.show()

# Chart 2: Heatmap for Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
plt.title('Confusion Matrix Heatmap')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Explanation of Charts:
# - Bar Chart: Shows the probability of 'No Fever' vs. 'Fever' for the new patient.
#   Higher bar indicates the predicted class.
# - Confusion Matrix Heatmap: Visualizes how well the model performed on test data.
#   Diagonal values are correct predictions; off-diagonals are errors.

# End of Script
# You can extend this by adding more data or features for better accuracy.
```
## Python implementation of a Naive Bayes Classification for the fever prediction example, tailored for beginners.

```python
import numpy as np
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Step 1: Create the dataset (from the transcript)
# Features: Flu (Yes/No), COVID (Yes/No)
# Target: Fever (Yes/No)
data = {
    'Flu': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No'],
    'COVID': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No'],
    'Fever': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

# Convert to DataFrame for easier handling
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Step 2: Preprocess the data (encode categorical variables)
# LabelEncoder converts Yes/No to 1/0
le_flu = LabelEncoder()
le_covid = LabelEncoder()
le_fever = LabelEncoder()

df['Flu'] = le_flu.fit_transform(df['Flu'])  # Yes=1, No=0
df['COVID'] = le_covid.fit_transform(df['COVID'])  # Yes=1, No=0
df['Fever'] = le_fever.fit_transform(df['Fever'])  # Yes=1, No=0

# Separate features (X) and target (y)
X = df[['Flu', 'COVID']].values
y = df['Fever'].values

# Step 3: Initialize and train the Categorical Naive Bayes model
# alpha=1 enables Laplace smoothing to handle zero probabilities
model = CategoricalNB(alpha=1.0)
model.fit(X, y)

# Step 4: Predict for new data (Flu = Yes, COVID = Yes)
# Encode the new data point
new_data = np.array([[le_flu.transform(['Yes'])[0], le_covid.transform(['Yes'])[0]]])  # [1, 1]
prediction = model.predict(new_data)
prediction_proba = model.predict_proba(new_data)

# Decode prediction back to Yes/No
prediction_label = le_fever.inverse_transform(prediction)[0]
proba_yes = prediction_proba[0][1]  # Probability of Fever = Yes
proba_no = prediction_proba[0][0]   # Probability of Fever = No

print("\nPrediction for Flu = Yes, COVID = Yes:")
print(f"Predicted Fever: {prediction_label}")
print(f"Probability of Fever = Yes: {proba_yes:.3f}")
print(f"Probability of Fever = No: {proba_no:.3f}")

# Step 5: Test another case (Flu = No, COVID = Yes)
test_data = np.array([[le_flu.transform(['No'])[0], le_covid.transform(['Yes'])[0]]])  # [0, 1]
test_prediction = model.predict(test_data)
test_proba = model.predict_proba(test_data)
test_label = le_fever.inverse_transform(test_prediction)[0]

print("\nPrediction for Flu = No, COVID = Yes:")
print(f"Predicted Fever: {test_label}")
print(f"Probability of Fever = Yes: {test_proba[0][1]:.3f}")
print(f"Probability of Fever = No: {test_proba[0][0]:.3f}")

# Step 6: Visualize the probabilities for the first prediction
labels = ['Fever = No', 'Fever = Yes']
probs = [proba_no, proba_yes]
plt.bar(labels, probs, color=['#FF6384', '#36A2EB'])
plt.title('Naive Bayes: Fever Prediction Probabilities (Flu = Yes, COVID = Yes)')
plt.ylabel('Probability')
plt.xlabel('Class')
plt.ylim(0, 1)
plt.show()

```