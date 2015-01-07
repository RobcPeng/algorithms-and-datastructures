'''
http://www.careercup.com/page?pid=google-interview-questions&sort=votes
You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists. 

For example, 
List 1: [4, 10, 15, 24, 26] 
List 2: [0, 9, 12, 20] 
List 3: [5, 18, 22, 30] 

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.'''

def problem(arr1, arr2, arr3):
    arr = [arr1[0], arr2[0], arr3[0]]
    smallest_range = max(arr) - min(arr)
    index1 = 0
    index2 = 0
    index3 = 0
    while True:
        if arr[0] == min(arr):
            index1 += 1
            if index1 >= len(arr1):
                break
            else:
                arr[0] = arr1[index1]
        elif arr[1] == min(arr):
            index2 += 1
            if index2 >= len(arr2):
                break
            else:
                arr[1] = arr2[index2]
        elif arr[2] == min(arr):
            index3 += 1
            if index3 >= len(arr3):
                break
            else:
                arr[2] = arr3[index3]
        if smallest_range > max(arr) - min(arr):
            smallest_range = max(arr) - min(arr)
    print arr
    return smallest_range
    
def main():
    list1 = [4, 10, 15, 24, 26]
    list2 = [0, 9, 12, 20]
    list3 = [5, 18, 22, 30]

    print problem(list1, list2, list3)

main()
