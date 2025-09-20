import json
import time 
import sys
from ui import messages, message_like_typing, message
from utils import sanitize_input_name, welcome_display, new_user_display, existing_user_display, sanitize_input_item
from inventory import inventory, check_item_in_inventory, check_item_quantity
from purchases import users_purchases, update_user_purchases, convert_user_purchases_to_string

choice=welcome_display()

while int(choice) <= 3:
    match choice:
        case "1":
            message_like_typing("To fetch your purchases we need your name please enter it : ")
            user_name=sanitize_input_name(input())
            if user_name=="":
                message_like_typing("name can't be empty \n")

            elif(user_name not in users_purchases):
                message_like_typing(f"Hello, {user_name}, you haven't visited our store yet ! \n")
                choice=new_user_display()
            else:
                data= users_purchases[user_name]
                if data=={}:
                    message_like_typing(f"Hello, {user_name}, you haven't made any purchases yet ! \n")
                    choice=existing_user_display()
                else:
                    message_like_typing("...fetching your purchases \n\n")
                    print(f"Here are all your purchases {user_name} : \n {convert_user_purchases_to_string(data)}")
                    time.sleep(1)
                    choice=existing_user_display()

        case "2":
            message_like_typing("Let start your purchase \n")
            name= input("please enter your name : ")
            if name=="":
                message_like_typing("name can't be empty \n")
                choice="2"
            else:
                name=sanitize_input_name(name)
                item=input("please enter the item you want to buy : ")
                item=sanitize_input_item(item)
                item_status=check_item_in_inventory(item, inventory)
                if(item_status==True):
                    message_like_typing("how many do you want to buy ? : ")
                    item_quantity= input()
                    status, quantity_left= check_item_quantity(item,item_quantity,inventory)
                    if(status==True):
                        update_user_purchases(name, item, item_quantity, users_purchases)
                        message_like_typing("you have purchased successfully \n Do you want to add more items ? (yes/no) : ")
                        continue_shopping=input().strip().lower()
                        if continue_shopping=='yes':
                            choice="2"
                        else:
                            message_like_typing("thank you for shopping with us \n")
                            sys.exit()
                    else:
                        message_like_typing("we don't have enough quantity for this item \nThe available quantity is : "+str(quantity_left)+"\n Do you want to continue shopping ? (yes/no) : ")
                        continue_shopping=input().strip().lower()
                        if continue_shopping=='yes':
                            choice="2"
                        else:
                            message_like_typing("thank you for shopping with us \n")
                            sys.exit()
               
                else:
                    print("item doesn't exist in inventory \n")
                    exit()

        case "3":
            print("thank you for visiting our store")
            
            sys.exit()

        case _:
            print("invalid action")
            exit()
