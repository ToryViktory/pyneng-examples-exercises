# -*- coding: utf-8 -*-

"""
Задание 22.1c

Изменить класс Topology из задания 22.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        self.topology = {}
        for key, value in topology_dict.items():
            if not self.topology.get(value) == key:
                self.topology[key]=value
        return self.topology

    def delete_link(self, forward_link, reverse_link):
        topology_copy = self.topology.copy
        topology_size = len(self.topology)
        for key, value in list(self.topology.items()):
            if key == forward_link and value == reverse_link:
                del self.topology[key]
            elif key == reverse_link and value == forward_link:
                del self.topology[key]
        if topology_size == len(self.topology):
                print("Такого соединения нет")

    def delete_node(self, node):
        dict_size = len(self.topology)
        for key, value in list(self.topology.items()):
            if key[0] == node or value[0] == node:
                del self.topology[key]
        if dict_size == len(self.topology):
            print("Такого устройства нет")

if __name__ == "__main__":
    top = Topology(topology_example)
    top.topology
    top.delete_node('SW1')
    print(top.topology)

