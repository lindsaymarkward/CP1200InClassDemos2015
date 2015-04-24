from symbol import return_stmt

__author__ = 'sci-lmw1'


def isPalindrome(string):
    if len(string) < 2:
        return True
    if string[0] != string[len(string) - 1]:
        return False
    return isPalindrome(string[1:len(string) - 1])

strings = ["", "a", "hannah", "bobby", "atoyotasatoyota"]

for string in strings:
    print(isPalindrome(string))