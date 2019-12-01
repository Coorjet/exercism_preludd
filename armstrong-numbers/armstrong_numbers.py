import math

def is_armstrong_number(number):
    stringifiedNumber = str(number)
    numberLength = len(stringifiedNumber)
    digitsSum = 0
    for i in range(numberLength):
        digitsSum += math.pow(int(stringifiedNumber[i]),numberLength)

    return (digitsSum == number)

