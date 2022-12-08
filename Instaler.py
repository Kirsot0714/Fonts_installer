import os
import shutil
import ctypes, sys
import collections

directory = r'C:\Users\Кирилл\Desktop\шрифты'
os_wolk = os.walk
dic = collections.defaultdict(dict)
EXTENTION_PRIORITY = ('otf', 'ttf')
extention_filtr = {'otf', 'ttf'}
# dic_not_default = {}

if os.path.isdir(directory):
    for way, namderectory, names in os_wolk(directory):
        for i in names:
            split_i = i.split('.')
            name = i[:-4:]
            type = split_i[-1]
            if split_i[-1] in extention_filtr:
                # dic_not_default[name] = {type : rf"{way}\{i}"}
                dic[name][type] = rf"{way}\{i}"
# print(dic_not_default)
try:
    for name_of_font, value in dic.items():
        for ext in EXTENTION_PRIORITY:
            path = value.get(ext)
            if path:
                shutil.copy(path, r'C:\Windows\Fonts')  # C:\Users\Кирилл\Desktop\шрифты_перенос
                print(name_of_font, path.replace('',''))
                break
except PermissionError as erorr: #Exception
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    print(erorr)
