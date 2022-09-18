from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from time import sleep

#? importing linear regression function
import sklearn.linear_model as lm

#! function to calculate r-squared, MAE, RMSE
from sklearn.metrics import r2_score , mean_absolute_error
from sklearn.metrics import mean_squared_error as mse
import warnings

warnings.filterwarnings('ignore')

def GPA():
    df = pd.read_csv('Project DATA/High School/Data/gpa_study_hours.csv')

    ax = df.plot.scatter(
        x = 'study_hours',
        y = 'gpa',
        rot = 45,
        legend = True,
    )

    ax.set_title('High School: Data', fontsize=17)
    ax.set_xlabel('Hours Studied', fontsize=14)
    ax.set_ylabel('GPA', fontsize=14)
    plt.show()

def Model():
    df = pd.read_csv('Project DATA/High School/Data/gpa_study_hours.csv')
    print("Correlation Matrix:", df.corr())

    sleep(5)
    lr = lm.LinearRegression()
    x = df.study_hours[:, np.newaxis]
    y = df.gpa
    fig = plt.gcf()

    lr.fit(x, y)

    print(lr.predict(x))

    plt.scatter(x, y, color='black')
    plt.plot(x, lr.predict(x), color='blue', linewidth = 3)
    plt.title('High School GPA VS Hours Studied', fontsize=20)
    plt.ylabel('High School GPA', fontsize=15)
    plt.xlabel('Hours Studied', fontsize=15)
    fig.canvas.set_window_title('Model')
    plt.show()

    sleep(2.5)
    print("R-Squared:", r2_score(y, lr.predict(x)))
    print("MSE:", mse(y, lr.predict(x)))
    print("MAE:", mean_absolute_error(y, lr.predict(x)))

def Pred_GPA():
    df = pd.read_csv('Project DATA/High School/Data/gpa_study_hours.csv')
    lr = lm.LinearRegression()
    x = df.study_hours[:, np.newaxis]
    y = df.gpa
    fig = plt.gcf()
    lr.fit(x, y)


    plt.plot(lr.predict(x), color='blue', linewidth = 3)
    plt.title('Predicted HS GPA VS Hours Studied', fontsize=20)
    plt.ylabel('Pred HS GPA', fontsize=15)
    plt.xlabel('Hours Studied', fontsize=15)
    fig.canvas.set_window_title('Predict HS GPA')
    plt.show()

def main():
    GPA()
    sleep(3)
    Model()
    sleep(2)
    Pred_GPA()

if __name__ == '__main__':
    main()