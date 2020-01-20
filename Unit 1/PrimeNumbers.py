"""
    Define a function to calculate how many prime numbers there are in a
    range given by the user. Calculate whether a number is prime or not
    by checking if the previous prime numbers can be divided by it
"""

user_input = int(input("Introduce the range to look for prime numbers: "))

def prime(num):
    primes = []
    primes.append(2)
    for i in range(2, num):
        for j in primes:
            if (i % j) == 0:
                break
            else:
                primes.append(i)
    return primes
print(prime(user_input))
