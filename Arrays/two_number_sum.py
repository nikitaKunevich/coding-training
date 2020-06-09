# O(n^2) time | O(1) space
def twoNumberSumOne(array, targetSum):
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i]+array[j] == targetSum:
				return [array[i],array[j]]
	return []

# O(n) time | O(n) space
def twoNumberSumTwo(array, targetSum):
	potentialNums = {}
	for i in array:
		diff = targetSum - i
		if diff in potentialNums:
			return[diff, i]
		else:
			potentialNums[i]=i
	return []

# O(n*log(n)) time | O(1) space
def twoNumberSumThree(array, targetSum):
	l, r = 0,len(array)-1
	array.sort()
	while l < r:
		res = array[l] + array[r]
		if res == targetSum:
			return [array[l],array[r]]
		elif res < targetSum:
			l +=1
		else:
			r -=1
	return []