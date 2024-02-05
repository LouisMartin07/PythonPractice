def is_armstrong_number(n):

    digits = str(n)
    num_digits = len(digits)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    return sum_of_powers == n

test_numbers = [1, 2, 5, 153, 370, 371, 407, 9474]

