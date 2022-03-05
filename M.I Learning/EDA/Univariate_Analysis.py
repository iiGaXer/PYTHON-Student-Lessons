from gettext import npgettext
from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm #! TanH Function
from time import sleep

iris = datasets.load_iris()
iris = pd.DataFrame(data = np.c_[iris['data'], iris['target']], 
    columns = iris['feature_names'] + ['species'])

iris.species = np.where(iris.species == 0.0, 'Setosa', np.where(
    iris.species == 1.0, 'Versicolor', 'Virginica'))

iris.columns = iris.columns.str.replace(' ', '')
iris.describe()

print(iris)
sleep(4)
print(iris['species'].value_counts())
