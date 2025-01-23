"""
Question 1:Suppose $1 was invested in 1776 at 3.3% interest compounded annually.
Approximately how much would that investment be worth today? What if the interest rate were 6.6%?
"""
print((1+0.033)**(2025-1776))
print((1+0.066)**(2025-1776))

"""
Question 2: Find the corresponding effective rates for:
3% compounded monthly, 18% compounded monthly, 18% compounded quarterly.
"""
print((1+0.03/12)**12-1)
print((1+0.18/12)**12-1)
print((1+0.18/4)**4-1)

"""
Question 3: Two copy machines are available. Both have useful lives of 5 years. One machine can be either 
leased or purchased outright, the other must be purchased. Below is a description of the three options A, B, C 
with the first year's maintenance included in the initial cost. There are then four additional yearly payments 
occurring at the beginning of each year, followed by the revenues from any resale. 
According to a PV analysis the least cost option is B:
Initial Outlay: 6000, 30000, 35000
Yearly Expense: 8000, 2000, 1600
Resale Value: 0, 10000, 12000
PV at 10%: 31559, 30131, 32621

It is not possible to compute an IRR on these options since the cashflows are all negative, except for the resale 
value. It is possible, however, to calculate the IRR on an incremental basis. Find the IRR on a change from A to B. 
Is this change justified on an IRR basis?
"""
#Note1: IRR is the rate at which the net present value of cash flows equals zero.
cashflowA = [-6000, -8000, -8000, -8000, -8000, 0]
cashflowB = [-30000, -2000, -2000, -2000, -2000, 10000]
change = [b - a for a, b in zip(cashflowA, cashflowB)]
from sympy import symbols, Eq, solve
r = symbols('r')
time = [i for i in range(len(change))]
eq1 = Eq(sum(c/(1+r)**i for i, c in enumerate(change)),0)
sol = solve(eq1,r)
numerical_irr = [s.evalf() for s in sol][0]
print("Numerical IRR:", numerical_irr)

"""
Question 4: Gavin's father, Mr. Jones, has just turned 90 years-old and is applying for a lifetime annuity 
that will pay $10,000 per year, starting 1 year from now, until he dies. He asks Gavin to analyze it for him. 
Gavin finds that according to statistical summaries, the probability of that Mr. Jones will die at a particular age is:
age: (90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)
prob.: (0.07, 0.08,0.09,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)

What would Gavin's answers be to the following questions:
What is Mr. Jones's (Gavin's father's) life expectancy?

What is the PV of an annuity at 8% interest that has a lifetime 
equal to Mr. Jones's life expectancy? (For an annuity equal to 
a non-integral number of years use an averaging method.)

What is the expected PV of the annuity?

What is the standard deviation of the annuity?
"""
age = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,101]
p = [0.07,0.08,0.09,0.1,0.1,0.1,0.1,0.1,0.1,0.07,0.05,0.04]
deathage = [a+0.5 for a in age]
life_expectancy = sum(p[i]*deathage[i] for i in range(len(p)))
print("Life Expectancy:", life_expectancy)

import math
r = 0.08
pv = sum((1+r)**(-i) for i in range(1,math.ceil(life_expectancy)+1-90))
print("PV of Anuity:", pv*10000)

expected_pv = [0]*len(p)
for i in range(len(p)):
    expected_pv[i] = sum((1+r)**(-j) for j in range(1,age[i]+1-90))*10000
exp_pv = sum(expected_pv[i]*p[i] for i in range(len(p)))
print("Expected PV of Annuity:", exp_pv)

age_sqrd = [a**2 for a in age]
expected_pv_sqrd = [0]*len(p)
exp_pv_sqrd = sum(p[i]*expected_pv[i]**2 for i in range(len(p)))
std_dev = exp_pv_sqrd - exp_pv**2
print("Standard Deviation of Annuity:", math.sqrt(std_dev))

