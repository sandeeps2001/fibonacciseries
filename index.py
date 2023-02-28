# A CONSTANT VARIABLE WHICH IS SET TO BE 100, DEFINES THE MAXIMUM THRESHOLD OF OUR MACHINE TO PRINT FIBBO SERIES
MAX = 100
MIN = 1

def getFibonacciSeries(numSize):
    prevVal = 0 
    currVal = 1
    try:
        if numSize.isnumeric()== False:
            raise Exception("sorry , input should me numeric ")
        else:
            numSize = int(numSize)
        if(numSize > MAX):
            raise Exception("Sorry, you are exceeded the maximum limit")
        
        if(numSize < MIN):
            raise Exception("the num size should be greater than {}".format(MIN))

        if(numSize == MIN):
            print("the value at {} of the fiboSeries is {}".format(numSize, 0))
            return
        
        print("the series {} {}".format(prevVal, currVal), end="")
        i = 2
        while (i < numSize):
            nextVal = prevVal + currVal
            prevVal = currVal
            currVal = nextVal
            print(" {}".format(nextVal), end="")
            i += 1
        
        print("")
        print("\nthe value at {} of the fiboSeries is {}".format(numSize, currVal))
    except Exception as error:
        print(error)

num = input("enter the number value : ")
getFibonacciSeries(num)
