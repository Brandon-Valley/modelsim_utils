

from util_submodules.clipboard_utils import clipboard_utils as cu

import keyboard as k


# Ctrl + a, copy to clipboard, return clipboard
def get_select_all():
    og_clipboard = cu.get_clipboard()
    
    k.press_and_release('Ctrl+a')
    k.press_and_release('Ctrl+c')
    
    new_clipboard = cu.get_clipboard()
    
    cu.set_clipboard(og_clipboard)
    
    return new_clipboard





if __name__ == '__main__':
    print('In Main:  auto_key_utils')
    
    print(get_select_all())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main:  auto_key_utils')