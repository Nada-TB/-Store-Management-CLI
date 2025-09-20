import time
messages={
    'welcome':"welcome to our store \n",
    'choose_action_question':'what do you want to do ? \n',
    'show_purchases':"1.show all purchases \n",
    'make_purchase':"2.make new purchase \n",
    'exit':"3.exit \n",
    'choose_action':"press the number of action you want to do : ",
}

def message_like_typing(message):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.1)
        
def message(message):
    message_like_typing(message)
    time.sleep(0.5)