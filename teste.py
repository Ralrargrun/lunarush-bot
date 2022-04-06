import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

currentMouseX, currentMouseY = pyautogui.position()

# bosshunt = pyautogui.locateOnScreen('boss-fight-mode-icon.png')
# print(bosshunt)

# # # pyautogui.moveTo(button7location) # Move the mouse to XY coordinates.
# pyautogui.click(bosshunt) 
# time.sleep(10)
# bossgreen = pyautogui.locateOnScreen('bossverde.PNG')
# pyautogui.moveTo(bossgreen)
# pyautogui.click(bossgreen) 
# time.sleep(10)

i=0
vazio1 = pyautogui.locateOnScreen('vazio.PNG')
print(vazio1)
print(type(vazio1))
while((vazio1 == None) and (i<1000)):
    vazio1 = pyautogui.locateOnScreen('vazio.PNG')
    print(vazio1)
    pyautogui.moveTo(vazio1)
    # time.sleep(0.00000001)
# pyautogui.click(vazio1) 
# time.sleep(10)

