# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий
для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно,
чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии,
но и удалять "дублирующиеся" соединения (их лучше всего видно на схеме, которую
генерирует функция draw_topology из файла draw_network_graph.py).
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Из-за того что один и тот же линк описывается дважды, на схеме будут лишние соединения.
Задача оставить только один из этих линков в итоговом словаре, не важно какой.

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии
с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть "дублирующихся" линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
from draw_network_graph import draw_topology
import yaml
from task_17_3a import generate_topology_from_cdp

def transform_topology(yml_file):

    with open(yml_file) as f:
        templates = yaml.safe_load(f)
        print(templates)
        new_dict = {}
        for key, value in templates.items():
            sub_dict = {}
            for subkey,subvalue in value.items():
                items = [list(i) for i in subvalue.items()]
                sub_dict[tuple([key,subkey])]=tuple(items[0])
                new_dict.update(sub_dict)
        # Remove duplicates
        topology_copy= new_dict.copy()

        for key in list(new_dict.keys()): 
            for value in list(topology_copy.values()):
                if key == value:
                    del new_dict[key]
                    del topology_copy[value]
        result = new_dict
    return result

if __name__ == "__main__":
    topology = transform_topology("topology.yaml")
    print(topology)
    draw_topology(topology)