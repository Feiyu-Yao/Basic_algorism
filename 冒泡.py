def plingpling(nums):
	length = len(nums)
	for i in range(0,length):
		print(nums)
		for j in range(0,length-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]






if __name__ == '__main__':
	import random
	import numpy
	data = [random.randint(-100, 100) for _ in range(6)]
	plingpling(data)
	print(data)
