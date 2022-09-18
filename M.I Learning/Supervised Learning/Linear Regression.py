import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# importing linear regression function
import sklearn.linear_model as lm

# function to calculate r-squared, MAE, RMSE
from sklearn.metrics import r2_score , mean_absolute_error, mean_squared_error

df = pd.read_csv('M.I Learning/Supervised Learning/Data/Grade_Set.csv')
lr = lm.LinearRegression()

x = df.Hours_Studied[:, np.newaxis]
y = df.Test_Grade.values

lr.fit(x, y)
print("Intercept:", lr.intercept_)
print("Coefficient:", lr.coef_)
print("Prediction (Math):", 52.2928994083 + 4.74260355*6)
# print("Prediction Function:", lr.predict(6)) #! Problem

plt.scatter(x, y, color='black')
plt.plot(x, lr.predict(x), color='blue', linewidth = 3)
plt.title('Grade VS Hours Studied')
plt.ylabel('Test_Grade')
plt.xlabel('Hours_Studied')
plt.show()


