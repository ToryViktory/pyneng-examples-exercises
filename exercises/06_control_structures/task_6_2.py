# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input("Input IP address: ")

octets = ip_address.split('.')
numver = int(octets[0])
if numver in range(1, 223):
   print('unicast')
elif numver in range(224,239):
   print('multicast')
elif numver == 255 and int(octets[1]) == 255 and int(octets[2]) == 255 and int(octets[3]) == 255:
   print('local broadcast')
elif numver == 0 and int(octets[1]) == 0 and int(octets[2]) == 0 and int(octets[3]) == 0:
   print('unassigned')
else:
   print('unused')


