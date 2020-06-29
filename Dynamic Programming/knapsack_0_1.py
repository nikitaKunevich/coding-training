# O(n*c) time | O(n*c) space
def knapsackProblem(items, capacity):
    dp_arr = [[[0,[]] for _ in range(capacity + 1)] for _ in range(len(items))]
    for w in range(1,capacity + 1):
        for i in range(len(items)):
            if w < items[i][1]: #can't take the item
                if i > 0:
                    dp_arr[i][w] = dp_arr[i-1][w].copy()
                continue
            if i > 0:
                new_weight = w - items[i][1]
                prev_solution = dp_arr[i-1][w]
                remainder_solution = dp_arr[i-1][new_weight]
                if prev_solution[0] > remainder_solution[0] + items[i][0]:
                    dp_arr[i][w] = dp_arr[i-1][w].copy()
                else:
                    dp_arr[i][w][0] = items[i][0] + remainder_solution[0]
                    dp_arr[i][w][1].extend([i, *remainder_solution[1]])
            else:
                dp_arr[i][w][0] = items[i][0]
                dp_arr[i][w][1].append(i)
    return dp_arr[-1][-1]
                
assert knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10) == [10, [1, 3]]