import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

def Visualization():
    df = pd.read_csv('Project DATA/Video Game Sales/Data/vgsales.csv')
    print(df)

    fig = plt.gcf()
    X = df.Name
    Y = df.Global_Sales

    X = X.head()
    Y = Y.head()

    plt.bar(X, Y)
    plt.title('Video Game Sales: Data', fontsize=17)
    plt.xlabel('Ranking', fontsize=14)
    plt.ylabel('Global Sales', fontsize=14)
    fig.canvas.set_window_title('Data')
    plt.grid(linestyle = '-')
    plt.gca().set_aspect('auto')
    plt.show()

def main():
    Visualization()

if __name__ == '__main__':
    main()