#from  pynput.mouse import *#Button, Controller
#from pynput.keyboard import *#Key, Controller
import pynput.keyboard as keyboard1
#import pynput.mouse as mouse1
import time
import os
'''
mouse = mouse1.Controller()
print(mouse.position)
time.sleep(3)
print('The current pointer position is {0}'.format(mouse.position))

mouse.position = (70, 150)
print('now we have moved it to {0}'.format(mouse.position))


mouse.press(mouse1.Button.left)
mouse.release(mouse1.Button.left)
'''
keyboard = keyboard1.Controller()

#Press and release space
#keyboard.press(keyboard1.Key.space)
#keyboard.release(keyboard1.Key.space)
#Type a lower case A ;this will work even if no key on the physical keyboard  is labelled ‘A‘
#keyboard.press('a')
#keyboard.release('a')

#type ‘hello world ‘  using the shortcut type  method
#keyboard.type('hello world')
count=1
while True:
    time.sleep(1)
    print(count)
    count=count+1
    if count ==4200 :
        break;

keyboard.press(keyboard1.Key.f2)
keyboard.release(keyboard1.Key.f2)

'''
count=1
while True:
    time.sleep(1)
    print(count)
    count=count+1
    if count == 3 :
        os.system('taskkill/f/im oCam.exe')
        time.sleep(10)
        os.system('shutdown -s -t 0')

'''
