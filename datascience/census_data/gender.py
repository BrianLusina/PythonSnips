import numpy as np
import pandas
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score
# from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# from sklearn.externals import joblib


col_names = ["age", " workclass", " fnlwgt", " education", " education-num", " marital-status", " occupation",
             " relationship", " race", " sex", "capital-gain", "capital-loss", "hours-per-week", "native-country",
             "income"]
with open("adult.csv", 'r') as csvfile:
    data = pandas.read_csv(csvfile, names=col_names)
print(data.shape)

Data = data.dropna(how='any', axis=0)

y = data.income
x = data.drop("income", axis=1)

print(x.head(1))
print(y.head(1))

cat_cols = x.select_dtypes(include=['object'])
num_cols = x.select_dtypes(include=['int64', 'float64'])

lb = LabelEncoder()
# en = OneHotEncoder()


for i in range(8):
    cat_cols.values[:, i] = lb.fit_transform(cat_cols.values[:, i])

print(cat_cols.head(2))

fin_data = pandas.concat([num_cols, cat_cols], axis=1)
print(fin_data.head(2))

x_train, x_test, y_train, y_test = train_test_split(fin_data.values, y, test_size=0.2, random_state=1)

clft = tree.DecisionTreeClassifier()
clft = clft.fit(x_train, y_train)
y_predict = clft.predict(x_test)
# joblib.dump(clft, 'census.pkl')
print(y_test)
print(y_predict)
print(confusion_matrix(y_test, y_predict, labels=[' >50K ', ' <=50K']))
print(accuracy_score(y_test, y_predict))

print("LEVANTO CENSUS. INPUT THE DETAILS")
test = []
enc = []
nonc = []

for i in range(0, 14):
    if i == 1:
        attr = input(col_names[i] + "(State-gov, Self-emp-not-inc, Private, Local-gov, Federal-gov): ")
        enc.append(attr)
    elif i == 3:
        attr = input(
            col_names[i] + "(Bachelors, HS-grad, Masters, 7th-8th, 9th, 11th, Some-college, Assoc-acdm, Assoc-voc): ")
    elif i == 5:
        attr = input(col_names[
                         i] + "(Never-married, Married-civ-spouse, Divorced, Married-spouse-absent, Separated, Married-AF-spouse): ")
    elif i == 6:
        attr = input(col_names[
                         i] + "(Adm-clerical, Exec-manager, Handlers-cleaners, Exec-managerial, Prof-specialty, Sales, Protective-serv, Craft-repair, Transport-moving, Farming-fishing, Machine-op-inspct, Tech-support, Other-service): ")
    elif i == 7:
        attr = input(col_names[i] + "(Not-in-family, Husband, Wife, Local-gov, Federal-gov): ")
    elif i == 8:
        attr = input(col_names[i] + "(White, Black, Asian-Pac-Islander, Amer-Indian-Eskimo): ")
    elif i == 9:
        attr = input(col_names[i] + "(Male, Female): ")
    elif i == 13:
        attr = input(col_names[i] + "(Enter your country): ")
    else:
        attr = int(input(col_names[i] + ": "))

    test.append(attr)

for i in range(13):
    if (i == 1 or i == 3 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 13):
        enc.append(test[i])
    else:
        nonc.append(test[i])

enc = lb.fit_transform(enc)

my_sample = np.concatenate([enc, nonc], axis=0)

prediction = clft.predict([my_sample])

# prediction = clft.predict([test])
print(prediction)
