from handlers import handle_show_purchases, handle_make_purchase, handle_exit
from ui import messages, fetch_message

dispatch_map = {
    '1': handle_show_purchases,
    '2': handle_make_purchase,
    '3': handle_exit
}

def dispatch(option,context):
    handler = dispatch_map.get(option)
    if handler:  
        handler(context)
    else:
        fetch_message("Invalid option selected.")