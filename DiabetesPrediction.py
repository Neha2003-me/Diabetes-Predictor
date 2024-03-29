

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis"""

#loading the diabetes dataset
diabetes=pd.read_csv('diabetes.csv')

#printing the first five rows
diabetes.head()

#printing the number of rows and columns
diabetes.shape

#Statistics of data
diabetes.describe()

diabetes['Outcome'].value_counts()

"""0: The person is non-diabetic ; 1: The person is diabetic """

diabetes.groupby('Outcome').mean()

#separating the data and labels
X=diabetes.drop(columns='Outcome',axis=1)
Y=diabetes['Outcome']

"""Data Standardization"""

scale=StandardScaler()

scale.fit(X)

standard_data=scale.transform(X)

X=standard_data

"""Train-test Split"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=1)

"""Training the model:"""

classifier=svm.SVC(kernel='linear')

"""Training the support vector machine classifier"""

classifier.fit(X_train,Y_train)

"""Model evaluation"""

#training data accuracy score
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)
print(training_data_accuracy)

#test data accuracy score
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)
print(test_data_accuracy)

"""Making a predictive system"""

input_data=(4,300,100,35,50,32.5,0.5,60)
#changing the input data to numpy array
num_input=np.asarray(input_data)
#reshape the array as we are predicting only for one instance
input_data_reshaped=num_input.reshape(1,-1)
#standardize the input data
std_data=scale.transform(input_data_reshaped)
#print(std_data)


prediction=classifier.predict(std_data)

"""Final prediction:"""

if(prediction[0]==0):
  print("The person is not diabetic.")
else:
  print("The person is diabetic. ")
