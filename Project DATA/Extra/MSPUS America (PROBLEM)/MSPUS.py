from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from time import sleep
import datetime as dt

#? importing linear regression function
import sklearn.linear_model as lm

#! function to calculate r-squared, MAE, RMSE
from sklearn.metrics import r2_score , mean_absolute_error
from sklearn.metrics import mean_squared_error as mse
import warnings
from datetime import datetime
import financialanalysis as fa

warnings.filterwarnings('ignore')

def Graph():
    df = pd.read_csv('Project DATA/Extra/MSPUS America/Data/MSPUS.csv')

    x = df['Date'].head()
    y = df['MSPUS'].head()
    fig = plt.gcf()

    plt.plot(x, y, color='blue', linewidth = 3, marker='o')
    plt.title('MSPUS Data', fontsize=20)
    plt.ylabel('MSPUS', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.grid(linestyle = '--')
    fig.canvas.set_window_title('Date (Small parts)')
    plt.show()

def Model():
    df = pd.read_csv('Project DATA/Extra/MSPUS America/Data/MSPUS.csv', 
    index_col='Date', parse_dates=['Date'])

    print(df.head())
    df['Time'] = np.arange(len(df.index))
    print(df.head())

    # print("Correlation Matrix:", df.corr())

    sleep(5)
    lr = lm.LinearRegression()

    x = df.loc[:, ['Time']]  # features
    y = df.loc[:, 'MSPUS']  # target

    # print(X)
    # print(Y)

    # x = df.Date[:, np.newaxis]
    # y = df.MSPUS
    fig = plt.gcf()

    lr.fit(x, y)

    print(lr.predict(x))

    plt.plot(x, y, color='black')
    plt.plot(x, lr.predict(x), color='blue', linewidth = 3, marker='o')
    plt.title('MSPUS VS Date', fontsize=20)
    plt.ylabel('MSPUS', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    fig.canvas.set_window_title('Model')
    plt.show()

    sleep(2.5)
    print("R-Squared:", r2_score(y, lr.predict(x)))
    print("MSE:", mse(y, lr.predict(x)))
    print("MAE:", mean_absolute_error(y, lr.predict(x)))

def main():
    # Graph()
    Model()

if __name__ == '__main__':
    main()