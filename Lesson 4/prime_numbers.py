import matplotlib.pyplot as plt
import numpy as np

def generate_N_primes(N):

    primes = [] # list to store the prime numbers
    candidate = 2 # candidate will be the variable we are testing if its a prime and we are starting with 2

    while len(primes) < N: # while our list has less prime numbers stored than what we asked the function to find we do the following

        flag = True # If the flag is true the candidate is a prime number so we start by assuming it is a prime

        for i in range(2, candidate): # i goes from 2 to candidate-1

            if candidate % i == 0: # check if the candidate number we assume is prime for now is divisible by i
                flag = False # if it is divisible by i then candidate is not a prime number so we set the flag to false
                break # this stops the for loop because we already know that candidate is not prime

        if flag: # if the flag is true the candidate is a prime and we store it in the primes list
            primes.append(candidate)

        candidate += 1 # we increment candidate by 1 to check the next integer on whether it is a prime number

    return primes

print(generate_N_primes(25))

def generate_primes_from_Ni_to_Nf(Ni, Nf):

    primes = []

    for i in range(Ni, Nf+1): # this is our candidates

        flag = True # assume candidate is prime unless we find below otherwise

        for j in range(2, i): # need to check if candidate is divisible with any integer smaller than candidate down to 2

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
