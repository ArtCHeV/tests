from mimesis.builtins import RussiaSpecProvider as rus
from mimesis import Person
import random
import time
import csv

def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%d.%m.%Y', prop)

fib_list = [i for i in range(1,26)]
for num in range(len(fib_list)):
    if num >=3:
        fib_list[num]= fib_list[num-1]+fib_list[num-2]
print(fib_list)
person_list =[]
for num in range(25):
    name = num
    i = rus()
    name = Person('ru')
    person_list.append([str(name.full_name())+';'
    +str(name.telephone(mask= '79#########'))+';'
    +str(name.email())+';'+str(fib_list[num])+';'
    +str(randomDate('1.1.1971', '31.12.2021', random.random()))+';'])

myFile = open('example2.csv', 'w',newline='',encoding='utf-8')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(person_list)
