import focus_utils

import time 
import keyboard as k

global HOTKEY_PRESSED 
# project must be open in modelsim
# do file must be in project dir (such that if you were to start typing it in the modelsim cmd window, you could autocomplete)
def auto_run(do_file_name = 'run_cmd.do', run_to_pane_shift_sleep_sec = 7):
    def pressed():
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        global hotkey_pressed
        hotkey_pressed = True
    
#     global hotkey_pressed
    hotkey_pressed = False
#     focus_utils.set_foreground("ModelSim")
#     
# #     time.sleep(2)
#     time.sleep(.3)
#     k.press_and_release("ctrl+/")
#     time.sleep(.3)
#     k.press_and_release("shift+f4")
# # #     time.sleep(.3)
# #     k.press_and_release("shift+f4")
# # #     time.sleep(.3)
    print('waiting')
#     k.add_hotkey('/', print, args=('triggered', 'hotkey'))    
    k.add_hotkey('a', pressed) 
    
    while(not hotkey_pressed):
        time.sleep(1)
        print('hp: ', hotkey_pressed)

# #     k.press_and_release("Alt + /")
# #     k.press_and_release("Alt + /")
# #     k.press_and_release("Alt + /")
# #     k.press_and_release("Alt + /")
#     k.write("do " + do_file_name)
# #     time.sleep(.2)
# #     k.press_and_release("enter")
# # #     time.sleep(run_to_pane_shift_sleep_sec)
# # #     k.press_and_release("shift+f4")
# # #     k.press_and_release("shift+f4")
# # #     k.press_and_release("f")

if __name__ == "__main__":
    auto_run('run_cmd__NAND4')



# do run_cmd.do