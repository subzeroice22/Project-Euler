
def isPalindrome(arg):
    return str(arg) == str(arg)[::-1]
    

A = []
B = []

for x in range(1000):
    A.append([])
    for y in range(1000):
        A[x].append(x * y)

biggest = 0

for x in A:
    for y in x:
        if (isPalindrome(y) and y > biggest):
            biggest = y

print(biggest)
