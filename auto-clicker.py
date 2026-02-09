import pyautogui
pyautogui.position()

import time

pyautogui.FAILSAFE = True

print("bismillah")
time.sleep(4)

confirm_button= (1784, 556)
ok_button= (1534, 378)
biliyorum_hata_var_button=(1686, 645)
count=0

while True:
    pyautogui.click(confirm_button)
    time.sleep(4)

    pyautogui.click(ok_button)
    time.sleep(13)

    pyautogui.click(biliyorum_hata_var_button)
    time.sleep(2)
    count+=1
    print (count)