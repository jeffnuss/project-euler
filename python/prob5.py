a = 2*3*4*5*7*8*11*13*17*19 # 465585120
check = 0
for j in range(20):
    check = 0
    a = a/(j+1)
    for i in range(20):
        a = 2*3*4*5*7*8*11*13*17*19*3
        if a % (i+1) != 0:
            print str(a) + " not divisible by " + str(i+1)
            check = 1
    if check == 0:
        print a
        
if  check == 0:
    print str(a)