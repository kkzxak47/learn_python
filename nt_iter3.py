from math import exp
x = 0.5
for i in range(10):
    x = (x*x*exp(x)+1)/(exp(x)+x*exp(x))
    print(x)