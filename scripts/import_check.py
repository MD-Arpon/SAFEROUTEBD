import importlib, traceback

try:
    m = importlib.import_module('accounts.forms')
    print('Imported accounts.forms, classes:', [name for name in dir(m) if name.endswith('Form')])
except Exception:
    traceback.print_exc()
