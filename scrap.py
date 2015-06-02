index = 2
stop = 65

multiples = (x for x in range(index, stop + 1) if x % index == 0)

for x in multiples:
    print(x)
