def choose(nums):
	length = len(nums)
	for i in range(0,length-1):
		minindex = i
		for j in range(i+1, length):
			if nums[j] < nums[minindex]:
				minindex = j
		if minindex != i:
			nums[i], nums[minindex] = nums[minindex], nums[i]












if __name__ == '__main__':
	import random
	import numpy
	data = [random.randint(-100, 100) for _ in range(10)]
	choose(data)
	print(data)
