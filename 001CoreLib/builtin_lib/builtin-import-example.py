# encoding:utf-8
'''
Created on 2018年9月11日

@author: litsoft
'''

import glob, os

moudles = []

for moudle_file in glob.glob("*-plugin.py"):
    try:
        moudle_name, ext = os.path.splitext(os.path.basename(moudle_file))
        moudle = __import__(moudle_name)
        moudles.append(moudle)
    except ImportError:
        pass

for moudle in moudles:
    moudle.hello()

print("-" * 20)


def getfunctionbyname(moudle_name, function_name):
    moudle = __import__(moudle_name)
    return getattr(moudle, function_name)


print getfunctionbyname("dumbdbm", "open")
print repr(getfunctionbyname("dumbdbm", "open"))

print("-" * 20)


class LazyImport:
    def __init__(self, moudle_name):
        self.moudle_name = moudle_name
        self.moudle = None

    def __getattr__(self, name):
        if self.moudle is None:
            self.moudle = __import__(self.moudle_name)
        return getattr(self.moudle, name)


string = LazyImport("string")
print(string)
print(string.lowercase)

print("-" * 20)


