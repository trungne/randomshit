import random
randomNumber = random.randint(0,10)
print('A random number between 0 and 10 (including 0 and 10) has been selected for you. You must guess what it is in 5 guesses')
NumberOfGuess = 0
while True:
    if NumberOfGuess < 5:
        YourGuess = input('Enter your guess: ')
        try:
            YourGuess = int(YourGuess)
        except:
            print('You must enter a number!')
            continue
        if YourGuess > 10 or YourGuess < 0:
            print('The random number should be between 0 and 10')
            continue
        elif YourGuess == randomNumber:
            print('Congratulations! The number is '+ str(YourGuess))
            break
        else:
            print('Nope!')
            NumberOfGuess = NumberOfGuess +1
    else: print ('You lose, the number is' + str(randomNumber))