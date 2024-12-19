import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

kidney_df = pd.read_csv('kidney/kidney_disease.csv')

print(kidney_df.head())
print(kidney_df.tail())
print(kidney_df.info())
print(kidney_df.isnull().sum())

#imputing null values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(kidney_df), columns=kidney_df.columns)
print(df_imputed.head())

print(df_imputed.isnull().sum())

#finding unique values in columns
for col in df_imputed.columns:
  print(f'{col}: {df_imputed[col].unique()}')
  
print(df_imputed["rc"].mode())
print(df_imputed["wc"].mode())
print(df_imputed["pcv"].mode())

df_imputed["classification"]=df_imputed["classification"].replace("ckd\t","ckd")
df_imputed["classification"]=df_imputed["classification"].replace("notckd","not ckd")

df_imputed["cad"]=df_imputed["cad"].replace("\tno","no")

df_imputed["dm"]=df_imputed["dm"].replace( "\tno","no")
df_imputed["dm"]=df_imputed["dm"].replace( "\tyes","yes")
df_imputed["dm"]=df_imputed["dm"].replace( " yes","yes")

df_imputed["wc"]=df_imputed["wc"].replace("\t6200","9800")
df_imputed["wc"]=df_imputed["wc"].replace("\t?","5.2")
df_imputed["wc"]=df_imputed["wc"].replace("\t8400","9800")

df_imputed["pcv"]=df_imputed["pcv"].replace("\t43","41")
df_imputed["pcv"]=df_imputed["pcv"].replace("\t?","41")

df_imputed["rc"]=df_imputed["rc"].replace("\t?","5.2")

#finding unique values in columns
for col in df_imputed.columns:
  print(f'{col}: {df_imputed[col].unique()}')

print(df_imputed.dtypes)
print(kidney_df.select_dtypes(exclude=["object"]).columns)

for i in kidney_df.select_dtypes(exclude=["object"]).columns:
  df_imputed[i] = df_imputed[i].astype('float')
  
print(df_imputed.dtypes)

object_dtypes = df_imputed.select_dtypes(include = 'object')
print(object_dtypes.head())

dictonary = {
        "rbc": {
        "abnormal":1,
        "normal": 0,
    },
        "pc":{
        "abnormal":1,
        "normal": 0,
    },
        "pcc":{
        "present":1,
        "notpresent":0,
    },
        "ba":{
        "notpresent":0,
        "present": 1,
    },
        "htn":{
        "yes":1,
        "no": 0,
    },
        "dm":{
        "yes":1,
        "no":0,
    },
        "cad":{
        "yes":1,
        "no": 0,
    },
        "appet":{
        "good":1,
        "poor": 0,
    },
        "pe":{
        "yes":1,
        "no":0,
    },
        "ane":{
        "yes":1,
        "no":0,
    }
}

df=df_imputed.replace(dictonary)
print(df.head())

X = df.drop(['id','classification', 'sg', 'appet', 'rc', 'pcv', 'hemo', 'sod'], axis = 1)
y = df['classification']
print(X.columns)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
print(y_test.value_counts())

from sklearn.preprocessing import StandardScaler

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler on the training data and transform both training and test data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 20)
model.fit(X_train, y_train)

y_pred= model.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
print(f"Accuracy is {round(accuracy_score(y_test, model.predict(X_test))*100, 2)}%")

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, y_train)
print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('Accuracy on Test data : ', test_data_accuracy)

df=pd.DataFrame({'Actual':y_test,'Predicted':X_test_prediction})
print(df.head())

print(X.head())
print(y.head())
print(X.tail())


# Integration
import pickle
export_path = 'kidney_disease_prediction.pkl'
with open(export_path, 'wb') as file:
    pickle.dump(model, file)

print(f"Model saved at {export_path}")

# Save the scaler to a file
scaler_path = 'kidney/scaler.pkl'
with open(scaler_path, 'wb') as file:
    pickle.dump(scaler, file)

print(f"Scaler saved at {scaler_path}")