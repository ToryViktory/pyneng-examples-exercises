# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(ip_list):
    alive = []
    unreachable = []
    for ip_address in ip_list:
        reply = subprocess.run(['ping', '-n', '3', ip_address])

        if reply.returncode == 0:
            alive.append(ip_address)
        else:
            unreachable.append(ip_address)

    result = tuple([alive,unreachable])
    return result

ip_list = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]

ping_ip_addresses(ip_list)