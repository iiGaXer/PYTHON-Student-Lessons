import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from time import sleep
import datetime as dt
from datetime import timezone
import requests
import json

#? importing linear regression function
import sklearn.linear_model as lm

#! function to calculate r-squared, MAE, RMSE
from sklearn.metrics import r2_score , mean_absolute_error
from sklearn.metrics import mean_squared_error as mse
import warnings
from datetime import datetime
import financialanalysis as fa
from os import system

warnings.filterwarnings('ignore')

system("cls")

def US():
    url = 'https://data.cdc.gov/resource/9mfq-cb36.json'
    response = requests.get(url)

    json_string = response.text

    data = json.loads(json_string)

    #* for subdata in data:
    #?    for key in subdata:
    #!         print(key, ":", subdata[key])

    df = pd.read_json(json.dumps(data))
    print(df)

    x = df['submission_date'].head()
    y = df['new_case'].head()
    fig = plt.gcf()

    # for i in range(len(x)):
    #     x[i] = str(x[i])

    # x.strftime('%Y-%m-%d %H:%M:%S')
    # x = df['submission_date']

    # with open("COVID US.txt", "w") as w_file:
    #     w_file.write(df)

    print(x)

    plt.plot(x, y, color='black')
    plt.title('COVID 19: US', fontsize=20)
    plt.ylabel('New Cases', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    fig.canvas.set_window_title('Data')
    plt.show()

def main():
    US()

if __name__ == '__main__':
    main()