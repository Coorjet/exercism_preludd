import math

def square_of_sum(number):
    # Sum of the N first numbers : n(n-1)/2
    return(math.pow((number * (number + 1) / 2),2))



def sum_of_squares(number):
    sum = 0
    for i in range(number + 1):
        sum += math.pow(i, 2)
    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
