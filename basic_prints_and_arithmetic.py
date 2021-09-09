import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, quadrature, romberg

string_1 = 'Alice'
string_2 = 'Bob'

print(string_1)
print(string_2)
print(string_1+' '+string_2)

num_1 = 7
num_2 = 10

print(num_1)
print(num_2)
print(num_2/num_1)
print(int(num_2/num_1)) # int casts float to floor integer eg 1.6 -> 1 and 1.3 -> 1 and 2.1 -> 2
print(np.ceil(num_2/num_1)) # ceil will cast float to ceil integer but keeps it float eg 1.5 -> 2.0

print(string_1, num_1)
print(string_1 + ' ' + str(num_1))

a = 7
b = 10

c = b + a  # 17
d = b - a  # 3
e = b * a  # 70
f = b / a  # 1.4285714285714286 now the number is float
g = b // a # floor division: performs b / a then floors to integer
h = b % a  # 3

print(np.e)

num_3 = 4
print(num_3**2)

x = 2

print(np.e**(x))



