import json

with open("inventory.json", "r") as file:
    inventory=json.load(file)

def check_item_in_inventory(item_name, inventory):
     if item_name in inventory:
            return True
     return False

def check_item_quantity(item_name, quantity, inventory):
    current_stock=inventory.get(item_name)
   
    if current_stock >= quantity :
        inventory[item_name]-=quantity
        with open('inventory.json','w') as file:
            json.dump(inventory,  file)
        return ( True, inventory[item_name]) 
    else:
        return ( False, inventory[item_name]) 
    