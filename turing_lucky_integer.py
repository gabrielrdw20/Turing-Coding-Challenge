'''This module is about finding a lucky integer.
E.g. is number 2 appears twice, it is a lucky number.
If number 4 appears 4 times, it is a lucky number.
If more than one number is lucky, return the bigger one.
'''


def makelist(items: str) -> int:
    '''Finds a lucky number from  input list'''
    result = None
    lucky_number = {}
    repeat = {}
    items = ' '.join(items).split()

    for item in items:
        repeat[item] = items.count(item)

    try:
        for key, value in repeat.items():
            if int(key) == int(value):
                lucky_number[key] = value
        result = max(lucky_number.keys())
    except:  # pylint: disable=W0702
        result = -1

    return result


if __name__ == '__main__':
    line = input()
    print(makelist(line))
