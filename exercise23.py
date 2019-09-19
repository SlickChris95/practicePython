'''
Give two files that have lists of numbers in them,
the numbers that are overlapping.
'''
import pprint
path2 = 'C:\\Users\\Chris\\Desktop\\test2.txt'
path1 = 'C:\\Users\\Chris\\Desktop\\test1.txt'


list1 = []
list2 = []

def overlap(l1,l2):
    newlist = []
    for i in range(len(l1)):
        if(l1[i] in l2):
            newlist.append(l1[i])
    return newlist

with open(path2,'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.rstrip('\n')
        list2.append(int(line))
        line = open_file.readline()

# pprint.pprint(list2)
print('--------------')

with open(path1,'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.rstrip('\n')
        list1.append(int(line))
        line = open_file.readline()

# pprint.pprint(list1)
pprint.pprint(overlap(list1,list2))
