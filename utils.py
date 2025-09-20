from ui import messages, message

def sanitize_input_name(user_input):
    return user_input.strip().capitalize()

def sanitize_input_item(user_input):
    return user_input.strip().lower()

def welcome_display():
    message(messages['welcome'])
    message(messages['choose_action_question'])
    message(messages['show_purchases'])
    message(messages['make_purchase'])
    message(messages['exit'])
    message(messages['choose_action'])
    choose_action = input()
    return choose_action

def new_user_display():
    message(messages['choose_action_question'])
    message(messages['make_purchase'])
    message(messages['exit'])
    message(messages['choose_action'])
    choose_action = input()
    return choose_action

def existing_user_display():
    messages(messages['choose_action_question'])
    message(messages['show_purchases'])
    message(messages['make_purchase'])
    message(messages['exit'])
    message(messages['choose_action'])
    choose_action = input()
    return choose_action

