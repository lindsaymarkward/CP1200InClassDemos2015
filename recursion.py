from symbol import return_stmt

__author__ = 'sci-lmw1'


def sumNumbersTo(n):
    if n <= 0:
        return 0
    return n + sumNumbersTo(n - 1);

print(sumNumbersTo(4))

# def main():
#     strings = ["", "a", "hannah", "bobby", "atoyotasatoyota"]
#     for string in strings:
#         print(string + ":", isPalindrome(string))
#
#
# def isPalindrome(string):
#     """
#     recursively check to see if a string is a palindrome (same forwards and backwards)
#     :param string: the string to check
#     :return: true or false
#     """
#     if len(string) <= 1:
#         return True
#     if string[0] != string[len(string) - 1]:
#         return False
#     return isPalindrome(string[1:len(string) - 1])
#
# main()