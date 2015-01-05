# Given an array of object A, and an array of object B. All A's have 
# different sizes, and all B's have different sizes. Any object A is of the 
# same size as exactly one object B. We have a function f(A, B) to compare the 
# size of one A and one B. But we cannot compare between two A's or two B's. 
# Give an algorithm to match each A with each B.
import random

arrayA = []
arrayB = []

def nuts_and_bolts(A, B):
	if len(A) >= len(B):
		print ('There are not enough of object b')
	else:
		startNumber = len(A)
		smallA = []
		bigA = []
		smallB = []
		bigB = []
		matchs = []
		for idx, objs in enumerate(B):
			if A[startNumber] > B:
				smallB.append(B)
			elif A[startNumber] < B:
				bigB.append(B)
			else:
				matchs.append(, B])



def object_size_match(A,B):
	matches = []
	for idxB, objB in enumerate(B):
		for idxA objA in enumerate(A):
			if len(objA) == len(objB): #f(x, y)
				matches.append([idxA, idxB])
	return matches






