import sys

input = sys.stdin.readline
vowels = set('aeiou')

def has_vowel(word):
    return any(c in vowels for c in word)


def continuous_check(word):
    for i in range(len(word) - 2):
        chunk = word[i:i + 3]

        if all(c in vowels for c in chunk):
            return False

        if all(c not in vowels for c in chunk):
            return False

    return True


def two_continuous_check(word):
    for i in range(1, len(word)):
        if word[i] == word[i - 1] and word[i] not in 'eo':
            return False

    return True


while True:
    password = input().strip()

    if password == 'end':
        break

    if has_vowel(password) and continuous_check(password) and two_continuous_check(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')