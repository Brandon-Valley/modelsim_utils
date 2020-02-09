import argparse

import modelsim_utils

import time

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--do_file_name'               , default = 'run_cmd.do')
parser.add_argument('-r', '--run_to_pane_shift_sleep_sec', default = 7) # 6 used to work
args = parser.parse_args()

time.sleep(1) # 1 used to work
modelsim_utils.auto_run(args.do_file_name, int(args.run_to_pane_shift_sleep_sec))