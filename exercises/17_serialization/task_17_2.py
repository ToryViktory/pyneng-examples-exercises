# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import re
import csv

sh_version_files = glob.glob("sh_vers*")
# print(sh_version_files)

headers = ["hostname", "ios", "image", "uptime"]

def parse_sh_version(sh_version):
  pattern = re.compile(r'Cisco IOS Software, (?:\S+\s)*(?:Version\s)(?P<ios>\S+), RELEASE'
          r'|router uptime is(?P<uptime>(\s\d+\s\S+)+)'
          r'|System image file is "(?P<image>\S+)"', re.MULTILINE)
  result = []
  lines = sh_version.split('\n')
  for line in lines:
    match = re.search(pattern, line)
    if match:
      if match.lastgroup == 'ios':
          result.insert(0, match.group('ios'))
      elif match.lastgroup == 'uptime':
          result.insert(2, match.group('uptime').strip())
      else:
          result.insert(1, match.group(match.lastgroup))
  result_tuple = tuple(result)
  return result_tuple

def write_inventory_to_csv(data_filenames,csv_filename):
  data = [headers]
  for filename in data_filenames:
    with open(filename) as src:
      hostname = filename.strip('.txt').split("_")[-1]
      out = parse_sh_version(src.read())
      formatted_list = [hostname]
      formatted_list = formatted_list + list(out)
      data.append(formatted_list)

  with open(csv_filename, 'w', newline='') as dest:
    writer = csv.writer(dest)
    for row in data:
        if row:
            writer.writerow(row)

if __name__ == "__main__":
    output_file = "routers_inventory.csv"
    write_inventory_to_csv(sh_version_files,output_file)
