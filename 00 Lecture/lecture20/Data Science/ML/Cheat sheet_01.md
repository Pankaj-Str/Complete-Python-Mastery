# Machine Learning Cheat Sheet

This cheat sheet covers key concepts, techniques, and algorithms from your list. For each, you'll find:
- **Brief Description**: What it is.
- **When to Use**: Ideal scenarios.
- **Advantages**: Pros.
- **Disadvantages**: Cons.

Organized by your sections.

## Exploratory Data Analysis (EDA)
- **Description**: Initial investigation of data to discover patterns, spot anomalies, test hypotheses, and check assumptions via summary statistics and visualizations (e.g., on Automobile Dataset).
- **When to Use**: At the start of any ML project to understand data distribution, relationships, and issues.
- **Advantages**: Helps identify data quality issues early; guides feature engineering; builds intuition.
- **Disadvantages**: Time-consuming; subjective interpretation; no direct model building.

## Handling Missing Data (Imputation Techniques)
- **Common Techniques**: Mean/median/mode imputation, KNN imputation, multiple imputation.
- **When to Use**: When dataset has missing values (common in real-world data).
- **Advantages**: Preserves sample size; simple (mean/median) or advanced (KNN) methods improve accuracy.
- **Disadvantages**: Can introduce bias (mean reduces variance); computationally expensive for advanced methods; assumes missingness mechanism.

## Outlier Detection and Handling
- **Methods**: Z-score, IQR, Isolation Forest, capping/removal/replacement.
- **When to Use**: When data has extreme values that skew models (e.g., distance-based algorithms).
- **Advantages**: Improves model robustness and performance; prevents distortion.
- **Disadvantages**: Risk of removing valid data; domain knowledge needed; can alter distribution.

## Encoding Categorical Data
- **One-Hot Encoding**: Creates binary columns for each category.
- **Label Encoding**: Assigns integers to categories.
- **When to Use**: For categorical features; one-hot for nominal, label for ordinal or tree-based models.
- **Advantages**: Makes data usable for algorithms; one-hot avoids ordinal assumption.
- **Disadvantages**: One-hot causes high dimensionality (curse of dimensionality); label implies false order.

## Data Scaling & Normalization
- **Min-Max Scaling**: Scales to [0,1].
- **Standardization (Z-score)**: Mean 0, variance 1.
- **When to Use**: Required for distance-based (KNN, SVM) or gradient descent algorithms; when features have different scales.
- **Advantages**: Improves convergence and performance; robust to outliers (robust scaling variant).
- **Disadvantages**: Changes original distribution; sensitive to outliers (Min-Max); must apply consistently to train/test.

## Feature Selection & Feature Engineering
- **Description**: Selecting relevant features or creating new ones (e.g., interactions, polynomials).
- **When to Use**: High-dimensional data; to improve interpretability and reduce overfitting.
- **Advantages**: Reduces noise/complexity; faster training; better generalization.
- **Disadvantages**: Risk of losing information; requires domain knowledge; computational cost.

## Handling Imbalanced Data
- **SMOTE**: Synthetic oversampling of minority class.
- **Undersampling/Oversampling**: Reduce majority or duplicate minority.
- **When to Use**: Classification with skewed classes (e.g., fraud detection).
- **Advantages**: Improves minority class recall; SMOTE avoids simple duplication.
- **Disadvantages**: Oversampling increases size/noise; undersampling loses data; SMOTE can create unrealistic samples.

## Supervised Learning – Regression

| Algorithm                  | When to Use                          | Advantages                                      | Disadvantages                                  |
|----------------------------|--------------------------------------|-------------------------------------------------|------------------------------------------------|
| Simple Linear Regression  | One feature, linear relationship     | Simple, interpretable, fast                     | Assumes linearity, sensitive to outliers       |
| Multiple Linear Regression| Multiple features, linear            | Interpretable coefficients                      | Multicollinearity issues, assumes linearity    |
| Polynomial Regression     | Non-linear relationships             | Captures curvature                              | High risk of overfitting with high degrees     |
| Regularization (Lasso)    | Feature selection needed, sparse     | Performs automatic feature selection            | Can be unstable with correlated features       |
| Regularization (Ridge)    | Multicollinearity present            | Handles correlated features well                 | No feature selection (shrinks but not to zero) |

