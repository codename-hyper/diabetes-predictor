import pandas as pd
import pickle

data = pd.read_csv('diabetes.csv')

for col in data.columns:
    if col != 'Outcome':
        data[col] = data[col].replace(0, data[col].median())

x = data
y = data.pop('Outcome')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=1)

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
score = accuracy_score(y_test, y_pred=y_pred)
f1 = f1_score(y_test, y_pred)

pickle.dump(model, open('diabetes.pkl', 'wb'))

model = pickle.load(open('diabetes.pkl', 'rb'))