"""
The Smith family just took out a variable-rate mortgage on their 
new home. The mortgage value is $100,000, the term is 30 years, 
and the initial interest rate is 8%. This rate is guaranteed for 5 
years, after which it will be adjusted to the prevailing rates. 
The mortgage will be adjusted by either modifying the payment 
amount or the length of the remaining loan.

What is the monthly payment at the start of the mortgage?

What is the mortgage balance after 5 years?

If the prevailing rate is 9% at the readjustment point and the 
mortgage termination date is kept constant, then what is the 
new monthly payment?

Under the same conditions immediately above, if the monthly payment 
is kept constant, then what it the new term (i.e., years and months 
remaining) of the mortgage?
"""
r = 0.08
k =12
y =30
m = 100000
from sympy import symbols, Eq, solve
p = symbols('p')
eq2 = Eq(sum(p*(1+r/k)**(-i) for i in range(1,y*k+1)),m)
sol2 = solve(eq2,p)
mon_pay = [s.evalf() for s in sol2][0]
print("Monthly Payment:", mon_pay)

balance = sum(mon_pay*(1+r/k)**(-i) for i in range(1,25*12+1))
print("Mortage balance after 5 years:",balance)

x = symbols('x')
eq3 = Eq(sum(x*(1+0.09/k)**(-i) for i in range(1,25*k+1)),balance)
sol3 = solve(eq3,x)
new_mon_pay = [s.evalf() for s in sol3][0]
print("New Monthly Payment at 9%:", new_mon_pay)

r = 0.09/12
t= symbols('t')
n = -math.log(1-balance*r/mon_pay)/math.log(1+r) 
year = n//12
month = n% 12
print("New Term of Mortgage:", year, "years and", month, "months remaining")

"""
Question 6: A firm wishes to purchase a building for $10,000,000. Origination 
fees and other costs will total $25,000. The firm has $2,000,000 to cover the 
initial costs and down payment on the building. The mortgage terms available 
are a 5-year term with monthly payments computed at 7.5% with an amortization 
of 20 years. 

What is the amount of the mortgage?

What are the monthly payments and final balloon payment?

How much interest did the firm pay over the 5 years of the mortgage?
"""
mortgage = 10000000 +25000 - 2000000

p = symbols('p')
eq4 = Eq(sum(p*(1+0.075/12)**(-i) for i in range(1,20*12+1)),mortgage)
sol4 = solve(eq4,p)
mon_pay = [s.evalf() for s in sol4][0]
balloon = sum(mon_pay*(1+0.075/12)**(-i) for i in range(1,15*12+1))
print("Monthly payment:", mon_pay, "Balloon payment:", balloon)

print("Total interest paid over 5 years:", 12*5*mon_pay - (mortgage - balloon))

"""
Question 7: Arthur is planning on buying a house and needs to take out a mortgage for $200,000. 
He has two choices a 30-year with monthly payments of $1,468 and a 15-year with 
monthly payments of 1,854. Arthur wants to pay the lowest interest rate possible. 

What is the interest rate on each mortgage and which mortgage should he pick?

He changes his mind and wants to pay the smallest amount of total interest. 
What are the total interest charges for each mortgage and which mortgage 
should he now pick?
"""
from scipy.optimize import root_scalar

def find_interest_rate(principal, monthly_payment, num_payments):
    def equation(r):
        return principal-monthly_payment*(1-(1+r)**(-num_payments))/r
    result = root_scalar(equation, bracket=[1e-8, 1], method='brentq')
    return result.root * 12 
rate_30yr = find_interest_rate(200000, 1468, 30*12)
rate_15yr = find_interest_rate(200000, 1854, 15*12)
print("Interest rate for 30-year mortgage:", rate_30yr,"Interest rate for 15-year mortgage:", rate_15yr)

print("Total interest for 30-year mortgage:", 1468*30*12 - 200000,"Total interest for 15-year mortgage:", 1854*15*12 - 200000)
 


