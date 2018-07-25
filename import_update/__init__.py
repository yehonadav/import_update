# -*- coding: utf-8 -*-
"""
careful!
all __init__.py files
content will be overwritten
run this everytime you want to update your imports.


# usage example:

from os.path import dirname
from import_update import update_imports_recursively

update_imports_recursively(dirname(__file__))
"""


__version__ = '1.0.1'


import os
import glob


def update_imports(path):
    files = os.listdir(path.replace("__init__.py", ""))
    imports = []

    for i in range(len(files)):
        name = files[i].split('.')
        if len(name) > 1:
            if name[1] == 'py' and name[0] != '__init__':
                name = name[0]
                imports.append(name)

    file = open(path, 'w')
    write = '__all__ = '+str(imports)
    file.write(write)
    file.close()


def update_imports_recursively(root_directory):
    for filename in glob.iglob(root_directory+'/**', recursive=True):
        if filename.endswith("__init__.py"):
            update_imports(filename)
