import pyautogui
import pyperclip
import time


name = "文件传输助手"
message = "新年快乐"
pyautogui.click(1162,1046)
time.sleep(0.5)
pyautogui.keyDown("ctrl")
pyautogui.hotkey('f')
pyautogui.keyUp("ctrl")
# time.sleep(0.1)
pyperclip.copy(name)
time.sleep(0.1)
pyautogui.keyDown("ctrl")
pyautogui.hotkey("v")
pyautogui.keyUp("ctrl")
pyautogui.hotkey("enter")
pyperclip.copy(message)
for i in range(10):
    time.sleep(0.1)
    pyautogui.keyDown("ctrl")
    pyautogui.hotkey("v")
    pyautogui.keyUp("ctrl")
    pyautogui.hotkey("enter")

