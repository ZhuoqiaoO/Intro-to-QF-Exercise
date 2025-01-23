from sympy import symbols, Eq, solve
from scipy.optimize import root_scalar

"""
Question 1: Meg has the opportunity to purchase bond A at origination 
for $98,930. The bond's term is 10 years and pays semi-annual interest 
based on a nominal rate of 3.5%. She needs to invest the money for 5 
years after which she wants to sell the bonds and put the funds towards 
the purchase of a house. She chose a 10-year bond to secure a higher 
interest rate.

What is bond A's yield?

Another bond B is offered for sale with the same characteristics 
except the coupon rate is 3.75%. How would the market price bond B?

Meg is concerned that yields are at all time lows and is concerned 
that they will rise in the future. If the long term average yield 
for 5-year bonds is 4.75%, then how would the prices of bonds A and 
B be affected when Meg is ready to sell them?
"""
s = 98930
r = 0.035
k =2
n =10
f = 100000
c = f*r/k
def bond_ytm(price, face_value, coupon, periods):
    def equation(y):
        return sum(coupon / (1 + y)**t for t in range(1, periods + 1)) + face_value / (1 + y)**periods - price
    result = root_scalar(equation, bracket=[1e-8, 0.1], method='brentq')
    return result.root
print("Bond A's yield to maturity:", bond_ytm(s, f, c, n*k)*k)

y = bond_ytm(s, f, c, n*k)*k
c = f* 0.0375 / k
sb = sum(c*(1+y/k)**(-i) for i in range(1,n*k+1)) + f*(1+y/k)**(-n*k)
print("Market price of bond B:", sb)

s_5yr = sum(c*(1+0.0475/k)**(-i) for i in range(1,5*k+1)) + f*(1+0.0475/k)**(-5*k)
print("Price of bond A after 5 years:", s_5yr-sb)

"""
Question 2: A newly issued $10,000 bond with a ten-year term has a 4% 
coupon rate and pays semi-annually. The current market yield for a ten-year 
bond of this type is 3.7%. What is the current market price of the bond?
"""
f = 10000
r = 0.04
k = 2
y = 0.037
n = 10
c = f * r / k
s = sum(c*(1+y/k)**(-i) for i in range(1,n*k+1))+f*(1+y/k)**(-n*k)
print("Current market price of the bond:", s)

"""
A $10,000 bond with a five-year term, a 3.7% coupon rate paying semi-annually 
was issued eight months ago. The current market yield is 3.5%.

What is the current price of the bond?

What is the accrued interest on the bond?
"""
f = 10000
r = 0.037
k = 2
y = 0.035
n = 5
c = f * r / k
def bond_price(face_value, coupon, periods, yield_rate):
    pv_coupons = sum(coupon / (1 + yield_rate)**i for i in range(1, int(periods) + 1))
    if periods % 1 != 0:
        fractional_period = periods % 1
        pv_coupons += coupon / (1 + yield_rate)**fractional_period
    pv_face_value = face_value / (1 + yield_rate)**periods
    return pv_coupons + pv_face_value
current_price = bond_price(f, c, n*k-8/6, y/k)
print("Current price of the bond:", current_price)

d = (8-6)*30
D = 6*30
print("Accrued interest on the bond:", c * d / D)

"""
Question 3: Consider a $10,000 semi-annual bond with a twenty-year term and a 4.5% coupon rate. 
The bond was issued five-years ago and currently trades at a price of $10,500. What is the yield 
on the bond?
"""
f = 10000
r = 0.045
k = 2
n = 15
c = f * r / k
s = 10500
y = bond_ytm(s, f, c, n*k)*k
print("Yield on the bond:", y)