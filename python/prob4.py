def IsPalindrome(numberToCheck):
    numStr = str(numberToCheck)
    i = len(numStr) / 2
    j = 0
    while j < i:
        if numStr[j] != numStr[len(numStr) - 1 - j]:
            return False
        j += 1
    return True

def main():
    startLeft = 999
    startRight = 999
    limit = startLeft * startRight

    stop = False
    checkLeft = startLeft
    checkRight = startRight

    while not stop:
        checkLeft = checkLeft - 1
        checkRight = checkRight - 1
        check = checkRight * checkLeft
        limit = startRight * startLeft
        #print startRight
        while startLeft > checkLeft - 100:
            if IsPalindrome(limit):
                resultRight = startRight
                resultLeft = startLeft
                stop = True
                break
            #print startLeft
            startLeft -= 1
            limit = startRight * startLeft
        startLeft = checkLeft
        startRight -= 1

    print
    print "Result:"
    print resultRight
    print resultLeft
    print limit
    #906609

if __name__ == "__main__":
    main()