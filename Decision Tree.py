# Decision Tree Classifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the Iris Dataset
iris = load_iris()
X, y = iris.data, iris.target  

# Split the dataset into training and testing sets (80% Train and 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train the Model
clf.fit(X_train, y_train)

# Predict on the Test Set
y_pred = clf.predict(X_test)

# Evaluate the Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Predict for new sample
sample = [[6.0, 2.9, 4.9, 1.5]]  # Typical Iris Versicolor Measurements
prediction = clf.predict(sample)
print(f"Predicted class: {iris.target_names[prediction[0]]}")

# Visualize Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True)
plt.title("Decision Tree Visualization")  
plt.show()