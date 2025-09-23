import json
import time

with open("users_purchases.json", "r") as file:
    users_purchases=json.load(file)

def convert_user_purchases_to_string(user_purchases):
    output=[]
    for i, item in enumerate(user_purchases, start=1):
          output.append(f'{i}. {item} :')
          output.append("")
          output.append(f"{'Date':12}| {'Quantity':>8}")
          output.append("-" * 23)
          for purchase in user_purchases[item]:
                output.append(f'{purchase["date"]:11} | {purchase["quantity"]:>3}') 
          output.append("-" * 23) 
          output.append("")    
    return ('\n').join(output)
''''
def convert_users_purchases_to_string(all_users_data):
     for name in all_users_data:
       print(f"{name.capitalize()}'s purchases: \n", end="") 
       print("====================\n", end="") 
       if all_users_data[name]=={}:
                print("no purchases yet \n")
       else:
         convert_user_purchases_to_string(all_users_data[name])
'''
def update_user_purchases(name, item, quantity, users_purchases):
    if name not in users_purchases:
        users_purchases[name]={}
    
    data={'date':time.strftime("%Y-%m-%d"), 'quantity':quantity}
    if item in users_purchases[name]:
        users_purchases[name][item].append(data)
    else:
        users_purchases[name][item]=[data]
    
    with open('users_purchases.json', 'w') as file:
        json.dump(users_purchases, file)