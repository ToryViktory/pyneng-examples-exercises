# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate
def print_ip_table(reachable_list,unreachable_list):
    ips = {"Reachable": reachable_list, "Unreachable": unreachable_list}

    print(tabulate(ips, headers="keys"))

if __name__ == "__main__":
    alive = ["10.10.1.7", "10.10.1.8", "10.10.1.9", "10.10.1.15"]
    unreachable = ["10.10.2.1", "10.10.1.2"]

    print_ip_table(alive,unreachable)