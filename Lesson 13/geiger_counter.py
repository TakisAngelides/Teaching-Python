import random
import winsound
from numpy import arange
import matplotlib.pyplot as plt

lambda_constant = 0.5

N = 100

t_list = []
N_list = []

for time in range(200):

    print(time)

    t_list.append(time)
    N_list.append(N)

    for atom in arange(1, N):

        rdm = random.uniform(0, 1)  # from 0 to 1 inclusive

        if rdm < lambda_constant:

            N -= 1

            winsound.Beep(600, 10)

plt.plot(t_list, N_list)
plt.show()



