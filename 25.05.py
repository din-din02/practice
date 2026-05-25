import math
import multiprocessing
import random
import csv
import pandas

list_number=list(random.sample(range(100,1000), 500))
list_number1=str(list_number)

def write():
    with open ('our_numbers.csv','w') as num:
        num.write(list_number1)
    print('файл записан')
def reading():
    with open('our_numbers.csv','r') as num:
        list_num=[]
        a=num.read()
        a.strip()
        for i in a:
            list_num.append(int(a[i]))
    return list_num

def func_for_proccess(list1: list): #func for process
    num=1
    for i in list1:
        num*=i
    return num

a=reading()
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
def for_list():
    counter=100
    global a
    list1=[]
    for i in a:
        if counter>0:
            list1.append(0)
            a.remove(0)
            counter-=1
        else:
            return list1

list1=for_list() 
list2=for_list() 
list3=for_list() 
list4=for_list() 
list5=for_list() 