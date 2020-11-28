
def shellrank(nums):
    import math
    gap = 1
    while gap< (len(nums)/3):
        gap = 3 * gap + 1
    while gap > 0:
        for i in range(gap, len(nums)):
            current = nums[i]
            pivot = i - gap
            while pivot >= 0 and nums[pivot] > current:
                nums[pivot+gap] = nums[pivot]
                pivot -= gap
            nums[pivot+gap] = current
        gap = math.floor(gap/3)

















if __name__ == '__main__':
    import random
    import numpy
    data = [random.randint(-100, 100) for _ in range(6)]
    shellrank(data)
    print(data)