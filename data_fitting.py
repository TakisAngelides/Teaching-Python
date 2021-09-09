import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# TODO: Write some code for polyfit

def trial_function(x, a, b, c):

    return a*np.exp(b*x) + c

x_data = np.linspace(0, 20, 20)
y_data = np.pi*np.exp(-(1/np.pi)*x_data) + np.pi

theoretical_a = np.pi
theoretical_b = -1/np.pi
theoretical_c = np.pi

initial_guess = [1, -1, 1]

parameters, parameter_covariance = curve_fit(trial_function, x_data, y_data, initial_guess)

fitted_a, fitted_b, fitted_c = parameters[0], parameters[1], parameters[2]

y_fitted = trial_function(x_data, fitted_a, fitted_b, fitted_c)

plt.scatter(x_data, y_data, marker = 'x', color = 'r')
plt.plot(x_data, y_fitted, color = 'k')
plt.legend([f'{fitted_a:.3f} $exp({fitted_b:.3f}x)$ + {fitted_c:.3f}', 'Data'])
plt.show()
