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

    with open("./flash_cards.txt", "r") as f:
        for line in f:
            line = line.strip()
            split_index = line.index("=")
            card_name = line[0: split_index].strip()
            definition = line[split_index + 1: len(line)].strip()
            flash_cards[card_name] = definition

    if len(flash_cards) < 4:
        print("You must have at least 4 flash cards in text file before starting Quizlet, exiting program now")
        sys.exit()


def update_flash_cards(card_name, new_definition, save_to_file=True, delete_flash_card=False):
    """Will be called whenever adding or deleting or replacing a flash card"""
    global flash_cards

    if delete_flash_card:
        del flash_cards[card_name]
    else:
        flash_cards[card_name] = new_definition

    if save_to_file:
        write_flash_cards_to_text_file()


def write_flash_cards_to_text_file():
    """Will line by line write the name and definition for each flash card to a file for saving"""
    global flash_cards

    if len(flash_cards) < 4:
        print("Error: You must have at least 4 flash cards before saving to file")
        return

    # https://www.geeksforgeeks.org/reading-writing-text-files-python/
    #
    with open("./flash_cards.txt", "w+") as f:
        for key, value in flash_cards.items():
            f.write(key + "=" + value + "\n")


def add_flash_card():
    """Will be called from main menu to create or update flash card"""
    card_name = input("Enter Card Name: ")
    definition = input("Enter Card Definition: ")
    save_to_file = input("Save To File (Y/N)?: ").lower()

    if save_to_file == 'y':
        save_to_file = True
    else:
        save_to_file = False

    update_flash_cards(card_name, definition, save_to_file)


def remove_flashcard():
    """Will be called from main menu to delete a flash card"""
    global flash_cards
    card_name = input("Enter Card Name: ")
    save_to_file = input("Save To File: Y/N?").lower() == 'y'
    if card_name not in flash_cards:
        print("Error: Card name " + card_name + " not in flash cards")
    else:
        update_flash_cards(card_name, "", save_to_file=save_to_file, delete_flash_card=True)


def study_flash_cards():
    """Will launch the study mode of Quizlet to let you learn the flash card definitions"""
    global flash_cards

    for card, definition in flash_cards.items():
        print("Card: " + card)
        print("Definition: " + definition)
        exit_study = input(
            "Press Enter when you are ready to move to the next flash card, type Q to quit").lower() == 'q'
        if exit_study:
            break
        print("-----------------------")
    print("")
    print("All flash cards are complete")
    print("-----------------------")


def get_valid_int_input():
    """Will return a number 1-4 or -1 to Exit program"""
    is_valid = False
    answer = -1
    while not is_valid:
        answer = input("Enter 1-4, or Q to quit: ").lower()
        if answer.isnumeric():
            answer = int(answer)
            if 1 <= answer <= 4:
                is_valid = True
            else:
                print("Error: Please enter number 1-4")
        else:
            if answer == 'q':
                answer = -1
                is_valid = True
            else:
                print("Error: Please enter number 1-4")
    return answer


def get_random_choices(answer, definitions):
    """Will return a randomly shuffled list of choices for the quiz mode"""
    global flash_cards

    answers = [answer]

    while len(answers) < 4:
        random_definition = random.choice(definitions)
        if random_definition not in answers:
            answers.append(random_definition)

    random.shuffle(answers)

    return answers


def take_quiz():
    """Will be called from main menu to launch quiz mode of Quizlet"""
    global flash_cards

    if len(flash_cards) < 4:
        print("Not enough flash cards to quiz with, add some more cards")
        return

    card_names = list(flash_cards.keys())
    definitions = list(flash_cards.values())

    random.shuffle(card_names)
    random.shuffle(definitions)

    score = 0

    for card_name in card_names:
        print("What is the definition for " + card_name)
        answer_choices = get_random_choices(flash_cards[card_name], definitions)

        for i in range(len(answer_choices)):
            print(str(i + 1) + ") " + answer_choices[i])

        answer = get_valid_int_input() - 1

        if answer == -2:
            print("Exiting Quiz")
            print("")
            break

        print("")

        if answer_choices[answer] == flash_cards[card_name]:
            print("You chose the correct answer!")
            score += 1
            print("+1 Point")
        else:
            print("Sorry, the correct answer was")
            print(card_name + " - " + flash_cards[card_name])
        print("----------------")
        print("")

    print("Quiz is complete")
    print("Your total score was " + str(score) + "/" + str(len(flash_cards)))


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
    print(menu)


def get_valid_menu_input():
    """Will return valid number 1-6"""
    is_valid = False
    answer = -1
    while not is_valid:
        answer = input("Enter 1-6: ").lower()
        if answer.isnumeric():
            answer = int(answer)
            if 1 <= answer <= 6:
                is_valid = True
            else:
                print("Error: Please enter number 1-6")
        else:
            print("Error: Please enter number 1-6")
    return answer


def main():
    """Main entry point of Quizlet, allows menu item selections"""
    global flash_cards

    random.seed(time.time())
    read_flash_cards_from_text_file()

    run_loop = True

    print("--------Welcome to Quizlet--------")

    while run_loop:
        print_menu()
        option = get_valid_menu_input()
        if option == 1:
            add_flash_card()
        elif option == 2:
            remove_flashcard()
        elif option == 3:
            write_flash_cards_to_text_file()
        elif option == 4:
            study_flash_cards()
        elif option == 5:
            take_quiz()
        elif option == 6:
            run_loop = False

    print("Thanks for using Quizlet!")


if __name__ == '__main__':
    main()
