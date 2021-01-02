import random
import time

"""
    -------HANGMAN-------
    How it will work:
    1. A random word will be chosen from our list of hangman words.
    2. The player will have 6 lives, as in if the player
        chooses 6 incorrect letters he loses.
    3. The player can only guess one letter at a time
    4. Before every guess the player can see the letters
        he has guessed incorrectly
    5. Before every guess a hangman drawing will be displayed
        based on the number of lives left
    6. If all letters in the randomly chosen word were guessed
        before the lives are over, it will display a you win message
    7. If all lives are over, it will display a you lose message
"""

# Global variable for correctly guessed letters
correctly_guessed_letters = []

# Global variable for incorrectly guessed letters
incorrectly_guessed_letters = []

# Global variable for randomly chosen word
randomly_chosen_word = ""

# Global variable for lives left
lives_left = 6

# Global variable for game over
game_over = False


def choose_random_word():
    """Will return a randomly selected word from our predefined list of acceptable words"""
    global randomly_chosen_word

    acceptable_words = [
        "Abruptly",
        "Axiom",
        "Bagpipes",
        "Blizzard",
        "Croquet",
        "Flapjack"
    ]

    random.seed(time.time())
    randomly_chosen_word = random.choice(acceptable_words)
    randomly_chosen_word = randomly_chosen_word.lower()


def draw_word():
    global correctly_guessed_letters
    global randomly_chosen_word

    for i in range(0, len(randomly_chosen_word)):
        letter = randomly_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")


def draw_hangman():
    """Will print out the hangman drawing based on the number of lives left"""
    global lives_left

    if lives_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")


def get_one_valid_letter():
    """Will make sure the user types only 1 letter that has not been used before"""
    is_letter_valid = False
    letter = ""
    while is_letter_valid is False:
        letter = input("Enter guess letter: ")
        letter = letter.strip().lower()
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be of length 1")
        else:
            if letter.isalpha():
                if letter in correctly_guessed_letters or letter in incorrectly_guessed_letters:
                    print("You have already guessed the letter " + letter + ", please try again")
                else:
                    is_letter_valid = True
            else:
                print("Letter must be (a-z)")

    return letter


def guess_letter():
    """Will check if the 1 letter guessed is correct or wrong, and update global variables based on the result"""
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global lives_left

    letter = get_one_valid_letter()
    if letter in randomly_chosen_word:
        correctly_guessed_letters.append(letter)
    else:
        incorrectly_guessed_letters.append(letter)
        lives_left -= 1


def check_for_game_over():
    """Check to see if the player has won or lost"""
    global lives_left
    global game_over
    global correctly_guessed_letters

    if lives_left <= 0:
        game_over = True
        draw_hangman()
        print("You lost! The word was " + randomly_chosen_word + ". Try again next time!")
    else:
        guessed_all_letters = True
        for letter in randomly_chosen_word:
            if letter not in correctly_guessed_letters:
                guessed_all_letters = False
                break
        if guessed_all_letters:
            game_over = True
            print("You won! Congrats, and feel free to play again!")


def main():
    """The entry point of the application, will call all the other methods in a game loop"""
    global game_over

    print("-----Welcome to Hangman----")
    choose_random_word()

    while game_over is False:
        draw_hangman()
        draw_word()

        if len(incorrectly_guessed_letters) > 0:
            print("Incorrect guesses: ")
            print(incorrectly_guessed_letters)

        guess_letter()
        check_for_game_over()


if __name__ == '__main__':
    """Will only be called when you run the python program from the terminal or an IDE like PyCharms"""
    main()
