import sys
import copy
sys.setrecursionlimit(1500)

def binary_search(thing, arr):
    mid_point = len(arr)//2
    if mid_point == 0 and arr[mid_point] != thing:
        return False
    elif arr[mid_point] == thing:
        return True
    elif arr[mid_point] > thing:
        binary_search(thing, arr[:mid_point])
    else:
        binary_search(thing, arr[mid_point:])

def non_recursive_binary_search(thing, arr):
    mid = len(arr)//2
    array = copy.deepcopy(arr)
    found = False
    while not found:
        if array[mid] != thing and mid == 0:
            return found
        if array[mid] == thing:
            found = True
        elif array[mid] > thing:
            array = array[:mid]
            mid = len(array)//2
        else:
            array = array[mid:]
            mid = len(array)//2 
    return found



a = [1, 2, 3, 4, 5, 7, 7, 8, 9, 7, 8, 9, 10, 11, 12]
print len(a)
print non_recursive_binary_search(10, a)
print non_recursive_binary_search(6, a)
print binary_search(1, a)
print binary_search(6, a)

