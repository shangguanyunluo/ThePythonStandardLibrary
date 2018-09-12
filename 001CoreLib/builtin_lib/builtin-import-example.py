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
