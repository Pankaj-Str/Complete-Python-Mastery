from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

import joblib

X , y = load_iris(return_X_y=True)

model = RandomForestClassifier()

model.fit(X, y)


# save the model to a file
joblib.dump(model, 'model.pkl')
print("Model saved to model.pkl")