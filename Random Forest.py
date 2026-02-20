# Random Forest 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#Load the Iris Dataset
iris = load_iris()
X, y = iris.data, iris.target 

# Split the dataset into training and testing sets (80% Train and 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Create a Random Forest Classifier
rf_clf = RandomForestClassifier(n_estimators = 100, max_depth = 4, random_state = 42)

#Training the model
rf_clf.fit(X_train, y_train)

# Predict on the Test Set
y_pred = rf_clf.predict(X_test)

#Evaluate the Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Predict for new sample
sample = [[6.0, 2.9, 4.9, 1.5]]  # Typical Iris Versicolor Measurements
prediction =rf_clf.predict(sample)
print(f"Predicted class: {iris.target_names[prediction[0]]}")

#Feature Importance Visualization 
importances = rf_clf.feature_importances_
feature = iris.feature_names
plt.figure(figsize=(8,6))
plt.barh(feature, importances, color='skyblue')
plt.xlabel("Feature Importance")
plt.title("Random Forest Feature Importance")
plt.show()
print(y_test)
print(y_pred)