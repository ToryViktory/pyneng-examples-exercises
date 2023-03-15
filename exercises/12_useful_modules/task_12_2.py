# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
def convert_ranges_to_ip_list(ip_list):
    new_ip_list = []
    for ip_address in ip_list:
        if '-' in ip_address:
            first_ip, last_value = ip_address.split('-')
            first_ip_last_oct = first_ip.split('.')[-1]
            first_ipv4 = ipaddress.ip_address(first_ip)
            if len(last_value)<=3:
                last_ipv4 = ipaddress.ip_address(first_ipv4 + (int(last_value)-int(first_ip_last_oct)))
            else:
                last_ipv4 = ipaddress.ip_address(last_value)
            
            ip = first_ipv4
            while ip <= last_ipv4:
                new_ip_list.append(str(ip))
                ip+=1
        else:
            new_ip_list.append(ip_address)
    return new_ip_list

ip_list = ["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]
print(convert_ranges_to_ip_list(ip_list))