from ui import fetch_message
from purchases import users_purchases, convert_user_purchases_to_string, update_user_purchases
from inventory import check_item_in_inventory,inventory, check_item_quantity
import sys

def handle_show_purchases(context):
    if context.get('user_name') not in users_purchases:
        fetch_message(f"Dear {context.get('user_name')}, you haven't visited our store yet ! your have 0 purchase \n")
    else: 
        user_purchases= convert_user_purchases_to_string(users_purchases[context.get('user_name')])
        fetch_message("Showing all purchases...")
        if not user_purchases:
            fetch_message("You haven’t made any purchases yet. Start shopping to see your items here!")
        else: 
            fetch_message(f"Here are all your purchases {context.get('user_name')} : \n {user_purchases}")

def handle_make_purchase(context):
    fetch_message("Making a new purchase...")
    item_status=check_item_in_inventory(context.get('item_name'), inventory)
   
    if(item_status):
         status,quantity_left=check_item_quantity(context.get('item_name'), context.get('item_quantity'), inventory) 
         if status :
            update_user_purchases(context.get('user_name'),context.get('item_name'),context.get('item_quantity'), users_purchases)
            fetch_message("you have purchased successfully \nDo you want to add more items ? (yes/no) : ")
         else:
            fetch_message(f"we don't have enough quantity for this item \nThe available quantity is : {str(quantity_left)} \n Do you want to continue shopping ? (yes/no) : ")
    else:
        fetch_message("Sorry, the item you entered is not available in our store.\nDo you want to continue shopping ? (yes/no) : ")

