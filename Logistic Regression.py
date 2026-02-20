"""
LOGISTIC REGRESSION
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Data
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([0,0,0,0,0,0,1,1,1,1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# Prediction for 4.5 hours
study_hours = np.array([[4.5]])
proba = model.predict_proba(study_hours)[0][1]
prediction = model.predict(study_hours)[0]

print(f"Probability of passing with 4.5 hours: {proba:.2f}")
print(f"Predicted Class: {'Pass' if prediction == 1 else 'Fail'}")

# Test range for curve
X_test = np.linspace(0, 11, 100).reshape(-1, 1)
probs = model.predict_proba(X_test)[:, 1]

# Plot
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X_test, probs, color='blue', label='Sigmoid Curve')
plt.axvline(4.5, color='gray', linestyle='--', label='4.5 Hours')
plt.axhline(0.5, color='gray', linestyle='-_', label='Decision Threshold (0.5)')

plt.xlabel('Study Hours')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression: Probability of Passing vs Study Hours')
plt.legend()
plt.show()