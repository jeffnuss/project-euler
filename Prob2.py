a, b = 1, 2
fsum = 0
sum = 2

while fsum <= 4000000:
    fsum =  a + b
    a = b
    b = fsum
    if fsum % 2 == 0:
        sum += fsum

print sum