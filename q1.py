import mm1
import matplotlib.pyplot as plt
import numpy as np 
import math

mm1.seed=1234
a=572
m=16381
n=10000

def integral(x):
	return math.exp(-x**2)


#without importance sampling
sum=0
sum1=0
for i in range(1,n+1):
	x=mm1.mlcg_random_number(a,m)#creating random number between 0 to 1
	sum+=integral(x)/n
	sum1+=(integral(x)**2)/n
	error=(sum1-(sum)**2)**0.5

print("The value of the integral without importance sampling",sum,"+/-",error)


#The value of integral with imoportance sampling
#probability function
def probF(x, alpha):
    return alpha*math.e**(-x)


alpha = math.e/(math.e-1)

integral_value = 0
for i in range(n):
	x = mm1.mlcg_random_number(a,m)
	prob = -math.log(1-x/alpha)
	integral_value += (integral(prob)/probF(prob,alpha))
	ans = integral_value/n


print("The value of the integral with importance sampling is ",ans)
print('Analytical Value = ',0.746824132812427)

#output 
"""
The value of the integral without importance sampling 0.7461017227461381 +/- 0.2011653349063367
The value of the integral with importance sampling is  0.7468066027734229
Analytical Value =  0.746824132812427"""