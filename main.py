from ui import messages, fetch_message
from utils import welcome_message_display, get_choice_input, get_name_input, choices, get_input_item, get_item_quantity
import dispatcher
from exceptions import ChoiceInvalidError, EmptyNameError,IsNotAlphaError, ItemQuantityError

context = {
    "user_name": None,
    "item_name": None,
    "item_quantity": 0
}

continue_shopping= True
choice= 0

welcome_message_display()

while True:   
    try:
        choice=get_choice_input(messages['choose_action'])
        break
    except ChoiceInvalidError:
        fetch_message(messages['choices_allowed'])

while choice in ("1", "2"):
    try:
        user_name=get_name_input(messages['get_name'])
        context['user_name']= user_name
        break
    except EmptyNameError:
        fetch_message(messages['error_name_empty'])
    except IsNotAlphaError:
        fetch_message(messages['error_name_notAlpha'])

if choice !="3" :  
    fetch_message(f"Hello, {user_name}! You chose option {choices[int(choice)-1]}. Let's proceed.\n")

if choice =="2":
        try: 
            item_name= get_input_item(messages['get_item'])
            context['item_name']=item_name
        except EmptyNameError:
            fetch_message(messages['item_error'])
        try:
            item_quantity= get_item_quantity(messages['get_quantity'])
            
            context['item_quantity']=int(item_quantity)
        except ItemQuantityError :
            fetch_message(messages ['error_quantity_not_digit'])


dispatcher.dispatch(choice,context)









