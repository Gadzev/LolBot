import pyautogui

role = pyautogui.confirm('What role would you like to play?', 'Select role', ['Top', 'Adc', 'Jungle', 'Support', 'Mid'])

locate = True

print 'Waiting for match...'

while locate:
    located = pyautogui.locateCenterOnScreen('choose.png')
    if located != None:
        locate = False

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite(role + '\n')
pyautogui.typewrite(role + '\n')


























