# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
# from sys import argv
filtered_lines = []

final_list = []
# filename = argv[1]
input_vlan = int(input("Input VLAN: "))
filename = 'CAM_table.txt'
with open(filename) as f:
    for line in f:
        line_elements = line.split()

        for element in line_elements:
            if '.' in element:
                filtered_lines.append(line)
        count=len(filtered_lines)
    for filtered_line in filtered_lines:
        new_list = []
        vlan = int(filtered_line.split()[0])
        mac = filtered_line.split()[1]
        ports = filtered_line.split()[3]
        new_list.append(vlan)
        new_list.append(mac)
        new_list.append(ports)
        final_list.append(new_list)
    sorted_list = sorted(final_list)

    for sorted_line in sorted_list:
        vlan, mac, ports = sorted_line
        output = "{:<8} {} {:>8}"
        if (vlan == input_vlan):
            print(output.format(vlan,mac,ports))
        else:
            pass

