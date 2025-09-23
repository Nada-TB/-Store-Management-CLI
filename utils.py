from ui import messages, fetch_message
from exceptions import ChoiceInvalidError, EmptyNameError, IsNotAlphaError, EmptyItemError, ItemQuantityError

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
    if item =="":
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
   
'''''
def new_user_options_display():
    messages=[
        messages['choose_action_question'],
        messages['make_purchase'],
        messages['exit'],
        messages['choose_action']
    ]
    for message in messages :
        fetch_message(message) 
   

def existing_user_options_display():
    fetch_message(messages['choose_action_question'])
    fetch_message(messages['show_purchases'])
    fetch_message(messages['make_purchase'])
    fetch_message(messages['exit'])
    fetch_message(messages['choose_action'])
   
'''
