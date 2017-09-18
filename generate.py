#! env bin/python
# codding = utf-8
import turtle
import pprint
import math


if __name__ == "__main__":
    def f():
        while True:
            print("from gen")
            a = yield 1
            print(a)


    g = f()
    next(g)
    for i in range(10):
        print("in loop")
        # print(next(g))
        b = g.send(i)
        print(b)