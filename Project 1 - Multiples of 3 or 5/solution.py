import math

def solution():
    runningSum = 0
    # counting for multiples of 3
    for naturalNum in range(3,1000, 3):
        if naturalNum % 5 == 0:
            pass # want to avoid double counting with the 5s
        else:
            print(naturalNum)
            runningSum += naturalNum

    # counting for multiples of 5
    for naturalNum in range (5, 1000, 5):
        if naturalNum % 3 == 5:
            pass # want to avoid double counting with the 3s
        else:
            print(naturalNum)
            runningSum += naturalNum

    print(runningSum)

if __name__ == '__main__':
    solution()
