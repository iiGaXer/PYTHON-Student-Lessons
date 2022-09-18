import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load data
df = pd.read_csv('M.I Learning/Supervised Learning/Data/Grade_Set.csv')
print(df)

# Simple scatter plot
df.plot(kind='scatter', x='Hours_Studied', y='Test_Grade', title='Grade vs Hours Studied')
print(df.corr())
plt.show()