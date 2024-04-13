#Given an integer x, return true if x is a palindrome , and false otherwise.


def isPalindrome(x):
    x_str = str(x)
    if x_str[::-1] == x_str:
        print(True)
    else:
        print(False)


isPalindrome(121)

# done recursively 
def is_palindrome(x):
    if len(x) <= 1:
        print(True)
    else:
        # s[0] == s[-1] verifies first and lest letter are the same with each loop
        # [1:-1] slices the first and last off with each loop
        return x[0] == x[-1] and is_palindrome(x[1:-1])
    
is_palindrome('racecar')