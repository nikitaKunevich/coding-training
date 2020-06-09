# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seq_pointer = 0
    array_pointer = 0
    while array_pointer < len(array):
        if array[array_pointer] == sequence[seq_pointer]:
            seq_pointer += 1
            if seq_pointer == len(sequence):
                break
        array_pointer += 1
    return seq_pointer == len(sequence)