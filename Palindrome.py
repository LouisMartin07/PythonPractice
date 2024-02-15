#Given an integer x, return true if x is a palindrome , and false otherwise.


def isPalindrome(x):
    x_str = str(x)
    if x_str[::-1] == x_str:
        print(True)
    else:
        print(False)


isPalindrome(-121)