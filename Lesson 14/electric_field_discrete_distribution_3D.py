from random import randrange, random
import numpy as np
from numpy import pi
from matplotlib.pyplot import quiver
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

num = 40 # number of points in each space dimension
epsilon_0 = 1 # permittivity of free space set to 1 using particular units
x_min = x_max = y_min = y_max = z_min = z_max = 5
x = np.linspace(-x_min, x_max, num) # last argument is the number of points to include linearly between lower and upper limit
y = np.linspace(-y_min, y_max, num)
z = np.linspace(-z_min, z_max, num)
charge_values_list = []
charge_position_list = []
data = [] # will store lists containing E_x, E_y, E_z, x, y, z

# Specify position and sign of charge

charge_position_list.append([2, 0, 0])
charge_position_list.append([-2, 0, 0])
charge_position_list.append([0, 2, 0])
charge_position_list.append(([0, -2, 0]))
charge_values_list.append(-1)
charge_values_list.append(-1)
charge_values_list.append(1)
charge_values_list.append(1)

def get_distance(x_charge, y_charge, z_charge, x_position, y_position, z_position):

    # Return the distance between a charge and a position in space

    return np.sqrt((y_position-y_charge)**2 + (x_position-x_charge)**2 + (z_position-z_charge)**2)


# For all positions in the x, y space

for x_pos in x:

    for y_pos in y:

        for z_pos in z:

            # Initialize the electric field at the new position to 0, these variables will store the final electric field at that position
            # then appended to a list and once the for loop comes back to here they will be re-assigned to 0 for the next space position

            E_x_total = 0
            E_y_total = 0
            E_z_total = 0

            # For all charges

            for i in range(len(charge_values_list)):

                x_charge_position = charge_position_list[i][0]
                y_charge_position = charge_position_list[i][1]
                z_charge_position = charge_position_list[i][2]

                r = get_distance(x_charge_position, y_charge_position, z_charge_position, x_pos, y_pos, z_pos) # get distance from charge to point in space we want to calculate the electric field at
                r_x = x_pos - x_charge_position
                r_y = y_pos - y_charge_position
                r_z = z_pos - z_charge_position

                # Accumulate the electric field at this position contributed from all charged indexed by dummy variable i

                E_x_total += (1/(4*pi*epsilon_0))*(charge_values_list[i]*r_x)/(r**3)
                E_y_total += (1/(4*pi*epsilon_0))*(charge_values_list[i]*r_y)/(r**3)
                E_z_total += (1/(4*pi*epsilon_0))*(charge_values_list[i]*r_z)/(r**3)

            data.append([E_x_total, E_y_total, E_z_total, x_pos, y_pos, z_pos])


X_POS, Y_POS, Z_POS, E_X, E_Y, E_Z = [], [], [], [], [], []

for element in data:

    if (element[0]**2 + element[1]**2 + element[2]**2)**(1/2) > 0.2: # checking if the electric field diverged at that position because of the 1/r**3 which tends to a very large number when r tends to 0
        continue # because the field diverges when r gets very small, this happens when the point is space is very near to a charge

    E_X.append(element[0])
    E_Y.append(element[1])
    E_Z.append(element[2])

    X_POS.append(element[3])
    Y_POS.append(element[4])
    Z_POS.append(element[5])


ax = plt.figure().add_subplot(projection='3d')
quiver(X_POS, Y_POS, Z_POS, E_X, E_Y, E_Z) # the bigger the vector's magnitude the brighter its colour
plt.xlim(-3, 3) # limits on the x axis
plt.ylim(-3, 3)
plt.show()
