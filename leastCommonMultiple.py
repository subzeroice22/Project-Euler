from functools import reduce
from collections import deque

def gcd(a,b):
    if (b == 0):
        return a
    if (a >= b and b > 0):
        return gcd(b, a % b)
    if ( b >= a and a > 0):
        return gcd(a, b % a)

def lcm(a,b):
    return (a*b) / gcd(a,b)

numbers = deque(range(1,21))

while (len(numbers)) > 1:
    numbers.append(lcm(numbers[0], numbers[1]))
    numbers.popleft()
    numbers.popleft()
    print(len(numbers))

print(numbers)
