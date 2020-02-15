

from util_submodules.clipboard_utils import clipboard_utils as cu

import keyboard as k
from pynput.keyboard import Key
from pynput.keyboard import Controller
import time


def make_selection(select_mode):
    if select_mode == 'all':
        k.press_and_release('Ctrl+a')
    elif select_mode == 'shift_home':            
        keyboard = Controller()
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.home)
            keyboard.release(Key.left)
        

# Ctrl + a, copy to clipboard, return clipboard
def get_selection(deselect_key_str = None, error_on_empty_clipboard = False):
    og_clipboard = cu.get_clipboard()
    
    cu.clear_clipboard()
    
#     k.press_and_release('Ctrl+a')
    k.press_and_release('Ctrl+c')
    
    new_clipboard = cu.get_clipboard()
    
    if error_on_empty_clipboard and str(new_clipboard) == '':
        raise Exception("ERROR:  Tried to copy current selection, nothing was copied to clipboard")
        
    
    cu.set_clipboard(og_clipboard)
    
    if deselect_key_str != None:
        time.sleep(.3)# need ??????????????????????????????????????????????????????
        k.press_and_release(deselect_key_str)
    
    return new_clipboard



def make_then_get_selection(select_mode, deselect_key_str = None, error_on_empty_clipboard = False):
    make_selection(select_mode)
    return get_selection(deselect_key_str, error_on_empty_clipboard)

if __name__ == '__main__':
    print('In Main:  auto_key_utils')
    
# #     print(get_select_all())
    time.sleep(4)
#     k.press_and_release('shift+home')
# #     k.press_and_release('home')


    make_selection('shift_home')

#     k.press('shift')
#     time.sleep(.3)
#     k.press_and_release('left arrow')
#     time.sleep(.3)
# 
#     k.press_and_release('left arrow')
#     time.sleep(.3)
#     k.press_and_release('left arrow')
#     time.sleep(.3)
#     k.release('shift')
    
    
#     k.release('shift')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main:  auto_key_utils')