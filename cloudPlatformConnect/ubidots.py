import time
import requests
import random


deviceToken = ""  # Put your TOKEN here 
deviceLabel = ""  # Put your device label here. no spacebar 
VARIABLE_LABEL_1 = ""  # Put your first variable label here. no spacebar
VARIABLE_LABEL_2 = "" # Put your Second variable label here. no spacebar

val1=random.randrange(0,5) 
val2 = random.randrange(1,100)




def postRequestUbidots(devLabel,token,variable_1,variable_2,value_1,value_2):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, devLabel)
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    payload = {
            variable_1 : value_1,
            variable_2 : value_2,
    }
    print(payload)
    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        try:
            req = requests.post(url=url, headers=headers, json=payload)
            status = req.status_code
            req.raise_for_status()
            attempts += 1
            time.sleep(1)
        except requests.exceptions.RequestException as err:
            print(f"[ERROR] An error occurred: {err}")

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True



postRequestUbidots(deviceLabel,deviceToken,VARIABLE_LABEL_1,VARIABLE_LABEL_2,val1,val2)