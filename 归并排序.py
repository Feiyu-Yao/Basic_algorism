def mergerank(nums):
    import math
    if len(nums) < 2:
        return nums
    middle = math.floor(len(nums)/2)
    left = nums[0:middle]
    right = nums[middle:]
    return merge(mergerank(left),mergerank(right))


def merge(left, right):
    result = []
    print(left, right)
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    print(result)
    return result














if __name__ == '__main__':
    import random
    import numpy
    data = [random.randint(-100, 100) for _ in range(6)]
    data = mergerank(data)
    print(data)