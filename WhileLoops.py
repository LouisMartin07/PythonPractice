# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 
print('Guessing game') 
guess = int(input('Please guess a number: '))
guess_number = 1

while  (guess) != 69 and guess_number < 10:
    if (guess) < 69 :
        guess = int(input('your guess was too low, please try again: '))
        guess_number += 1
    else :
        guess = int(input('Your number was too high, guess again: '))
        guess_number += 1

if guess == 69:
    print('Congratulations, you have guessed the correct number!')
else:
    print('Sorry, you did not guess the number in 10 tries.')


