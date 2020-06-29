from collections import Counter
# O(w^2 * n) time | O(w*n) space - dict solution ?

def groupAnagramsCounter(words):
    groups = []
    group_dicts = []
    for w in words:
        char_table = Counter(w)
        grouped = False
        for i in range(len(groups)):
            if char_table == group_dicts[i]:
                groups[i].append(w)
                grouped = True
        if not grouped:
            groups.append([w])
            group_dicts.append(char_table)
    return groups


# w - num of words, n - len of longest word
# O(w*nlog(n)) time | O(w*n == c) space
def groupAnagramsSort(words):
    groups = {}
    for w in words:
        w_sorted = ''.join(sorted(w))
        if w_sorted in groups:
            groups[w_sorted].append(w)
        else:
            groups[w_sorted] = [w]
    return list(groups.values())



