from random import randrange, random
import numpy as np
from numpy import pi
from matplotlib.pyplot import quiver
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

epsilon_0 = 1 # permittivity of free space set to 1 using particular units just like 1000 metres are 1 in kilometres units
x_min = x_max = y_min = y_max = 5
x = np.linspace(-x_min, x_max, 150) # last argument is the number of points to include linearly between lower and upper limit
y = np.linspace(-y_min, y_max, 150)
charge_values_list = []
charge_position_list = []
data = [] # will store lists containing E_x, E_y, x, y

# Specify position and sign of charge

charge_position_list.append([2, 0])
charge_position_list.append([-2, 0])
charge_position_list.append([0, 2])
charge_position_list.append(([0, -2]))
charge_values_list.append(-1)
charge_values_list.append(-1)
charge_values_list.append(1)
charge_values_list.append(1)

def get_distance(x_charge, y_charge, x_position, y_position):

    # Return the distance between a charge and a position in space

    return np.sqrt((y_position-y_charge)**2 + (x_position-x_charge)**2)


# For all positions in the x, y space

for x_pos in x:

    for y_pos in y:

        # Initialize the electric field at the new position to 0, these variables will store the final electric field at that position
        # then appended to a list and once the for loop comes back to here they will be re-assigned to 0 for the next space position

        E_x_total = 0
        E_y_total = 0

        # For all charges

        for i in range(len(charge_values_list)):

            # Get the position of the charge labelled by dummy index i

            x_charge_position = charge_position_list[i][0]
            y_charge_position = charge_position_list[i][1]

            r = get_distance(x_charge_position, y_charge_position, x_pos, y_pos) # get distance from charge to point in space we want to calculate the electric field at

            # r_space - r_charge will point away from charge and if the charge is negative it will point inward

            r_x = x_pos - x_charge_position
            r_y = y_pos - y_charge_position

            # Accumulate the electric field at this position contributed from all charged indexed by dummy variable i

            E_x_total += (1/(4*pi*epsilon_0))*(charge_values_list[i]*r_x)/(r**3)
            E_y_total += (1/(4*pi*epsilon_0))*(charge_values_list[i]*r_y)/(r**3)

        data.append([E_x_total, E_y_total, x_pos, y_pos]) #


X_POS, Y_POS, E_X, E_Y = [], [], [], []

for element in data:

    if (element[0]**2 + element[1]**2)**(1/2) > 0.2: # checking if the electric field diverged at that position because of the 1/r**3 which tends to a very large number when r tends to 0
        continue # because the field diverges when r gets very small, this happens when the point is space is very near to a charge

    E_X.append(element[0])
    E_Y.append(element[1])

    X_POS.append(element[2])
    Y_POS.append(element[3])

E_mag_data = (np.array(E_X)**2+np.array(E_Y)**2)**(1/2) # magnitude of electric field vector at each point
norm = Normalize()
norm.autoscale(E_mag_data) # normalized magnitudes meaning with values between 0 and 1
colormap = cm.inferno # hotter/brighter the bigger the value

quiver(X_POS, Y_POS, E_X, E_Y, color = colormap(norm(E_mag_data)), scale = 4) # the bigger the vector's magnitude the brighter its colour
plt.xlim(-3, 3) # limits on the x axis
plt.ylim(-3, 3)
plt.show()
