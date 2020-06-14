# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
    dp_matrix = []
    for y in range(len(str2) + 1):
        dp_matrix.append([])
        for x in range(len(str1) + 1):
            new_val = 0
            if y == 0:
                new_val = x
            elif x == 0:
                new_val = y
            else:
                if str1[x-1] == str2[y-1]:
                    new_val = dp_matrix[y-1][x-1]
                else:
                    new_val = min(dp_matrix[y-1][x], dp_matrix[y-1][x-1], dp_matrix[y][x-1])+1				
            dp_matrix[y].append(new_val)
    print(dp_matrix)
    return dp_matrix[len(str2)][len(str1)]