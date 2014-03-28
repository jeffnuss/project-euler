a = 1000
b = 3
c = 5
sum = 0

for i in range(a):
    if i % b == 0 or i % c == 0:
        sum += i
    
print sum