import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

x= np.array([-2,-1.64,-0.7,0,0.45,1.2,1.64,2.32,2.9])
y = np.array([1.0, 1.5, 2.4, 2, 1.49, 1.2, 1.3, 1.2, 0.5])

def func(x, p1,p2):
    return p1*np.sin(p2*x) + p2*np.cos(p1*x)

popt, pcov = curve_fit(func, x, y,p0=(1.0,0.2))
p1 = popt[0]
p2 = popt[1]

residuals = y - func(x,p1,p2)
fres = sum(residuals**2)

curvex=np.linspace(-2,3,100)
curvey=func(curvex,p1,p2)

plt.plot(x, y, 'bo ')
plt.plot(curvex, curvey,'r')
plt.title('Non-linear fitting')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(['data','fit'],loc='best')
plt.grid(linestyle = '--')
plt.show()