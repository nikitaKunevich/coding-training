# O(nd) time | O(n) space
def minNumberOfCoinsForChangeOne(n, denoms):
    results = [0]
    denoms.sort()
    for amount in range(1, n + 1):
        min_coins = float('inf')
        for denom in denoms:
            if amount < denom:
                break
            leftovers = amount - denom
            if results[leftovers] == float('inf'):
                continue
            coin_num = results[leftovers] + 1
            if coin_num < min_coins:
                min_coins = coin_num
        results.append(min_coins)
    return results[n] if results[n] != float('inf') else -1

###############################################################################
# O(n*d) time | O(n) space
def minNumberOfCoinsForChangeTwo(n, denoms):
    num_of_coins = [float('inf') for x in range(n+1)]
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if amount >= denom:
                num_of_coins[amount] = min(num_of_coins[amount], num_of_coins[amount - denom] + 1)
    return num_of_coins[n] if num_of_coins[n] != float('inf') else -1