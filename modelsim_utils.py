''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line
import auto_key_utils

util_submodule_l = ['exception_utils', 'hotkey_utils', 'focus_utils']  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

from util_submodules.hotkey_utils    import hotkey_utils    as hu      ; util_submodule_import_check_count += 1
from util_submodules.exception_utils import exception_utils as eu      ; util_submodule_import_check_count += 1
from util_submodules.focus_utils     import focus_utils     as fu      ; util_submodule_import_check_count += 1

''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''



import auto_key_utils as aku

import time 
import keyboard as k

# for exception handling 
import _tkinter 


NEXT_PANE__SHORTCUT_STR           = 'Shift+f4'
RAISE_CMD_WINDOW__SHORTCUT_STR    = 'Alt+/'
ZOOM_FULL__WAVE_PANE_SHORTCUT_STR = 'f'

# press Alt + / when modelsim opens
# project must be open in modelsim
# do file must be in project dir (such that if you were to start typing it in the modelsim cmd window, you could autocomplete)
def auto_run(do_file_name = 'run_cmd.do', run_to_pane_shift_sleep_sec = 7):

    fu.set_foreground("ModelSim")

    time.sleep(.3)
    
    
    
    
    print('waiting for hotkey press: ', RAISE_CMD_WINDOW__SHORTCUT_STR, '...')
    hu.wait_for_hotkey_press(RAISE_CMD_WINDOW__SHORTCUT_STR)
    
    cmd = "do " + do_file_name
    k.write(cmd)
#     time.sleep(.3)# need ???????????????????????????????????????????????????????
    
#     hu.wait_for_hotkey_press('a', print_waiting_msg = True)

    
    # check if cmd window stayed up long enough to enter command, if not, do it again
    try:
        selection = aku.make_then_get_selection(select_mode = 'shift_home', error_on_empty_clipboard = True)
    except(_tkinter.TclError):
        time.sleep(.3)
        k.press_and_release(RAISE_CMD_WINDOW__SHORTCUT_STR)
        k.write(cmd)
    
    
    # run command to execute do file
    k.press_and_release("enter")
    
    
    time.sleep(7)  # not optimized!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     
    # shift into console pane from the sim pane
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    
    # enter command that does nothing because if you don't, you can't get into the wave pane for some reason
    k.press_and_release('esc') # just in case you had an auto-complete window up before running this
    k.press_and_release('enter')
    
    # shift into wave pane from terminal pane 
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    
    # zoom full to show the part of the wave you care about
    time.sleep(.3)
    k.press_and_release(ZOOM_FULL__WAVE_PANE_SHORTCUT_STR)
    
    # shift into console window because I feel like it
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    k.press_and_release(NEXT_PANE__SHORTCUT_STR)
    
    
    
#     k.write
    
    
    
#     console_output = aku.make_then_get_selection(deselect_key_str = 'right arrow', error_on_empty_clipboard = True) # sim:/nand4_tb/i_a sim:/nand4_tb/i_b sim:/nand4_tb/i_c sim:/nand4_tb/i_d sim:/nand4_tb/o_f 
#     print(console_output) # sim:/nand4_tb/duv/NAND2_1/i_a sim:/nand4_tb/duv/NAND2_1/i_b sim:/nand4_tb/duv/NAND2_1/o_f 
 
     
#     print('waiting for hotkey press: ', RAISE_CMD_WINDOW__SHORTCUT_STR, '...')
#     hu.wait_for_hotkey_press(RAISE_CMD_WINDOW__SHORTCUT_STR)
# 
#     k.write("do " + do_file_name)
#     time.sleep(.3)
#     k.press_and_release("enter")
#     
# #     time.sleep(7)
#     
# #     console_output = aku.get_select_all(deselect_key_str = 'right arrow')
# #     print(console_output)
#     
#     time.sleep(run_to_pane_shift_sleep_sec)
#     k.press_and_release(NEXT_PANE__SHORTCUT_STR)
# 
# #     k.press_and_release("shift+f4")
# #     k.press_and_release("shift+f4")
#     k.press_and_release("esc")
#     k.write('empty command to shift focus')
# #     k.press_and_release("enter")
# #     k.press_and_release(NEXT_PANE__SHORTCUT_STR)
# #     k.press_and_release("f")




''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == "__main__":
    print('In Main: modelsim_utils')
    
    auto_run('run_cmd__NAND4.do')
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main: modelsim_utils')