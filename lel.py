import pyautogui, time
time.sleep(5)
f = open("lmao.txt", 'r')
for word in f:
 pyautogui.typewrite(word)
 pyautogui.write(['enter'])
