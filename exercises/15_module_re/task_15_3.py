# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
stringTemplate = '''
object network LOCAL_{ip}
 host {ip}
 nat (inside,outside) static interface service tcp {port} {intf}'''
def convert_ios_nat_to_asa(src_file,dst_file):
    regex = (r'(?:\w+\s)*'
            r'(?P<ip>\S+) '
            r'(?P<port>\d+) '
            r'(?:\w+\s\S+) '
            r'(?P<intf>\d+)')
    lines = []

    with open(src_file) as src, open(dst_file, 'w') as dest:
        for m in re.finditer(regex, src.read()):
            ip = m.group(1)
            port = (m.group(2))
            intf = (m.group(3))

            line_out=stringTemplate.format(ip = ip, port = port, intf = intf)
            lines.append(line_out)
        dest.writelines(lines)

if __name__ == "__main__":
    info = convert_ios_nat_to_asa("cisco_nat_config.txt","out_cisco_nat_config.txt")
    print(info)