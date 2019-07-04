import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
pd.set_option('display.max_columns', None)

### pokemon generation 1-6 ####
df = pd.read_csv('pokemon.csv')

### pokemon generation 7 ####
df2 = pd.read_csv('gen7.csv')
df3 = pd.read_csv('gen7.csv')


### looking at the legendary pokemon ###
#print(df[df['Legendary'] == True])

df.drop(['#', 'Generation','Type 1', 'Type 2'], 1, inplace=True)
df2.drop(['#', 'Generation', 'Type 1', 'Type 2'], 1, inplace=True)


### Getting rid of the mega evolutions and other buffs some pokemon get ###
df = df[df.Name.str.contains("Black") == False]
df = df[df.Name.str.contains("White") == False]
df = df[df.Name.str.contains("Mega") == False]
df = df[df.Name.str.contains("Primal") == False]
df = df[df.Name.str.contains("%") == False]
df = df[df.Name.str.contains("Forme") == False]
df = df[df.Name.str.contains("Confined") == False]


### getting rid of the names of each pokemon ###
df.drop(['Name'], 1, inplace=True)
df2.drop(['Name'], 1, inplace=True)
#print("df2 head")
#print(df2.head())

#print("df2 columns")
#print(df2.columns)


### just the pokemon's values without knowing whether or not they are legendary ###
X = np.array(df.drop(['Legendary'], 1))
### just whether or not each pokemon is legendary or not
y = np.array(df['Legendary'])


### just the pokemon's values without knowing whether or not they are legendary Gen 7###
X1 = np.array(df2.drop(['Legendary'], 1))
### just whether or not each pokemon is legendary or not Gen 7 ###
y1 = np.array(df2['Legendary'])


### seperating the gen 1-6 data into training and testing sets ###
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)
### using a classification ###
clf = neighbors.KNeighborsClassifier()
### fitting the data ###
clf.fit(X_train, y_train)

### seeing how accurate it is ###
accuracy = clf.score(X_test, y_test)
print("accuracy is:")
print(accuracy)



example_measures = np.array(X1)
example_measures = example_measures.reshape(len(example_measures), -1)

### using the data from generation 1-6 to predict which pokemon are legendary in generation 7 ###
prediction = clf.predict(example_measures)
print("The amount of pokemon predicted to be legendary are:")
print(prediction.sum())
guess = df3[prediction]
print("Table of pokemon predicted to be legendary are:") 
print(guess[['#', 'Generation','Name','Type 1', 'Type 2','Total','Legendary']])
dfTrue = df3[df3['Legendary'] == True]
print('pokemon that are actually legendary:')
print(dfTrue[['#', 'Generation','Name','Type 1', 'Type 2','Total','Legendary']])


### quite often when running this the "Tapu" fairy over watches of each island would be left out so i just wanted to look at their stats ###
df3.drop(['#', 'Generation','Legendary', 'Type 2', 'Type 1'], 1, inplace=True)
print(df3[df3['Name'].str.contains('Tapu')])





