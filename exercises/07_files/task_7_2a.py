# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv

cfg_lines2 = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        words_list = line.split()
        unique = set(words_list) & set(ignore)
        if line.startswith('!'):
            pass
        elif unique:
            pass
        # elif any(ign in line for ign in ignore):
        #     pass
        else:
            cfg_lines2.append(line)
print(''.join(cfg_lines2))
