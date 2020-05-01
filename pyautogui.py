import pyautogui, time

pyautogui.FailSafeException = True
pyautogui.PAUSE = 0.1
x = 0

#count = str(x)

while x < 10000:
    x += 1
    ##pyautogui.click(1035, 537)
    ##pyautogui.typewrite(str(x))
    ##pyautogui.press('return')
    time.sleep(0.1)
    
