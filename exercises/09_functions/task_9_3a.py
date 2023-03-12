# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
                if len(line_elements) >= 4:
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
                else:
                    for el in line_elements:
                        if el.startswith(' switchport mode access'):
                            access_vlans = int(1)
                            access_output[interface]=access_vlans


        result = tuple([access_output,trunk_output])
        return result

filename='config_sw2.txt'
result = get_int_vlan_map(filename)
print(result)
