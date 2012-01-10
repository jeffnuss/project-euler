#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jeff Nuss
#
# Created:     10/01/2012
# Copyright:   (c) Jeff Nuss 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    #target = 600851475143.0
    #target = 8462696833.0 #71
    #target = 10086647.0 #839
    target = 6857.0 #1471
    n = 2
    factors = []
    keepGoing = True
    while (keepGoing):
        if (target % n == 0):
            factors.append(n)
            keepGoing = False
            print(target / n)
            print(n)
        n += 1

if __name__ == '__main__':
    main()
