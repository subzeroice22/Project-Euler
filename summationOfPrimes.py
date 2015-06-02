import math

def sieveOfEratosthenes(end):
    #stop = math.floor(math.sqrt(end))
    stop = end
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

        print(index, '{percent:.2%}'.format(percent=(float(index)/float(stop))))

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

summation = 0

primes = sieveOfEratosthenes(2000000)

for x in primes:
    summation = summation + x

print('Sum:', summation)
