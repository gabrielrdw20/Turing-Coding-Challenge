'''Find a duplicated number in a set of numbers from 1 to n and replace it with a proper one.
Example: array = [0,1,2,3,5]
Expected output: [5,4]
Explanation: number 5 (last one) is an error and should be replaced with number 4.
'''


def find_duplicate(txt: str) -> list:
    '''Finds a duplicated number and replaecs it with a proper digit'''
    result = None

    def is_number(list_to_check: list):
        for number in list_to_check:
            checker = True
            if number.isalpha():
                checker = False
                break
        return checker
    if isinstance(txt, str) and is_number(txt):
        txt = txt.replace(",", "")
        nums = list(' '.join(txt).split())
        if nums[1:] > nums[-1:]:
            nums = list(reversed(nums))
        try:
            for number in nums:
                if int(number) - int(nums[nums.index(number)+1]) != -1:
                    result = int(nums[nums.index(number) + 1]), int(number)+1
                    break
        except:  # pylint: disable=W0702
            result = -1
    try:
        result = list(result)
    except:  # pylint: disable=W0702
        result = -1
    return result


if __name__ == "__main__":
    line = input()
    print(find_duplicate(line))
