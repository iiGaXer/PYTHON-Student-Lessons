# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
# from datetime import datetime
from sklearn.metrics import r2_score , mean_absolute_error, mean_squared_error, accuracy_score 
from sklearn import preprocessing
import requests
from bs4 import BeautifulSoup
import sklearn.linear_model as lm
from os import system
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import random
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

def Train(lr, train_x, train_y, test_y, x, y, y_pred):    
    memory = []
    # num = 0.2
    train = False
    
    while train != True:
        num = random.uniform(0.3, 0.5)
        for i in range(5):
            memory.append(r2_score(test_y, y_pred))
            if r2_score(test_y, y_pred) >= 1 - .05 or memory[-1] >= 1 - .05:
                train = True
                print("R-Squared:", r2_score(test_y, y_pred))
                break
            else:
                train_x, x_test, train_y, y_test = train_test_split(x, y, test_size = num)

                lr.fit(train_x, train_y)
                
                if r2_score(test_y, y_pred) < 0.75:
                    memory.remove(memory[0])
                    pass
                else:
                    memory.append(r2_score(test_y, y_pred))
                    memory.sort()

def sigmoid(x, Beta_1, Beta_2):
    '''NON-linear regression method'''
    y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
    return y

def Visualization():
    '''Visualisation of Data'''
    # fig, ax = plt.subplots()

    site = 'https://www.agentinottawa.com/stats/'
    request = requests.get(site)
    html_data = request.text

    soup = BeautifulSoup(html_data, 'lxml')
    data = soup.find_all('div', class_ = 'user-content clearfix')

    x = []
    y = []
    memory = []

    for subdata in data:
        section = subdata.find('div', class_ = '')
        part = section.find('table')
        part_2 = part.find('tbody')
        part_3 = part_2.find_all('tr')

        for parts in part_3:
            i = (len(parts) - (len(parts) + 1)) + 1
            scrapped = parts.find('td', style="text-align: center; width: 111.2px;").text.replace('', '')
            if scrapped == '\xa0':
                y.append('0%')
            else:
                # print(f'''\nData: {scrapped}''')
                y.append(scrapped)

        sleep(5)
        system("cls")

        for parts in part_3:
            scrapped = parts.find('td', style="text-align: center; width: 106.4px;").text.replace('', '')
            x.append(scrapped)
            # print(f'''\nMonth: {scrapped}''')

    try:
        xtitle = x[0]
        ytitle = float(y[0].replace("%", ""))/100
        ytitle = y[0]

        xtitle = 'Months'
        ytitle = 'Month Changes'

    except:
        xtitle = x[0]
        ytitle = y[0]
        
        x.remove(x[0])
        y.remove(y[0])


    sleep(5)
    system("cls")

    for i in range(len(y)):
        y[i] = y[i].replace("%", "")
        y[i] = float(y[i])

    count = len(x)

    for i in range(len(x)):
        a = x[i]
        if len(a) != 3:
            a = a[:3]
            x[i] = a
        else: 
            pass

    for i in range(len(x)):
        for j in range(count):
            j += i + 1
            if j + 1 > len(x):
                break
            elif x[i] in x[j]:
                memory.append(x[i] + '\n2022')
                x[j] = memory[i]
            else:
                pass

        count -= 1

    sleep(2.5)

    print(x, f"\n")
    print(y)

    # plt.figure(figsize=(8, 6))
    plt.figure("Data Plotted", figsize=(8, 6))
    plt.plot(x, y)
    plt.title("Canadian Market Percent Increase")
    plt.xlabel(xtitle, fontsize=14)
    plt.ylabel(ytitle, fontsize=14)
    plt.grid(linestyle = '--')
    plt.show()

    # Model(x, y, xtitle, ytitle)
    # Model_2(x, y, xtitle, ytitle)
    # Model_3(x, y, xtitle, ytitle)
    Model_4(x, y, xtitle, ytitle)

def Model(x, y, title_x, title_y):
    '''Model 1: Linear Regression method with fitting and predicting test Xs and Ys'''
    x1 = x
    for i in range(len(x1)):
        x1[i] = i

    x1 = np.array(x1)
    y1 = y

    x1.reshape(1, -1)
    x1 = x1[:, np.newaxis]

    x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size = 0.2)

    lr = lm.LinearRegression()

    lr.fit(x_train, y_train)

    plt.figure("Model 2", figsize=(8, 6))
    plt.scatter(x1, y1, color='black')
    plt.scatter(x_test, lr.predict(x_test), color='red')
    plt.plot(x1, lr.predict(x1), color='blue', linewidth = 2)
    plt.title('Canadian Market Percent Increase: Prediction')
    plt.grid(linestyle = '--')
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.show()

