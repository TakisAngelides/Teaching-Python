import matplotlib.pyplot as plt
import numpy as np
from numpy import polyfit
from scipy.optimize import curve_fit

#---------------------------------------------------------------------------------------------------------------------

# Exercise 1

# Use polyfit from numpy to find the function that describes the data in the text file data_exercise_1.txt which can
# be found in the teams folder of Lesson 9.

# Hint: Download the text file from teams and put it in the same folder as your pycharm project. First open the text
# file to see how the data are separated. Read the data from the text file to store it in
# python variables. Make a scatter plot of the data to see what kind of function might describe them. Then use polyfit
# accordingly to extract the coefficients that describe the function.

#---------------------------------------------------------------------------------------------------------------------

# Exercise 2

# Do the same as exercise 1 but now using curve_fit from scipy.optimize and with the data found in data_exercise_2.txt.

#---------------------------------------------------------------------------------------------------------------------

# Exercise 3

# Do the same as exercise 1 but now using the data found in data_exercise_3.txt.






# Solutions

#---------------------------------------------------------------------------------------------------------------------

# 1

with open('data_exercise_1.txt', 'r') as f:

    x = []
    y = []

    line = f.readline()

    while line:

        row = line.strip().split(',')
        x.append(float(row[0]))
        y.append(float(row[1]))
        line = f.readline()

    plt.scatter(x, y)
    plt.show()

x = np.array(x)
y = np.array(y)

coefficients = polyfit(x, y, 1)

y_fit = coefficients[1] + coefficients[0]*x

plt.scatter(x, y, color = 'k', marker = '+', s = 100)
plt.plot(x, y_fit, color = 'r')
plt.legend([f'y = {coefficients[1]:.3f} + {coefficients[0]:.3f}x', 'Data'])
plt.show()

# So we find the coefficients to be 2 and 1, ie the function is y = 2x + 1

# Here is how I have written the data to the text file. The function to be found can be seen below to be y = 2x + 1
# so the coefficients that describe the function are a = 2 and b = 1.

# with open('data_exercise_1.txt', 'w') as f:
#
#     x = np.linspace(0, 100, 100)
#     y = 2*x + 1
#
#     for i in range(len(x)):
#
#         if i != len(x)-1:
#
#             f.write(f'{x[i]},{y[i]}')
#             f.write('\n')
#
#         else:
#
#             f.write(f'{x[i]},{y[i]}')

#---------------------------------------------------------------------------------------------------------------------

# 2

with open('data_exercise_2.txt', 'r') as f:

    x = []
    y = []

    line = f.readline()

    while line:

        row = line.strip().split(',')
        x.append(float(row[0]))
        y.append(float(row[1]))
        line = f.readline()

    plt.scatter(x, y)
    plt.show()

x = np.array(x)
y = np.array(y)

def trial_function(x, a, b, c):

    return a*np.exp(b*x)+c

initial_guess = [1, -1, 0]

parameters, parameter_covariance = curve_fit(trial_function, x, y, initial_guess)

fitted_a, fitted_b, fitted_c = parameters[0], parameters[1], parameters[2]

y_fitted = trial_function(x, fitted_a, fitted_b, fitted_c)

plt.scatter(x, y, marker = 'x', color = 'r')
plt.plot(x, y_fitted, color = 'k')
plt.legend([f'y = {fitted_a:.3f} $exp({fitted_b:.3f}x)$ + {fitted_c:.3f}', 'Data'])
plt.show()

# So we find the coefficients that describe the function which fits the data are a = 1, b = -1, c = 0.

# Here is how I have written the data to the text file. The function to be found can be seen below to be y = exp(-x)
# so the coefficients that describe the function are a = 1, b = -1, c = 0.

# with open('data_exercise_2.txt', 'w') as f:
#
#     x = np.linspace(0, 20, 100)
#     y = np.exp(-x)
#
#     for i in range(len(x)):
#
#         if i != len(x)-1:
#
#             f.write(f'{x[i]},{y[i]}')
#             f.write('\n')
#
#         else:
#
#             f.write(f'{x[i]},{y[i]}')

#---------------------------------------------------------------------------------------------------------------------

# 3

with open('data_exercise_3.txt', 'r') as f:

    x = []
    y = []

    line = f.readline()

    while line:

        row = line.strip().split(',')
        x.append(float(row[0]))
        y.append(float(row[1]))
        line = f.readline()

    plt.scatter(x, y)
    plt.show()

x = np.array(x)
y = np.array(y)

coefficients = polyfit(x, y, 3)

y_fit = coefficients[3] + coefficients[2]*x + coefficients[1]*x**2 + coefficients[0]*x**3

plt.scatter(x, y, color = 'k', marker = '+', s = 100)
plt.plot(x, y_fit, color = 'r')
plt.legend([f'y = {coefficients[3]:.3f} + {coefficients[2]:.3f}x + {coefficients[1]:.3f}$x^2$ + {coefficients[0]:.3f}$x^3$', 'Data'])
plt.show()

# So we find the coefficients that describe the function which fits the data are a = -3, b = 4, c = 2, d = -1.

# Here is how I have written the data to the text file. The function to be found can be seen below to be
# y = - 3*x**3 + 4*x**2 + 2*x - 1, so the coefficients that describe the function are a = -3, b = 4, c = 2, d = -1.

# with open('data_exercise_3.txt', 'w') as f:
#
#     x = np.linspace(-50, 50, 100)
#     y = - 3*x**3 + 4*x**2 + 2*x - 1
#
#     for i in range(len(x)):
#
#         if i != len(x)-1:
#
#             f.write(f'{x[i]},{y[i]}')
#             f.write('\n')
#
#         else:
#
#             f.write(f'{x[i]},{y[i]}')

