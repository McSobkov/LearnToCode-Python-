import math
import string

def sphere_volume(radius):
    return 4 * math.pi * radius**3 / 3


print(sphere_volume(2))  # should be approximately 33.49333...


def ran_check(num, low, high):
    return low <= num <= high


print(ran_check(5, 2, 7))


def up_low(s):
    count_upper = 0
    count_lower = 0
    for x in range(0, len(s)):
        if s[x].isupper():
            count_upper += 1
        elif s[x].islower():
            count_lower += 1
    print(f"No. of Upper case characters : {count_upper}\nNo.of Lower case characters : {count_lower}")


up_low("hOW manY aRE tHErE")


def unique_list(lst):
    return set(lst)


print(unique_list([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6]))


def multiply(s):
    total = 1
    for item in s:
        total *= item
    return total


print(multiply([1, 2, 3, -4]))


def palindrome(s):
    s2 = s[::-1]
    return s2 == s


print(palindrome ("racecar"))
print(palindrome("why isn't a palindrome a palindrome"))


def ispangram(str1, alphabet = string.ascii_lowercase):
    for x in range(0,26):
        if str1.find(alphabet[x]) == -1:
            return False
    return True


print(ispangram("The quick brown fox jumps over the lazy dog"))
