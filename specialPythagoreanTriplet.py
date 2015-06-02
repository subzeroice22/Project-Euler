from math import sqrt

triplesArray = []

def triples(n):
    squares = [x*x for x in range(1,n)]
    for x in squares:
        for y in squares:
            if ((x + y) in squares):
                a = sqrt(x)
                b = sqrt(y)
                c = sqrt(x+y)
                if(a + b + c == 1000):
                    return (a * b * c)
                triple = (sqrt(x), sqrt(y), sqrt(x+y))

print(triples(1000))
