from handlers import handle_show_purchases, handle_make_purchase
from ui import messages, fetch_message

dispatch_map = {
    '1': handle_show_purchases,
    '2': handle_make_purchase,
}

def dispatch(option,context):
    handler = dispatch_map.get(option)
    if handler:  
        handler(context)
   