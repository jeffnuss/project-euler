import sys
import math


def findTriangleNumber(n):
    triangleNumber = 0
    for x in range(1, n + 1):
        triangleNumber += x
    return triangleNumber


def findNumberOfDivisors(n):
    # divisors = []
    numberOfDivisors = 1
    for x in range(1, int(math.ceil(n ** 0.5))):
        if n % x == 0:
            numberOfDivisors += 2
            # divisors.append(x)
    # divisors.append(n)
    # return len(divisors)
    return numberOfDivisors


def findFirstTriangleNumberWithDivisors(n):
    finished = False
    i = 1
    while not finished:
        triangleNumber = findTriangleNumber(i)
        numberOfDivisors = findNumberOfDivisors(triangleNumber)
        finished = numberOfDivisors > n
        i += 1
    print("Found triangle number with at least %d divisors: %d is the %dth triangle number" %
          (n, triangleNumber, i - 1))


def main(argv):
    findFirstTriangleNumberWithDivisors(int(argv[1]))

if __name__ == '__main__':
    main(sys.argv)
