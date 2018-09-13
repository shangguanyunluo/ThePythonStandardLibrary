# encoding:utf-8
'''
Created on 2018年9月10日

@author: litsoft
'''
from pip.utils.logging import colorama


def function(a, b):
    print a, b
    

apply(function, ("hello", "world!"))
    
apply(function, (1, 2 + 3))

print("*"*20)

apply(function, ("hello",), {"b":"world!"})
apply(function, (), {"a":"hello", "b":"world!"})

print("*"*20)


class Rectangle():

    def __init__(self, color="white", width=10, height=10):
        print "create a ", color, "sized:", width, " width", height, " height"


class RoundedRectangle(Rectangle):

    def __init__(self, **kw):
        apply(Rectangle.__init__, (self,), kw)

        
rect = RoundedRectangle(color="red", width=100, height=100)
rect = RoundedRectangle(color="blue", width=20)
