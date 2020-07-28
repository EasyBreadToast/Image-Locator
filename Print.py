import pyautogui 
import time


while True: 
    f = pyautogui.locateCenterOnScreen('Untitled.png', confidence=0.8)   
    if f != None:              #If it founds it....
        print("Found")
        pyautogui.click(f)
        time.sleep(1)
        break
    else:
        print("Not found, relocating...") #Will keep finding it...
        time.sleep(1)

print('Image located... stopped')
