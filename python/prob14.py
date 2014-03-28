bestChainLength = 0
bestStartingNumber = 0
for currentNumber in xrange(999999, 1, -1):
    currentStaringNumber = currentNumber
    currentChainLength = 0
    while currentNumber != 1.0:
        currentNumberIsEven = currentNumber % 2 == 0

        if currentNumberIsEven:
            currentNumber /= 2
        else:
            currentNumber = 3 * currentNumber + 1

        currentChainLength += 1

    if currentChainLength > bestChainLength:
        bestChainLength = currentChainLength
        bestStartingNumber = currentStaringNumber

print("Best starting number: %d chain length: %d" %
      (bestStartingNumber, bestChainLength))
