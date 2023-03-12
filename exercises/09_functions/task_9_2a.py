# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_mapping,trunk_template):
    dict_output = {}
    for intf, vlans in intf_vlan_mapping.items():
        output = []
        # dict_output=dict(intf=output)
        # output.append(f'interface {intf}')
        for command in trunk_template:
            vlan_str = ",".join(str(vlan) for vlan in vlans)
            if command.endswith('allowed vlan'):
                output.append(f'{command} {vlan_str}')
            else:
                output.append(f'{command}')
        dict_output[intf] = output

    return dict_output

result = generate_trunk_config(trunk_config, trunk_mode_template)
print(result)


# result = {device: {key.lower(): value for key, value in params.items()}
#           for device, params in london_co.items()}

# In [44]: result
# Out[44]:
# {'r1': {'hostname': 'london_r1',
#   'ios': '15.4',
#   'ip': '10.255.0.1',
#   'location': '21 New Globe Walk',
#   'model': '4451',
#   'vendor': 'Cisco'},
#  'r2': {'hostname': 'london_r2',
#   'ios': '15.4',
#   'ip': '10.255.0.2',
#   'location': '21 New Globe Walk',
#   'model': '4451',
#   'vendor': 'Cisco'},
#  'sw1': {'hostname': 'london_sw1',
#   'ios': '3.6.XE',
#   'ip': '10.255.0.101',
#   'location': '21 New Globe Walk',
#   'model': '3850',
#   'vendor': 'Cisco'}}

# In [2]: r1 = dict(model='4451', ios='15.4')
# In [3]: r1
# Out[3]: {'model': '4451', 'ios': '15.4'}


# In [4]: r1 = dict([('model', '4451'), ('ios', '15.4')])
# In [5]: r1
# Out[5]: {'model': '4451', 'ios': '15.4'}