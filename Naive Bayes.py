# Naive Byes Algorithm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Load the iris dataset

iris= load_iris()
X,y= iris.data,iris.target #features and target labels

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=42)

# Create Gaussian Naive Bayes Classifier

gnb=GaussianNB()

#Train the Model

gnb.fit(X_train,y_train)

#predict on the test set 

y_pred = gnb.predict(X_test)

#Evaluate the Accuracy

accuracy = accuracy_score(y_test, y_pred)

print (f"Accuracy : {accuracy:.2f}")

#predic for a new sample

sample = [[2.1,1.3,1.4,0.2]] #Example Input

prediction = gnb.predict(sample)

print (f"Predicted.class:{iris.target_names[prediction[0]]}")

#preduict for a  new sample likely to be 'versicolor'

sample2 = [[6.0,2.9,4.5,1.5]] # Typical Iris Versicolor

prediction = gnb.predict(sample2)

print(f"Predicted Class:{iris.target_names[prediction[0]]}")