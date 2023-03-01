# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input("Input IP address: ")

try: 

   octets = ip_address.split('.')

   while not len(octets) == 4:
         raise ValueError()
   else:
      for octet in octets:
         number = int(octet)
         if number in range(0,256):
            pass
         else:
            raise ValueError()
except (ValueError, ZeroDivisionError):
   print("Неправильный IP-адрес")
else:
   numver = int(octets[0])
   if numver in range(1, 224):
      print('unicast')
   elif numver in range(224,240):
      print('multicast')
   elif numver == 255 and int(octets[1]) == 255 and int(octets[2]) == 255 and int(octets[3]) == 255:
      print('local broadcast')
   elif numver == 0 and int(octets[1]) == 0 and int(octets[2]) == 0 and int(octets[3]) == 0:
      print('unassigned')
   else:
      print('unused')
