import time, pyautogui as pag

print("Proceed to select Lightroom")
time.sleep(3)

while True:
    pag.hotkey("shift", 'a')
    time.sleep(1)
    pag.press('right')
    time.sleep(2)