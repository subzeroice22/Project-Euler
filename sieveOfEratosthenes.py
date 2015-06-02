import math
from time import gmtime, strftime

def shortcut(number):
    val = math.floor(math.sqrt(number))
    if (val % 2 == 0):
        val = val - 1
    foo = []
    for x in range(val, 0, -1):
        foo.append(x)

    print(len(foo))

def sieveOfEratosthenes(end):
    stop = math.floor(math.sqrt(end))
    primeArray = [True]*(stop + 1)

    for x in range(4, stop, 2):
        primeArray[x] = False

    index = 2
    proceed = True

    while (index < stop and proceed == True):

        while (primeArray[index] == False and index < stop):
            index = index + 1
            if (index == stop):
                proceed = False

        multiples = (x for x in range(index*index, stop + 1) if primeArray[x] != False and x != index and x % index == 0)

        for x in multiples:
            primeArray[x] = False

        index = index + 1

    primes = []
    index = 0

    for x in primeArray:
        if x == True and index != 0 and index != 1:
            primes.append(index)
        index = index + 1

    return primes

def primeFactors(number, primeList):
    factors = []
    for x in primeList:
        if (number % x == 0):
            factors.append(x)
    return factors

value = 13195
value2 = 600851475143

primes = sieveOfEratosthenes(value2)

primeFactorValues = primeFactors(value2,primes)

print(strftime("%H:%M:%S"), value2, primeFactorValues)

