import sys
import traceback

with open('traceback.txt', 'w') as f:
    for th in sys._current_frames().values():
        traceback.print_stack(th, file=f)
        f.write('\n')
