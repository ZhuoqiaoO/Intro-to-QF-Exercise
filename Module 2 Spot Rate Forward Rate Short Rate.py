import math
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

"""
Question 1: Take the yield curve {y_1,y_2,y_3} shown below and bootstrap 
the annual spot rates {s_1,...,s_5}. Use interpolation to estimate the 
missing yields you need to compute the spot curve.

Using the spot rate curve, compute the short rates {r_1,...,r_5}.

Compute the forward rate f_(2,5). 
"""
x = np.array([1, 3, 5])
y = np.array([0.0249, 0.0273, 0.0281])
spline = CubicSpline(x, y)
x_new = np.linspace(0, 5, 100)
y_new = spline(x_new)
plt.plot(x_new, y_new, label='Cubic Spline')
yield_rate = [spline(i) for i in range(1,6)]
s=1
f=1
spot = [spline(1)]
for i in range(2,6):
    c = spline(i)
    summ = sum(c/(1+spot[j])**j for j in range(len(spot)))
    spot.append(((c+1)/(1-summ))**(1/i)-1)
print("The spot rates are:",[float(x) for x in spot])

short = [spot[0]]
for i in range(1,5):
    rproduct = math.prod([1+short[j] for j in range(len(short))])
    r = (1+spot[i])**(i+1)/rproduct - 1
    short.append(r)
print("The short rates are:",[float(x) for x in short])

f_25 = ((1+spot[4])**5/(1+spot[1])**2)**(1/3)-1
print("The forward rate f_(2,5) is:", f_25)

"""
Question 2: The TUV corporation has just paid a dividend and its 
next dividend is estimated to be $1.4 million. It has a total 
market capitalization of $35,000,000. The growth rate for this 
type of company is 10%. What is the implied discount rate for the 
dividends of this stock?
"""
g =0.1
d1 = 1.4*10**6
s0 = 3.5*10**7
r = d1/s0+g
print("The implied discount rate is:", r)

