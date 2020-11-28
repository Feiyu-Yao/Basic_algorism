

def quick(nums, left, right):
	if left < right:
		indexmid = patrition(nums, left, right)
		quick(nums,left, indexmid-1)
		quick(nums,indexmid+1, right)


def patrition(nums, left, right):
	pivot = left
	index = pivot +1
	i =index
	while i <= right:
		if nums[i] < nums[pivot]:
			sweep(nums, index, i)
			index += 1
		i += 1
	sweep(nums, pivot, index-1)
	print(nums)
	return index-1





def sweep(nums, a, b):
	nums[a], nums[b] = nums[b], nums[a]







if __name__ == '__main__':
	import random
	data = [random.randint(-100, 100) for _ in range(6)]
	#data = [0,-1,2,-3,4,-5,6]
	print(data)
	quick(data, 0, len(data) - 1)
	print(data)
