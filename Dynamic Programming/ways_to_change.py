'''
Return number of ways to change the amount {n} with coin denominations: {denom}
'''

# O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
	return buildChangeWaysArray(n, denoms)[n]

def buildChangeWaysArray(n, denoms):
	ways_to_change = [0 for _ in range(n+1)]
	ways_to_change[0] = 1
	for denom in denoms:
		for i in range(1, n+1):
			rem = i - denom
			if rem >= 0:
				ways_to_change[i] += ways_to_change[rem]
	return ways_to_change