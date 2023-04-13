# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import csv
import re
def write_dhcp_snooping_to_csv(filenames,output):
    regex = (r'(?P<mac>\S+)\s+'
            r'(?P<ip>\S+)\s+'
            r'(?P<lease>\d+)\s+'
            r'(?:\S+)\s+'
            r'(?P<vlan>\d+)\s+'
            r'(?P<intf>\S+)')

    data = [['switch','mac','ip','vlan','interface']]
    common_data = []

    for filename in filenames:
        with open(filename) as src:
            for m in re.finditer(regex, src.read()):
                switch = filename.split('_')[0]
                mac = m.group('mac')
                ip = m.group('ip')
                vlan = m.group('vlan')
                intf = m.group('intf')
                data.append([switch,mac,ip,vlan,intf])
    with open(output, 'w', newline='') as dest:
        print(data)
        writer = csv.writer(dest)
        for row in data:
            if row:
                writer.writerow(row)
        # writer.writerows(data)


if __name__ == "__main__":
    filenames = ["sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt","sw3_dhcp_snooping.txt"]
    output = "common_dhcp_snooping.csv"
    info = write_dhcp_snooping_to_csv(filenames,output)
    print(info)