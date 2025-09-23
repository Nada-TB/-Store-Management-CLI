from ui import messages, fetch_message
from exceptions import ChoiceInvalidError, EmptyNameError, IsNotAlphaError, EmptyItemError, ItemQuantityError
import sys 

choices=("1","2","3")

def sanitize_input_item(user_input):
    return user_input.strip().lower()

def sanitize_input_name(user_input):
    return user_input.strip().capitalize()

def get_choice_input(prompt):
    fetch_message(prompt, space_after="") 
    choice= input().strip()
    if choice not in choices:
        raise ChoiceInvalidError
    return choice

def get_name_input(prompt):
    fetch_message(prompt, space_after="")
    name=sanitize_input_name(input())
    if name.strip() =="":
        raise EmptyNameError
    elif name.isdigit():
        raise IsNotAlphaError
    return name

def get_input_item (prompt):
    fetch_message(prompt, space_after="")
    item= sanitize_input_item(input())
    if not item:
        raise EmptyItemError
    return item 

def get_item_quantity (prompt):
    fetch_message(prompt, space_after="")
    item_quantity= input().strip()
    if not item_quantity.isdigit():
        raise ItemQuantityError
    return item_quantity

def welcome_message_display():
    lines=messages['welcome'].rsplit("\n")
    for line in lines:
        fetch_message(line)

def get_valid_input(prompt, validation_function, error_messages):
    while True : 
        try:
            input_value=validation_function(prompt)
            break
        except tuple(error_messages.keys()) as e:   
            fetch_message(messages[type(e)])
    return input_value

def handle_exit():
    fetch_message("thank you for visiting our store")
    sys.exit(0)
   

