import matplotlib.pyplot as plt # import this for plotting
from scipy.optimize import curve_fit # curve_fit is a function that finds the parameters for a function that will fit best the data given
import numpy as np
from numpy import polyfit # fits a polynomial function to given data, ie it gives the coefficients a,b,c... in a+b*x+c*(x*x)

# --------------------------------------------------------------------------------------------------------------------

# In this section we look at curve_fit from scipy package

def trial_function(x, a, b, c): # define a function to give to the function curve_fit in order to find the best a,b,c that fit the data given

    return a*np.exp(b*x) + c

x_data = np.linspace(0, 20, 30) # generates the x data from 0 to 20, the last number input 30 is the number of data points
y_data = np.pi*np.exp(-(1/np.pi)*x_data) + np.pi # we generate the y data to be fitted and pretend we don't know the coefficients, compare this with what the trial_function returns

# these are the values we pretend we don't know and expect curve_fit to find
theoretical_a = np.pi
theoretical_b = -1/np.pi
theoretical_c = np.pi

initial_guess = [1, -1, 1] # initial guess for [a,b,c] which we can give to curve_fit (this is optional)

parameters, parameter_covariance = curve_fit(trial_function, x_data, y_data, initial_guess) # the curve_fit function returns the parameters and their uncertainty, ie how confident the fitting is that a,b,c are what it estimated them to be

fitted_a, fitted_b, fitted_c = parameters[0], parameters[1], parameters[2] # we just put the parameters into new variables

y_fitted = trial_function(x_data, fitted_a, fitted_b, fitted_c) # we input the fitted parameters to plot the function we approximated using our data

# below is for making a plot
plt.scatter(x_data, y_data, marker = 'x', color = 'r')
plt.plot(x_data, y_fitted, color = 'k')
plt.legend([f'y = {fitted_a:.3f} $exp({fitted_b:.3f}x)$ + {fitted_c:.3f}', 'Data'])
plt.show()

# ---------------------------------------------------------------------------------------------------------------------

# Here we look at polyfit from numpy package

x_data = np.linspace(0, 1, 20)
y_data = 2 + 3*x_data - 4*x_data**2

# polyfit minimises square difference between real y which are the y_data and a+bx+cx*x...
coefficients = polyfit(x_data, y_data, 2) # coefficients of polynomial function approximated in decreasing order of degree ie the y-intercept is at coefficients[-1], the -1 is used to index the last element of a list

y_fit = coefficients[2] + coefficients[1]*x_data + coefficients[0]*x_data**2 # we compute the function we approximated

# below is for making a plot
plt.scatter(x_data, y_data, color = 'k', marker = '+', s = 100)
plt.plot(x_data, y_fit, color = 'r')
plt.legend([f'y = {coefficients[2]:.3f} + {coefficients[1]:.3f}x + {coefficients[0]:.3f}*$x^2$', 'Data'])
plt.show()

