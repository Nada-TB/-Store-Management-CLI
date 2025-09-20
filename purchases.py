import json
import time

with open("users_purchases.json", "r") as file:
    users_purchases=json.load(file)

def update_user_purchases(name, item, quantity, users_purchases):
    name=name.capitalize().strip()
    if name not in users_purchases:
        users_purchases[name]={}
    item=item.lower().strip()
    quantity=int(quantity)
    data={'date':time.strftime("%Y-%m-%d"), 'quantity':quantity}
    if item in users_purchases[name]:
        users_purchases[name][item].append(data)
    else:
        users_purchases[name][item]=[data]
    
    with open('users_purchases.json', 'w') as file:
        json.dump(users_purchases, file)

def convert_user_purchases_to_string(user_data):
    output=""
    for i, item in enumerate(user_data, start=1):
          output+=f'{i}.{item} : \n'
          output+=" Date       | Quantity \n"
          output+=" --------------------- \n"
          for data in user_data[item]:
                output+=f' {data["date"]} | {data["quantity"]}  \n'
                output+='--------------------- \n'
                output+="\n"
    return output

def convert_users_purchases_to_string(all_users_data):
     for name in all_users_data:
       print(f"{name.capitalize()}'s purchases: \n", end="") 
       print("====================\n", end="") 
       if all_users_data[name]=={}:
                print("no purchases yet \n")
       else:
         convert_user_purchases_to_string(all_users_data[name])