from pprint import pprint
import csv
import re
def unite_lines(line1, line2):
    result = line1
    index = 0
    while index < len(line1):
        if len(line1[index]) == 0:
            result[index] = line2[index]
        index = index+1
    return result

def add_elem_in_result_list(list, line):
    for item in list:
        if item[0] == line[0]:
            item = unite_lines(item, line)
            return 'unit'
    list.append(line)
    return  'no unit'


contacts_list = list()
with open("phonebook_raw.csv", encoding = 'utf-8') as f:
   rows = csv.reader(f, delimiter=",")
   contacts_list = list(rows)

regx1 = re.compile(r"^([А-Я]{1}[а-яё]+)\s*,*([А-Я]{1}[а-яё]+)\s*,*([А-Я][а-яё]*)*")
subs1 = r"\1,\2,\3"
regx2 = re.compile(r"(\+*\d{1}\s*)\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\s*\-*(\d{2})\s*(\(*([а-яё]*\.\s\d{4})\)*)*")
subs2 = r"+7 (\2) \3-\4-\5 \7"

result_list=[]
for line in contacts_list:
    fullname = line[0] + ' ' + line[1] + ' ' + line[2]
    fullname = regx1.sub(subs1, fullname).strip()
    line[0:3] = fullname.split(',')
    if len(line[5])>0:
        line[5] = regx2.sub(subs2, line[5]).strip()
    add_elem_in_result_list(result_list, line)

with open("phonebook.csv", "w", encoding = 'utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)