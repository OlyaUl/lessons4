#! env bin/python
# codding = utf-8
import re
import turtle
import argparse
from collections import namedtuple
from console import *


def main_loop(user_interface):
    while True:
        command = next(user_interface)
        if command == 'exit':
            break
        print(command)


if __name__ == "__main__":
    user_interface = user_interface_generator()
    main_loop(user_interface)














    '''while True:
        command = input()
        print(command)'''

    #all_commands = namedtuple('Open', 'Create', 'Save',
                             # 'Params', 'Circle', 'Triangle', 'Rectangle')
    '''all_commands = {'open':{},
                    'draw':{},
                    'exit':{}}'''

    '''def f():
        yield 1
        yield 2
        yield 3

    gen_obj = f()
    print(list(gen_obj))
    for i in gen_obj:
        print(i)'''