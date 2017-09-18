#! env bin/python
# codding = utf-8
from collections import namedtuple


'''cli = {'cmd': "Enter command (open,draw, exit)",
       'open': {'cmd': "Input file name"},
       'draw': {'cmd': 'choice circle or rectangle',
                       'choice circle or rectangle': ['circle', 'rectangle'],
                                                   'circle': 'input x y R', 'rectangle': 'input x1 y1 x2 y2'},
       'exit': {}}'''

'''cli = {'cmd': "Enter command (open,draw, exit)",
       'open': {'cmd': "Input file name"},
       'draw': {'cmd': 'choice circle or rectangle',
                       'choice circle or rectangle':
                           {'circle': 'x y R',
                            'rectangle': 'x1 y1 x2 y2'}
                 }
       }'''
'''namedtuple('choice', ['circle', 'rectangle']),
                               'circle': 'input x y R',
                                    'input x y R': namedtuple('x','y', 'z'),
                               'rectangle': 'input x1 y1 x2 y2',
                           '''
cli = {'name': 'root',
       'template': 'Enter command (open,draw, exit)',
       'childs': [{'name': 'root',
                   'template': 'Enter command (open,draw, exit)',
                   'childs':""}]
}


def user_interface_generator():
    while True:
        # com = input("Input command: ")
        com = input(cli['cmd'])
        print("enter command (%s)" % com)
        count = 0
        def rec(com):
            while True:
                if com in cli:
                    yield com
                    # key =
                    print(cli[com]['cmd'])

                    # break
                else:
                    print("Error")
                    #yield com
                    continue
        rec(com)
        #def rec(com):
        # while True:
        #     if com in cli:
        #         yield com
        #         # key =
        #         print(cli[com]['cmd'])
        #         break
        #
        #         '''if count == 0:
        #             print(cli[com]['cmd'])
        #             if cli[com]['cmd'] == "":
        #                 break
        #                 yield com
        #             else:
        #                 continue
        #         elif count == 1:
        #             if cli[com]['cmd'][com] == "":
        #                 break
        #                 yield com
        #
        #             else:
        #                 continue'''
        #
        #             #yield com
        #             #print(cli[com]['cmd'][com])
        #             #break
        #         count += 1
        #         # continue
        #     else:
        #         print("Error")
        #         # yield com
        #         continue
                    #rec(com)
        #rec(com)