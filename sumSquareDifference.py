firstHundred = list(range(1,101))

SumOfSquares = 0
SquareOfSums = 0

for x in firstHundred:
    SumOfSquares = SumOfSquares + (x * x)
    SquareOfSums = SquareOfSums + x

SquareOfSums = SquareOfSums * SquareOfSums

difference = SquareOfSums - SumOfSquares

print(SumOfSquares, SquareOfSums)
print(difference)
