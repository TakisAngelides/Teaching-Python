import random
import winsound
from numpy import arange
import matplotlib.pyplot as plt

lambda_constant = 0.005

N = 5000

t_list = []
N_list = []

for time in range(1000):

    t_list.append(time)
    N_list.append(N)

    for atom in arange(1, N):

        rdm = random.random()  # from 0 to 1 inclusive exclusive

        if rdm < lambda_constant:

            N -= 1

            winsound.Beep(600, 100)

plt.plot(t_list, N_list)
plt.show()



