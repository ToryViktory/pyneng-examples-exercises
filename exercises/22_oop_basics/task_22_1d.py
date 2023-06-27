# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Соединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Соединение с одним из портов существует


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

    def add_link(self, forward_link, reverse_link):
        dict_size = len(self.topology)
        for key, value in list(self.topology.items()):
            if key == forward_link and value == reverse_link:
                print("Такое соединение существует")
                break
            elif key == forward_link or value == reverse_link:
                print("Соединение с одним из портов существует")
                break
            else:
                self.topology.update({forward_link:reverse_link})

if __name__ == "__main__":
    top = Topology(topology_example)
    top.topology
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    print(top.topology)
    top.add_link(('R1', 'Eth0/4'), ('R8', 'Eth0/0'))
    print(top.topology)

