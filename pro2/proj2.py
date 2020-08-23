##############################################################################
# Proj2.py
# EEE 591: Python for Engineer
# 
# ********************
# Use Princeple component analysis to do the data analysis 
# and use Multi-layer Perceptron classifier to do the training
# ********************
##############################################################################

import numpy as np                                     # needed numpy to create array
import pandas as pd                                    # needed pandas to create dataframe
import matplotlib.pyplot as plt                        # modifying plot

from sklearn.neural_network import MLPClassifier       # needed as ML algrithom 
from sklearn.model_selection import train_test_split   # splits database
from sklearn.preprocessing import StandardScaler       # scaling data
from sklearn.decomposition import PCA                  # needed to run Princeple component analysis
from sklearn.metrics import confusion_matrix           # needed to built confusion matrix

from warnings import filterwarnings                    # needed to ignore warnings
filterwarnings("ignore")                               # we finally can ignore those warnings

#import data
sonar = pd.read_csv('sonar_all_data_2.csv', header=None, usecols=range(61)) #ignore last column in data, same info is kept in column 61
sonar = sonar.to_numpy()             # convert the import data as numpy array

#sonar columns 0 through 59 are the features column 
X = sonar[:,0:60]                    # get the features from : row and 0-59 col
y = sonar[:,60]                      # get the classifications from : row and 60 col

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0) #split data 70/30

stdsc = StandardScaler()                    # apply standardization
X_train_std = stdsc.fit_transform(X_train)  # standarized training data
X_test_std = stdsc.transform(X_test)        # standarized test data

scores = []  # create a list to hold the test accuacy 
cmat = [] # create a list to hold the output confusion matrices

for i in range(1,61):
    
    #perform PCA 
    pca = PCA(n_components=i)                    # use i number of features (>= 1)
    X_train_pca = pca.fit_transform(X_train_std) # apply PCA fit to train data
    X_test_pca = pca.transform(X_test_std)       # apply PCA fit to test data
    
    # now we use Multi-layer Perceptron classifier to do the training.
    mlp = MLPClassifier( hidden_layer_sizes=(100), activation='logistic',
                        max_iter=2000, alpha=0.00001, solver='adam', tol=0.0001, random_state=5 )
    
    mlp.fit(X_train_pca,y_train)                    # now use Multi-layer Perceptron classifier to fit our training data
    
    accuracy= mlp.score(X_test_pca, y_test)         # get the accuracy from the test dataset
    print("Number of components #: %d. test accuracy: %f" %(i ,accuracy)) # print the features that used, and the accuacy
    scores.append(accuracy)                         # append the accuarcy to the list and store it

    y_pred = mlp.predict(X_test_pca)                # see how we do on the test data
    cmat.append (confusion_matrix(y_test,y_pred))   # append the confusion matrix to the list

    
maxeleinlist = scores.index(max(scores))       # now get the index from the list that has max accuarcy
maxinlist = scores[maxeleinlist]               # get the value of max accuarcy from the index that we get from previous line

# print the maximum index+1 and its max accuarcy
print("The maximum is at position %d, the test accuracy is %.6f" % (maxeleinlist + 1, maxinlist))

# print which confusion matrix we need to get from
print('The Confusion Matrix for Number of components #: %d is'  % (maxeleinlist+1))
print(cmat[maxeleinlist])    #print the confusion matrix that has highest accuarcy

plt.title('Number of components vs. Accuracy')  # create plot title
plt.xlabel('Number of components')              # create x axis label
plt.ylabel('Accuarcy that Achieved')          # create y axis label
plt.plot(range(60),scores)                    # plot the accuarcy vs # features
plt.show()                                    # now show it