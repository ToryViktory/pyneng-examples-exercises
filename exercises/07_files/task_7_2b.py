# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv

cfg_lines2 = []
src_filename = argv[1]
dest_filename = argv[2]
# src_filename = 'config_sw1.txt.'
# dest_filename = 'config_sw2.txt.'
with open(src_filename) as f:
    with open(dest_filename, 'w') as dest:
        for line in f:
            words_list = line.split()
            unique = set(words_list) & set(ignore)
            if line.startswith('!'):
                pass
            elif unique:
                pass
            else:
                cfg_lines2.append(line)
        dest.writelines(cfg_lines2)
