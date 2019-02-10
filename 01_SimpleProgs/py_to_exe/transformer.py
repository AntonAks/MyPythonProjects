from os import system, getcwd
from json import load

with open(getcwd() + '\\' + 'settings.json') as set_file:
    set_data = load(set_file)

py_installer = set_data['py_installer']
py_script_path = set_data['py_script_path_one']
# py_script_path = set_data['py_script_path_two']


print(py_installer)
print(py_script_path)


system(py_installer + ' --onefile ' + '"' + py_script_path + '"')
# os.system(py_installer + ' "' + py_script_path + '"')
