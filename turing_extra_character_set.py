'''This module finds an additional character in one of two given lists. Result of a set type.'''


def find(list1: list, list2: list) -> str:
    '''Finds extra character in one of the two passed lists.'''
    result = None
    if isinstance(list1, str) and isinstance(list2, str):
        list1 = ' '.join(list1).split()
        list2 = ' '.join(list2).split()
        if len(list1) > len(list2):
            result = list(set(list1) - set(list2))
        elif len(list2) > len(list1):
            result = list(set(list2) - set(list1))
        else:
            result = set()
            result.add(x for x in list1 if x not in list2)
            result.add(x for x in list2 if x not in list1)
            result = list(result)
    else:
        raise TypeError("Expected string data type.")
    return result


if __name__ == "__main__":
    list_1 = input()
    list_2 = input()
    print(find(list_1, list_2))