- **Evaluation Metrics** (R², MSE, MAE, RMSE): Use R² for explained variance; MSE/RMSE for error magnitude (RMSE interpretable in units).

## Supervised Learning – Classification

| Algorithm             | When to Use                              | Advantages                                          | Disadvantages                                      |
|-----------------------|------------------------------------------|-----------------------------------------------------|----------------------------------------------------|
| Logistic Regression  | Binary/multiclass, interpretable needed  | Probabilistic outputs, fast, interpretable          | Assumes linearity in log-odds                      |
| K-Nearest Neighbors  | Small datasets, non-linear               | Simple, no training phase                           | Slow prediction, sensitive to scale/noise/outliers |
| Decision Trees       | Interpretable, mixed data                | Handles non-linear, easy to visualize, pruning helps| Prone to overfitting without pruning               |
| Random Forest        | General purpose, robust                  | Reduces overfitting, feature importance              | Less interpretable, slower                         |
| Support Vector Machine| Clear margins, high-dimensional          | Effective in high dimensions, robust                | Slow on large data, sensitive to parameters        |

- **Metrics**: Accuracy (overall); Precision/Recall/F1 (imbalanced); Confusion Matrix/ROC-AUC (threshold-independent).

## Ensemble Learning & Advanced

| Method                | When to Use                          | Advantages                                      | Disadvantages                              |
|-----------------------|--------------------------------------|-------------------------------------------------|--------------------------------------------|
| Bagging (e.g., Random Forest) | Reduce variance                     | Parallel, robust to overfitting                 | More memory, less interpretable            |
| Boosting (AdaBoost, Gradient Boosting, XGBoost) | High accuracy needed               | Sequential error correction, very accurate      | Sensitive to outliers, slower, overfitting risk |

- XGBoost: Fast, handles missing data, regularization built-in.

## Unsupervised Learning

| Algorithm                  | When to Use                          | Advantages                                      | Disadvantages                                  |
|----------------------------|--------------------------------------|-------------------------------------------------|------------------------------------------------|
| K-Means Clustering        | Spherical clusters, known K          | Fast, scalable                                  | Sensitive to K/initialization/outliers         |
| Hierarchical Clustering   | Dendrogram needed, no K              | No need for K, visual hierarchy                 | Computationally expensive (O(n²))               |
| DBSCAN                    | Arbitrary shapes, noise               | Handles outliers, no K needed                   | Sensitive to parameters (eps, min_samples)     |
| Principal Component Analysis (PCA) | Dimensionality reduction            | Reduces features while retaining variance       | Loses interpretability, assumes linearity      |

## Model Optimization

- **Cross-Validation**: Split data (e.g., k-fold) to estimate performance.
  - When: Limited data, avoid overfitting.
  - Adv: Reliable estimate; Disadv: Computationally expensive.

- **Hyperparameter Tuning**:
  - **GridSearchCV**: Exhaustive search.
    - Adv: Thorough; Disadv: Very slow for large spaces.
  - **RandomizedSearchCV**: Samples randomly.
    - Adv: Faster, good for large spaces; Disadv: May miss optimal.

- **Bias–Variance Tradeoff**: High bias (underfit), high variance (overfit). Regularization/ensembles balance it.

## Model Deployment Basics
- **Streamlit**: Python library for quick web apps.
- **When to Use**: Prototype ML predictions in interactive apps.
- **Advantages**: Simple, fast deployment; integrates plots/models.
- **Disadvantages**: Not for production-scale; limited customization.

