def main():
    sum = 0
    square = 0
    for i in range(1,101):
        sum += i
        square += (i * i)
        #print i
    print sum * sum
    print square
    print "Difference:"
    print (sum * sum) - square


if __name__ == "__main__":
    main()