import time
import sys

messages={
    'welcome':(
        "welcome to our store \n"
        'what do you want to do ? \n\n'
        "1.show all purchases \n"
        "2.make new purchase \n"
        "3.exit \n"),
    'choose_action':"Enter the number of action you want to do : ",
    'get_name':"please enter your name : ",
    'error_name_empty':"name can't be empty \n",
    'error_name_notAlpha':"The name must contain only letters.",
    'get_item':"please enter the item you want to buy : ",
    'error_item_empty':'You did not enter anything. Please provide a valid item.',
    'get_quantity':"how many do you want to buy ? : ",
    'error_quantity_not_digit': "Invalid input! Quantity must be a number. Please enter digits only.",
    'invalid_choice':"Invalid choice. Please try again.\n",
    'choices_allowed': (
        "Invalid choice. Please choose one of the following options:\n"
        "1. show all purchases \n"
        "2. make new purchase\n"
        "3. Exit the program"
    ),

    'action_after_finishing_purchase': (
        "You have finished shopping. What would you like to do next?\n"
        "1 - Show my purchases\n"
        "3 - Exit\n"
    ),
    'action_after_showing_purchases': (
        "What would you like to do next?\n"
        "2. make new purchase\n"
        "3. Exit the program"
    ),
    'choices':(
        "What would you like to do next?\n"
        "1. show all purchases \n"
        "2. make new purchase\n"
        "3. Exit the program"
    )

}

def message_like_typing(message, time_per_char=0.05, file=None):
    if file is None:
        file = sys.stdout
    for char in message:
        print(char, end="", file=file, flush=True)
        time.sleep(time_per_char)


def fetch_message(message, delay_after=0.2,space_after="\n"):
    message_like_typing(message)
    time.sleep(delay_after)
    print(end=space_after)  # Print a newline after the message