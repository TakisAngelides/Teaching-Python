from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------------------------------------

# 1

# Find the two roots of the function f(x) = e^(-x^2) - 1/2.

# Hint: You can use np.exp() from numpy for e.

# ------------------------------------------------------------------------------------------------------------------

# 2

# Find the intersection of the functions f(x) = e^(-x^2) - 1/2 and g(x) = x^2.

# ------------------------------------------------------------------------------------------------------------------

# 3

# Make a plot containing all the roots and intersection points you have found along with the graphs of f and g.

# ------------------------------------------------------------------------------------------------------------------


# Solutions

# ------------------------------------------------------------------------------------------------------------------

# 1

def f(x):

    return np.exp(-x**2)-0.5


x = np.linspace(-1, 1, 1000)
plt.plot(x, f(x), color = 'k') # this will show us that f(x) has two roots and help us with the initial guess
plt.title('f(x)')
plt.grid()
plt.show()

initial_guess_for_f = np.array([-1, 1])

roots_of_f = fsolve(f, initial_guess_for_f)

print(roots_of_f)

# ------------------------------------------------------------------------------------------------------------------

# 2

def g(x):

    return x**2

def h(x):

    return f(x) - g(x)

plt.plot(x, h(x))
plt.title('h(x)')
plt.grid()
plt.show()

initial_guess_for_h = np.array([-1, 1])

roots_of_h = fsolve(h, initial_guess_for_h)

print(roots_of_h)

# ------------------------------------------------------------------------------------------------------------------

# 3

x = np.linspace(-1, 1, 1000)

plt.plot(x, f(x), color = 'k', zorder = 0, label = 'f(x) = $e^{-x^2} - 0.5$')
plt.plot(x, g(x), color = 'blue', zorder = 1, label = 'g(x) = $x^2$')

for root_f in roots_of_f:

    plt.scatter(root_f, f(root_f), color = 'r', marker = 'x', s = 100, zorder = 2, label = 'Roots of f(x) = $e^{-x^2} - 0.5$')

for root_h in roots_of_h:

    plt.scatter(root_h, f(root_h), color = 'orange', marker = 'x', s = 100, zorder = 3, label = 'Intersection points\nh(x) = f(x) - g(x) = 0')

plt.grid()
plt.legend()
plt.show()

# ------------------------------------------------------------------------------------------------------------------

