import random
import sys
import time

"""
    -------QUIZLET-------
    How it will work:
    1. On application start it will load flash cards from text file and present menu options
    2. You can add/update a flash card
    3. You can delete a flash card
    4. You can save flash cards to text file
    5. You can study flash cards
    6. You can be quizzed on flash cards
"""

# Global variable for flash cards
flash_cards = {}


def read_flash_cards_from_text_file():
    """Will read line by line the card name and definition from a local txt file"""
    global flash_cards

    pass


def update_flash_cards(card_name, new_definition, save_to_file=True, delete_flash_card=False):
    """Will be called whenever adding or deleting or replacing a flash card"""
    global flash_cards

    pass


def write_flash_cards_to_text_file():
    """Will line by line write the name and definition for each flash card to a file for saving"""
    global flash_cards

    pass


def add_flash_card():
    """Will be called from main menu to create or update flash card"""

    pass


def remove_flashcard():
    """Will be called from main menu to delete a flash card"""
    global flash_cards

    pass


def study_flash_cards():
    """Will launch the study mode of Quizlet to let you learn the flash card definitions"""
    global flash_cards

    pass


def get_valid_int_input():
    """Will return a number 1-4 or -1 to Exit program"""

    pass


def get_random_choices(answer, definitions):
    """Will return a randomly shuffled list of choices for the quiz mode"""
    global flash_cards

    pass


def take_quiz():
    """Will be called from main menu to launch quiz mode of Quizlet"""
    global flash_cards

    pass


def print_menu():
    """Prints menu options to select from"""
    menu = """
    1. Add/update a flash card
    2. Delete a flash card
    3. Save flash cards to text file
    4. Study flash cards
    5. Be quizzed on flash cards
    6. Exit Quizlet
    """

    pass


def get_valid_menu_input():
    """Will return valid number 1-6"""

    pass


def main():
    """Main entry point of Quizlet, allows menu item selections"""
    global flash_cards

    pass


if __name__ == '__main__':
    main()
