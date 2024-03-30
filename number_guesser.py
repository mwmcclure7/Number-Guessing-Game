from random import randint


def play_game():
    minimum = 0
    maximum = 0
    max_loop = True
    while max_loop:
        maximum = int(input('What do you want the highest possible value of this number to be? > '))
        if maximum < minimum:
            print('You cannot input a negative number.')
        elif maximum >= minimum:
            max_loop = False
        else:
            print('Type a number!')
    maximum_typed = maximum
    minimum_typed = minimum
    number = randint(minimum, maximum)
    win = False
    guesses = 0
    less_than = 'or equal to '
    greater_than = 'or equal to '

    def printing():
        print(f'The number is greater than {greater_than}{minimum_typed} and less than {less_than}{maximum_typed}.')

    while not win:
        guesses += 1
        guess = int(input(f'Guess {guesses} > '))
        if guess > number:
            if guess <= maximum_typed:
                maximum_typed = guess
                less_than = ''
            printing()
        elif guess < number:
            if guess >= minimum_typed:
                minimum_typed = guess
                greater_than = ''
            printing()
        elif guess == number:
            print(f'You guessed the number in {guesses} guesses!')
            win = True
        else:
            print(f'"{guess} is not understood.')


play_again = True
while play_again:
    play_game()
    play_again_question_loop = True
    while play_again_question_loop:
        play_again_question = input('Would you like to play again? (Type YES or NO) > ').upper()
        if play_again_question == 'YES':
            print('Okay')
            play_again_question_loop = False
        elif play_again_question == 'NO':
            print('Okay, goodbye!')
            play_again = False
            play_again_question_loop = False
        else:
            print(f'"{play_again_question}" is not understood, please try again.')
