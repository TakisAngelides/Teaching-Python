import matplotlib.pyplot as plt
import numpy as np

def generate_N_primes(N):

    primes = []
    candidate = 2

    while len(primes) < N:

        flag = True

        for i in range(2, candidate):

            if candidate % i == 0:
                flag = False
                break

        if flag:
            primes.append(candidate)

        candidate += 1

    return primes

print(generate_N_primes(25))

def generate_primes_from_Ni_to_Nf(Ni, Nf):

    primes = []

    for i in range(Ni, Nf+1):

        flag = True

        for j in range(2, i):

            if i % j == 0:

                flag = False
                break

        if flag:
            primes.append(i)

    return primes

Ni = 10000
Nf = 10100

print(generate_primes_from_Ni_to_Nf(Ni, Nf))

primes = generate_primes_from_Ni_to_Nf(Ni, Nf)
x = np.arange(Ni, Nf+1)
y = []
for element in x:
    if element in primes:
        y.append(element)
    else:
        y.append(0)

plt.scatter(x, y, marker = 'x', color = 'k')
plt.show()
