import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from time import sleep

# importing linear regression function
import sklearn.linear_model as lm

# function to calculate r-squared, MAE, RMSE
from sklearn.metrics import r2_score , mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings('ignore')

def Thousand(x, pos):
    return '{:,.0f}'.format(x/1000)

df = pd.read_csv("Project Data/COVID-19; Canada/COVID-19 Training/US COVID-19.csv")
lr = lm.LinearRegression()
x = df.Date[:, np.newaxis]
y = df.Dose

lr.fit(x, y)

print(df)
sleep(2.5)
print("R-Squared:", r2_score(y, lr.predict(x)))
sleep(2.5)
print(df.corr)

ax = df.plot.line(
    x = 'Date',
    y = 'Dose',
    rot = 45,
    legend = False,
)

ax.set_title('COVID-19 Data', fontsize = 20)
ax.set_xlabel('Date', fontsize = 15)
#! Daily Count People Receiving Dose 1
ax.set_ylabel('Vaccinated: Dose 1', fontsize = 15)
ax.yaxis.set_major_formatter(Thousand)
plt.show()

