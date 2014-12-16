def MergeSort(List):
	if len(list) == 1:
		return List
	else:
		LeftList = MergeSort(List[:len(List)//2]) #splits the list in half
		RightList = MergeSort(List[len(List)//2:])
		LeftCounter = 0
		RightCounter = 0
		WholeCounter = 0

