import keyboard, time
Ptime = time.time()
words = input('Enter all the words here, each separated by a single space. Stop the program by holding down ESC. Keystrokes will be made 3 seconds after you submit your input so be ready: ').split()
for i in [3, 2, 1]:
    print(i)
    time.sleep(1)
while time.time()-Ptime < 3600 and not keyboard.is_pressed('esc'):
    for i in range(0, len(words)):
        keyboard.write(words[i])
        keyboard.press_and_release('enter')
        time.sleep(0.1)#or else your comp will die
    time.sleep(0.5)#you want your comp to be running, not frozen or crashed    
