import pyautogui
import time
steam_path = r'AcceptQ\queuepop.png'

def accept():
    count =0
    while True:
        
        steam_location = pyautogui.locateCenterOnScreen(steam_path)
        time.sleep(1)
        count +=1
        print('looking for queue pop', count)
         
        
        if steam_location is not None:
            
            break
        
    time.sleep(0.5)
    
    pyautogui.moveTo(steam_location)
    time.sleep(0.5)
    # pyautogui.leftClick()
    print('Queue Found and Accepted')

accept()