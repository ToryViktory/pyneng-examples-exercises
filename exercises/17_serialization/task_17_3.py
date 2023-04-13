# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
def parse_sh_cdp_neighbors(show_cdp_neighbors):
        result_dict = {}
        hostname_regex = (r'(?P<hostname>\S+>)')
        hostname_match = re.search(hostname_regex, show_cdp_neighbors)
        hostname = hostname_match.group('hostname').strip('>')
        regex = (r'(?P<device>\S+)\s+(?P<local_intf>\w+\s\S+)(?:\s+\d+\s+(?:\w\s+)*\S+\s+)(?P<port_id>\w+\s\S+)')
        result_dict[hostname] = {}
        for match in re.finditer(regex, show_cdp_neighbors):
                nested_dict_2 = {}
                nested_dict_1 = {}
                device = match.group('device')
                local_intf = match.group('local_intf')
                port_id = match.group('port_id')
                nested_dict_1[device]=port_id
                nested_dict_2[local_intf] = nested_dict_1
                result_dict[hostname].update(nested_dict_2)
        return result_dict

if __name__ == "__main__":
        filename = "sh_cdp_n_sw1.txt"
        with open(filename) as src:
                result = parse_sh_cdp_neighbors(src.read())
                print(result)
