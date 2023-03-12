# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    trunk_output = {}
    access_output = {}
    with open(config_filename) as f:
        lines_list = f.read().strip().split('!')
        for line in lines_list:
            new_line = line.strip()
            if new_line.startswith('interface'):
                interface = new_line.split()[1]
                line_elements=new_line.split('\n')
                for el in line_elements:
                    if el.startswith(' switchport trunk allowed vlan'):
                        trunk_str_vlans = (el.split(' ')[-1].split(','))
                        trunk_vlans = [int(item) for item in trunk_str_vlans]
                        trunk_output[interface]=trunk_vlans
                    elif el.startswith(' switchport access vlan'):
                        access_vlans = int(el.split(' ')[-1])
                        access_output[interface]=access_vlans
                    else:
                        pass
        result = tuple([access_output,trunk_output])
        return result

filename='config_sw1.txt'
result = get_int_vlan_map(filename)
print(result)
