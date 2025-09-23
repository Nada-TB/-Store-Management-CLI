from ui import messages, fetch_message
from utils import welcome_message_display, get_choice_input, get_name_input, choices, get_input_item, get_item_quantity, handle_exit, get_valid_input
import dispatcher
from exceptions import ChoiceInvalidError, EmptyNameError,IsNotAlphaError, ItemQuantityError, EmptyItemError

context = {
    "user_name": None,
    "item_name": None,
    "item_quantity": 0
}

continue_shopping= False
choice= 0

welcome_message_display()

while choice !="3" :
    if not continue_shopping : 
        while True : 
            try:
                choice=get_choice_input(messages['choose_action'])
                break
            except ChoiceInvalidError:   
                fetch_message(messages['choices_allowed'])

    if choice =="3":
         break 
    
    if not context.get('user_name'):
        while True:
            try:
                user_name=get_name_input(messages['get_name'])
                context['user_name']= user_name  
                break    
            except EmptyNameError:
                fetch_message(messages['error_name_empty'])
            except IsNotAlphaError:
                fetch_message(messages['error_name_notAlpha'])
        fetch_message(f"Hello, {user_name}! You chose option {choice}. Let's proceed.\n")  
        

    if choice =="2":
        while True:
            try: 
                item_name= get_input_item(messages['get_item'])
                context['item_name']=item_name
                break
            except EmptyItemError:
                fetch_message(messages['error_item_empty'])

        while True:
            try:
                item_quantity= get_item_quantity(messages['get_quantity'])
                context['item_quantity']=int(item_quantity)
                break
            except ItemQuantityError :
                fetch_message(messages ['error_quantity_not_digit'])
                    
        
    dispatcher.dispatch(choice,context)
    if choice =="1":
        fetch_message(messages['action_after_showing_purchases'])
    else :
        answer=input().strip().lower()
        continue_shopping= answer =="yes"
        if not continue_shopping :
             fetch_message(messages['action_after_finishing_purchase'])

handle_exit()







