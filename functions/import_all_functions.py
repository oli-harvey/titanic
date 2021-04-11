import os

def import_all_functions():

    funcs = os.listdir('functions')

    for func in funcs:
        if func.startswith('__') or func == 'import_all_functions.py':
            continue
        func = func.replace('.py','')
        print(f'{func} imported')
        exec(f'from functions.{func} import *')