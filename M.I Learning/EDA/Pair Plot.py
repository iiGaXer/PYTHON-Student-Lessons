from gettext import npgettext
from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm #! TanH() Function
from time import sleep
import Univariate_Analysis

Corr = Univariate_Analysis.iris.corr()
print(Corr)

sm.graphics.plot_corr(Corr, xnames = list(Corr.columns))
plt.show()