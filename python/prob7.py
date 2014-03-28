import math


def main():
    primes = [2]

    startingNumber = 3
    primeNumberToFind = 10001

    while (len(primes)) != primeNumberToFind:
        numToCheck = math.sqrt(startingNumber)
        isPrime = True
        # for prime in primes:
        n = 0
        prime = primes[n]
        while prime < numToCheck:
            prime = primes[n]
            # print "Mod: " + str(numToCheck) + " % " + str(prime) + " = " + str(startingNumber % prime)
            if (startingNumber % prime == 0):
                isPrime = False
                # print str(startingNumber) + " is not prime"
            n += 1
        if isPrime:
            primes.append(startingNumber)
        startingNumber += 2
        # print startingNumber

    print primes[primeNumberToFind - 1]

if __name__ == "__main__":
    main()
