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
# Global variable for incorrectly guessed letters
# Global variable for randomly chosen word
# Global variable for lives left
# Global variable for game over


def choose_random_word():
    """Will return a randomly selected word from our predefined list of acceptable words"""
    pass


def draw_word():
    """Will print out the word with dashes for letters that haven't been guessed yet"""
    pass


def draw_hangman():
    """Will print out the hangman drawing based on the number of lives left"""
    pass


def get_one_valid_letter():
    """Will make sure the user types only 1 letter that has not been used before"""
    pass


def guess_letter():
    """Will check if the 1 letter guessed is correct or wrong, and update global variables based on the result"""
    pass


def check_for_game_over():
    """Check to see if the player has won or lost"""
    pass


def main():
    """The entry point of the application, will call all the other methods in a game loop"""
    pass


if __name__ == '__main__':
    """Will only be called when you run the python program from the terminal or an IDE like PyCharms"""
    main()
