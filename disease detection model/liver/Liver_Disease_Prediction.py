import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

file_path = "liver_dataset.csv"
df = pd.read_csv(file_path)

print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df['is_patient'].value_counts())

X = df.drop('is_patient', axis=1)
y = df['is_patient']

print(X)

# Training the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X.shape, X_train.shape, X_test.shape)

print(y_test.value_counts())


num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

ct = ColumnTransformer(
   [('num', num_pipeline, ['age', 'tot_bilirubin', 'direct_bilirubin', 'alkphos', 'sgpt', 'sgot', 'tot_proteins', 'albumin', 'ag_ratio']),
     ('encoder', OneHotEncoder(), ['gender'])],
    remainder='passthrough'
)
X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, y_train)
print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('Accuracy on Test data : ', test_data_accuracy)

# Integration
import pickle
export_path = 'liver_disease_prediction.pkl'
with open(export_path, 'wb') as file:
    pickle.dump(model, file)

print(f"Model saved at {export_path}")