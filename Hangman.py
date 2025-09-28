from random import choice

def run_game():
    word: str = choice(['apple','secret','banana'])

    username:str = input("Enter your name: ")
    print(f"Your name is {username}")

    #Setup
    guesses: str = ""
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                blanks += 1
        print()

        if blanks == 3:
            print('Sorry, the word was', word)
            break
        guess: str = input("Enter your guess: ")
        if guess in guesses:
            print(f'You guessed {guess}!')
            continue
        guesses += guess

        if guess not in word:
            tries -= 1
            print(f'Wrong guess! Tries left: {tries}')

            if tries == 0:
                print('Sorry, the word was', word)
                break

if __name__ == '__main__':
    run_game()
