def quick_sort(nums: list, left: int, right: int):
	if left < right:
		i = left
		j = right
		pivot = nums[left]
		while i != j:
			while j > i and nums[j] > pivot:
				j -=1
			if j > i:
				nums[j] = nums[i]
				i += 1
			while i < j and nums[i] < pivot:
				i += 1
			if i < j:
				nums[j] = nums[i]
				j -=1

		nums[i]=pivot
		quick_sort(nums, left, i-1)
		quick_sort(nums, i+1, right)



if __name__ == '__main__':
	import random
	data = [random.randint(-100, 100) for _ in range(6)]
	quick_sort(data, 0, len(data) - 1)
	print(data)




