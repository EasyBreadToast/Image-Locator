import pyautogui 
import time

while True: 
    f = pyautogui.locateCenterOnScreen('Untitled.png', confidence=0.8)   
    if f != None:
        print("Found")
        pyautogui.click(f)
        time.sleep(1)
        break
    else:
        print("Not found, relocating...")
        time.sleep(1)

print('Image located... stopped')