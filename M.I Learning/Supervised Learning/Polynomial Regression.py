import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# importing linear regression function
import sklearn.linear_model as lm

# function to calculate r-squared, MAE, RMSE
from sklearn.metrics import r2_score , mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('M.I Learning/Supervised Learning/Data/Grade_Set_2.csv')
print("Correlation Matrix:", df.corr())

lr = lm.LinearRegression()
x = df.Hours_Studied[:, np.newaxis]
y = df.Test_Grade

lr.fit(x, y)

plt.scatter(x, y, color='black')
plt.plot(x, lr.predict(x), color='blue', linewidth = 3)
plt.title('Grade VS Hours Studied')
plt.ylabel('Test_Grade')
plt.xlabel('Hours_Studied')
plt.show()
print("R-Squared:", r2_score(y, lr.predict(x)))