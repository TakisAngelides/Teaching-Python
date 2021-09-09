from random import randrange, random
import numpy as np
from numpy import pi
from matplotlib.pyplot import quiver
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

epsilon_0 = 1
x_min = x_max = y_min = y_max = 5
x = np.linspace(-x_min, x_max, 150)
y = np.linspace(-y_min, y_max, 150)
charge_values_list = []
charge_position_list = []
data = []

charge_position_list.append([2, 0])
charge_position_list.append([-2, 0])
charge_position_list.append([0, 2])
charge_position_list.append(([0, -2]))
charge_values_list.append(-1)
charge_values_list.append(-1)
charge_values_list.append(1)
charge_values_list.append(1)

def get_distance(x_charge, y_charge, x_position, y_position):

    return np.sqrt((y_position-y_charge)**2 + (x_position-x_charge)**2)


for x_pos in x:

    for y_pos in y:

        E_x_total = 0
        E_y_total = 0

        for i in range(len(charge_values_list)):

            x_charge_position = charge_position_list[i][0]
            y_charge_position = charge_position_list[i][1]
            r = get_distance(x_charge_position, y_charge_position, x_pos, y_pos)
            # if r < 0.0001:
            #     continue
            r_x = x_pos - x_charge_position
            r_y = y_pos - y_charge_position
            E_x_total += (1/(4*pi*epsilon_0))*(charge_values_list[i]*r_x)/(r**3)
            E_y_total += (1/(4*pi*epsilon_0))*(charge_values_list[i]*r_y)/(r**3)

        data.append([E_x_total, E_y_total, x_pos, y_pos])


X_POS, Y_POS, E_X, E_Y = [], [], [], []

for element in data:

    if (element[0]**2+element[1]**2)**(1/2) > 0.2:
        continue
    X_POS.append(element[2])
    Y_POS.append(element[3])
    E_X.append(element[0])
    E_Y.append(element[1])

E_mag_data = (np.array(E_X)**2+np.array(E_Y)**2)**(1/2)
norm = Normalize()
norm.autoscale(E_mag_data)
colormap = cm.inferno

fig = plt.figure()
ax = fig.gca()
quiver(X_POS, Y_POS, E_X, E_Y, color = colormap(norm(E_mag_data)), scale = 4)
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.show()
