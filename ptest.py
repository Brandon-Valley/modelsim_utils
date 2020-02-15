from pynput.keyboard import Key
from pynput.keyboard import Controller

keyboard = Controller()

import time
time.sleep(3)

with keyboard.pressed(Key.shift):
    keyboard.press(Key.home)
#     keyboard.release(Key.left)
#     keyboard.press(Key.left)
    keyboard.release(Key.left)