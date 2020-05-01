##import tweepy
####twurl -H api.twitter.com -A "Content-Type: application/json" -X POST "/1.1/direct_messages/events/new.json"
####-d
##{
##  "event": {
##    "type": "message_create",
##    "message_create": {
##      "target": {
##        "recipient_id": "944480690"
##      },
##      "message_data": {
##        "text": "Hello World!"
##      }
##      }
##    }
##  }
##


import pyautogui, time, pynput

pyautogui.failsafeexception = True
pyautogui.PAUSE = 0.1

x = 0

#count = str(x)

while x < 10000:
    x += 1
    pyautogui.click(1035, 537)
    pyautogyi.typewrite(str(x))
    pyautogui.press('return')
    time.sleep(0.1)