def Model_2(x, y, title_x, title_y):
    '''Broken Model: Linear regression with training loop method'''
    
    x1 = x
    num = 0
    for i in range(len(x1)):
        if '2022' in x1[i]:
            x1[i] = num + 1
            num += 1
        else:    
            x1[i] = i + 1

    x1 = np.array(x1)
    y1 = y

    x1.reshape(1, -1)
    x1 = x1[:, np.newaxis]
    lr = lm.LinearRegression()
    x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size = .34)
    
    lr.fit(x_train, y_train)
    memory = []
    # num = 0.2
    train = False

    # while r2_score(y, lr.predict(x1)) <= 1 - 0.19:
    while train != True:
        for i in range(10):
            num = random.uniform(0.1, 0.51)
            memory.append(r2_score(y_train, lr.predict(x_train)))
            if r2_score(y_train, lr.predict(x_train)) >= 1 - .11 or memory[-1] >= 1 - .11:
                train = True
                print("R-Squared:", r2_score(y_train, lr.predict(x_train)))
                break
            else:
                x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size = num)

                lr.fit(x_train, y_train)
                memory.append(r2_score(y_train, lr.predict(x_train)))
                memory.sort()

        # if memory[0] > r2_score(y_train, lr.predict(x_train)):
        #     num -= .1 
        # elif num >= 0.899999:
        #     num -= .1
        # elif num <= 0:
        #     num += .1
        # else:
        #     num += .1

    # x1 = x[:, np.newaxis]

    print(x_test)
    print(y_test)
    print(lr.predict(x_test))
    print(lr.predict(x_train))

    plt.figure("Model 2", figsize=(8, 6))
    plt.scatter(x_test, y_test, color='black')
    plt.plot(x_test, lr.predict(x_test), color='blue', linewidth = 2)

    # plt.scatter(x1, y1, color='red')
    # plt.plot(x1, lr.predict(x1), color='orange', linewidth = 2)
    plt.title('Canadian Market Percent Increase: Prediction')
    plt.grid(linestyle = '--')
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.show()

def Model_3(x, y, title_x, title_y):
    '''Model 2: Testing Logistic Regression and predicting (training rlly) X and Y.'''
    x1 = x
    num = 0
    for i in range(len(x1)):
        # if '2022' in x1[i]:
        #     x1[i] = num + 1
        #     num += 1
        # else:    
        x1[i] = i + 1

    x1 = np.array(x1)
    y1 = y

    x1.reshape(1, -1)
    x1 = x1[:, np.newaxis]
    x1 = StandardScaler().fit_transform(x1)
    lr = lm.LogisticRegression(C=100)
    # lr = lm.LinearRegression()

    lab = preprocessing.LabelEncoder()
    y1 = lab.fit_transform(y1)
    # x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size = .25)

    lr.fit(x1, y1)
    y_pred = lr.predict(x1)

    print ("Accuracy : ", accuracy_score(y1, y_pred))
    # Train(lr, x_train, y_train, x1, y1)

    plt.figure("Model 3", figsize=(8, 6))
    plt.scatter(x1, y1, color='black')
    plt.plot(x1, lr.predict(x1), color='blue', linewidth = 2)

    # plt.scatter(x_test, y_test, color='gray')
    # plt.plot(x_test, lr.predict(x_test), color='blue', linewidth = 2)

    # plt.scatter(x_train, y_train, color='red')
    # plt.plot(x_train, lr.predict(x_train), color='orange', linewidth = 2)

    plt.title('Canadian Market Percent Increase: Prediction')
    plt.grid(linestyle = '--')
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.autoscale()
    plt.show()

def Model_4(x, y, title_x, title_y):
    x1 = x
    num = 0
    for i in range(len(x1)):
        # if '2022' in x1[i]:
        #     x1[i] = num + 1
        #     num += 1
        # else:    
        x1[i] = i + 1

    x1 = np.array(x1)
    y1 = y

    x1.reshape(1, -1)
    x1 = x1[:, np.newaxis]
    x1 = StandardScaler().fit_transform(x1)
    # lr = lm.LogisticRegression(C=100)
    lr = lm.LinearRegression()
    # lr = np.poly1d()
    deg = 2
    lr = make_pipeline(PolynomialFeatures(deg), lr)

    # lab = preprocessing.LabelEncoder()
    # y1 = lab.fit_transform(y1)
    x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size = .25)
    
    # lr.polyfit(x_train, y_train, 3)
    lr.fit(x_train, y_train)
    y_pred = lr.predict(x_test)
    
    Train(lr, x_train, y_train, y_test, x1, y1, y_pred)
    print("R-squared : ", r2_score(y_test, y_pred))

    plt.figure("Model 3", figsize=(8, 6))
    # plt.scatter(x1, y1, color='black')
    # plt.plot(x1, lr.predict(x1), color='blue', linewidth = 2)

    plt.scatter(x_test, y_test, color='gray')
    plt.plot(x_test, lr.predict(x_test), color='blue', linewidth = 2)

    # plt.scatter(x_train, y_train, color='red')
    # plt.plot(x_train, lr.predict(x_train), color='orange', linewidth = 2)

    plt.title('Canadian Market Percent Increase: Prediction')
    plt.grid(linestyle = '--')
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.autoscale()
    plt.show()

def main():
    Visualization()

if __name__ == '__main__':
    main()
    