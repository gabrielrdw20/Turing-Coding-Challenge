'''Find two numbers that sum gives value nearest to a K variable value.
E.g. list=[1,2,10,13], K = 15, max_sum = 12 (2 + 10).
'''

import itertools
K = 0.39

def add_two_numbers(list1: list, k_number):
    '''Adds two numbers to get the result as close as possible to the value of the variable K.'''
    result = None
    comparable_numbers = []
    smaller_numbers = []
    numbers = [float(value) for value in list1.split()]
    empty = []
    for number in numbers:
        if number < k_number:
            smaller_numbers.append(number)

    if smaller_numbers != empty:
        for number_a, number_a_plus_j in itertools.combinations(smaller_numbers, 2):
            if number_a + number_a_plus_j < k_number:
                comparable_numbers.append(number_a + number_a_plus_j)
        try:
            result = max(comparable_numbers)
        except:  # pylint: disable=W0702
            result: -1
    else:
        result = -1
    return result


line = input()
print(add_two_numbers(line, K))
