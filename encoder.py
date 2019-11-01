import base64
from datetime import datetime

import keys

def generate_passwd(time_stamp):
    time_now = datetime.now()       #print(time_now, this is unformatted time)
    time_stamp = time_now.strftime("%Y%m%d%H%M%S")     #print(time_stamp, "this is formatted time")
    
    #Generate password by base64 encoding BusinessShortcode, Passkey and Timestamp.
    data_to_encode = keys.business_code + keys.passkey + time_stamp
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf-8') 
    
    return decoded_password