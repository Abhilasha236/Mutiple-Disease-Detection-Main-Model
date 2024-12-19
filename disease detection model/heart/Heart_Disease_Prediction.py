# Importing the Dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

# Data Collection and Processing
# loading the csv data to a Pandas DataFrame
heart_data = pd.read_csv(r"heart/Heart_Disease_Prediction.csv")

# print first 5 rows of the dataset
print(heart_data.head())

# print last 5 rows of the dataset
print(heart_data.tail())

# print columns name
print(heart_data.columns)

# number of rows and columns in the dataset
print(heart_data.shape)

# getting some info about the data
print(heart_data.info())

# checking for missing values
print(heart_data.isnull().sum())

# statistical measures about the data
heart_data.describe()

# checking the distribution of Target Variable
heart_data['Heart Disease'].value_counts()

heart_data["Heart Disease"]= heart_data["Heart Disease"].map({"Presence":1,"Absence":0})
heart_data.head()

heart_data['Heart Disease'].value_counts()

# Splitting the Features and Target
X = heart_data.drop(columns='Heart Disease', axis=1)
Y = heart_data['Heart Disease']

print(X)

# Splitting the Data into Training data & Test Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

print(X.shape, X_train.shape, X_test.shape)

Y_test.value_counts()

# Data Scaling
from sklearn.preprocessing import StandardScaler

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler on the training data and transform both training and test data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Training

# Logistic Regression
model = LogisticRegression()
# training the LogisticRegression model with Training data
model.fit(X_train, Y_train)
Y_pred= model.predict(X_test)
print(Y_pred)

# Model Evaluation

# Accuracy Score

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy)

df = pd.DataFrame({'Actual': Y_test, 'Predicted': X_test_prediction})
print(df.head())

# Plotting the Histograms for Actual and Predicted values
df['Actual'].plot(kind='hist', bins=20, title='Actual')
plt.gca().spines[['top', 'right']].set_visible(False)
plt.show()

df['Predicted'].plot(kind='hist', bins=20, title='Predicted')
plt.gca().spines[['top', 'right']].set_visible(False)
plt.show()

# Building a Predictive System
input_data = (74,0,2,120,269,0,2,121,1,0.2,1,1,3)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = model.predict(std_data)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')
  
  
  
  
# Integration
import pickle
export_path = 'heart_disease_model.pkl'
with open(export_path, 'wb') as file:
    pickle.dump(model, file)

print(f"Model saved at {export_path}")