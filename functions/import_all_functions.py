import os

def import_all_functions():

    funcs = os.listdir('functions')

    for func in funcs:
        if func.startswith('__') or func == 'import_all_functions.py':
            continue
        # func = func.replace('.py','')
        # print(f'{func} imported')
        # exec(f'from functions.{func} import *')
        mod = __import__(f'functions.{func}')
        to_import = [getattr(mod, x) for x in dir(mod)]

        for i in to_import:
            try:
                setattr(sys.modules[__name__], i.__name__, i)
                print(f'{func} imported')
            except AttributeError:
                pass