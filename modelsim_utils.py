import focus_utils

import time 
import keyboard as k


# project must be open in modelsim
# do file must be in project dir (such that if you were to start typing it in the modelsim cmd window, you could autocomplete)
def auto_run(do_file_name = 'run_cmd.do', run_to_pane_shift_sleep_sec = 7):
    time.sleep(1)
    focus_utils.set_foreground("ModelSim")
    focus_utils.set_foreground("ModelSim")
    time.sleep(3)
    k.press_and_release("esc")
    time.sleep(3)
    k.press_and_release("Alt + /")
    time.sleep(3)
    k.write("do " + do_file_name)
    time.sleep(3) # .2 used to work
    k.press_and_release("enter")
    time.sleep(run_to_pane_shift_sleep_sec)
    k.press_and_release("shift+f4")
    k.press_and_release("shift+f4")
    k.press_and_release("f")

if __name__ == "__main__":
    auto_run()



# do run_cmd.do