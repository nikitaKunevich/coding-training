LATIN_START = ord('a')
LATIN_END = ord('z')
LATIN_ALPHABET_LENGTH = LATIN_END - LATIN_START + 1
# 23,24,25
# O(n) time | O(n) space
def shiftletter(letter, key):
    letter_idx = ord(letter) - LATIN_START
    shifted_idx = (letter_idx + key) % (LATIN_ALPHABET_LENGTH)
    return chr(shifted_idx + LATIN_START)

def caesarCipherEncryptor(string, key):
    return ''.join([shiftletter(l, key) for l in string])
