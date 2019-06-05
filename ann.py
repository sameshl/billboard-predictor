# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('ready_for_model.csv',sep='\t')
dataset.drop_duplicates(inplace = True)

'''
X=dataset.drop(dataset.columns[0:5],axis=1)
X.drop('BillboardHit',axis=1,inplace=True)
X.drop('artist_score',axis=1,inplace=True)
y = dataset['BillboardHit']

#X.drop('BillboardHit',axis=1,inplace=True)
dataset.drop(dataset.columns[0], axis=1, inplace=True)
# Encoding categorical data
mode=pd.get_dummies(X['Mode'],drop_first=True)
key=pd.get_dummies(X['Key'],drop_first=True)
X.drop(['Mode','Key'],inplace=True,axis=1)
X=pd.concat([X,mode,key],axis=1)
'''


bill_1=dataset[dataset['BillboardHit']==1]
bill_0=dataset[dataset['BillboardHit']==0]
print((len(bill_1)/(len(bill_1)+len(bill_0)))*100,"% of values are 1")



subset=len(bill_1)//2
bill_0=bill_0.loc[:subset]
print("chat 0 : ", len(bill_0))
print("chat 1 : ", len(bill_1))




'''
bill_0=bill_0.drop(bill_0.columns[0:5],axis=1)
bill_0.drop('BillboardHit',axis=1,inplace=True)
X.drop('artist_score',axis=1,inplace=True)
y = dataset['BillboardHit']
'''


# Encoding categorical data



new_data = pd.concat([bill_0, bill_1])
X = new_data.drop('BillboardHit', axis=1)
y = new_data['BillboardHit']

X.drop(X.columns[:5],axis =1, inplace =True)

mode=pd.get_dummies(X['Mode'],drop_first=True)
key=pd.get_dummies(X['Key'],drop_first=True)
X.drop(['Mode','Key'],inplace=True,axis=1)
X=pd.concat([X,mode,key],axis=1)
#X.drop('artist_score', axis = 1, inplace = True)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras import regularizers
# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu',kernel_regularizer=regularizers.l2(0.01), input_dim = 22))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 100, nb_epoch = 1000)



# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred)

print(classification_report(y_test, y_pred))

acc = (cm[0][0] + cm[1][1])/(cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])*100
print("Accuracy is ", acc)

