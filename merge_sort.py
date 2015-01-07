def merge(arr1,arr2):
	arr1_counter = 0
	arr2_counter = 0
	total_size = len(arr1) + len(arr2)
	sorted_array = []
	for i in range(0,total_size):
		if len(arr1) < arr1_counter
		if arr1[arr1_counter]  >= arr2[arr2_counter]:
			sorted_array.append(arr1[arr1_counter])
			arr1_counter += 1
		else:
			sorted_array.append(arr2[arr2_counter])
			arr2_counter += 1
	return sorted_array

def merge_sort(arr):
	right_counter = 0
	left_counter = 0
	middle = len(arr)//2
	right_array = arr[middle:]
	left_array = arr[:middle]
	if len(arr) > 1:
		merge(merge_sort(left_array),merge_sort(right_array))



a = [10,9,8,7,6,5,4]
b = [10,9,8,7,6,5,4]

print (merge(a,b))

