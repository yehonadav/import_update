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


__version__ = '1.0.4'


import os
import glob


def update_imports(path):
    dir_path = path.replace("__init__.py", "")
    files = os.listdir(dir_path)
    imports = []

    for i in range(len(files)):
        name = files[i].split('.')
        if len(name) > 1:
            if name[1] == 'py' and name[0] != '__init__':
                name = name[0]
                imports.append(name)
        elif os.path.isdir(dir_path + files[i]):
            for _ in glob.iglob(dir_path + files[i] + "/__init__.py"):
                imports.append(name[0])
                break

    all_line = '__all__ = {}\n'.format(str(imports))
    import_line = 'from . import {}\n'.format(str(imports)[1:-1].replace("'", ""))

    with open(path, 'r') as file:
        lines = file.readlines()

    all_line_exist = False
    import_line_exist = False

    for i in range(len(lines)):
        if lines[i].startswith('__all__'):
            lines[i] = all_line
            all_line_exist = True

        elif lines[i].startswith(import_line[:-1]):
            lines[i] = import_line
            import_line_exist = True

        elif all_line_exist is True and import_line_exist is True:
            break

    if all_line_exist is False:
        lines.append('\n')
        lines.append(all_line)
    if import_line_exist is False:
        lines.append('\n')
        lines.append(import_line)

    with open(path, 'w') as file:
        for line in lines:
            file.write(line)
        file.close()


def update_imports_recursively(root_init):
    """send init file or init directory"""
    for filename in glob.iglob(root_init.replace("__init__.py", "") + '/**', recursive=True):
        if filename.endswith("__init__.py"):
            update_imports(filename)
