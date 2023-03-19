import csv
import re
import tracemalloc
from datetime import datetime
start_time=datetime.now()

aaa = 0

with open("C:\\Users\\Dell\\Maghe\\New folder\\find_words.txt", 'r') as fp:
    lines = [line.rstrip('\n') for line in fp]

with open("C:\\Users\\Dell\\Maghe\\New folder\\t8.shakespeare.txt", 'r') as rd:
    data1 = rd.read()

for i in lines:
    for a in range(2):

        ENG = i
        with open("C:\\Users\\Dell\\Maghe\\New folder\\french_dictionary.csv", 'r',encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=['English', 'French'])
            data = list(filter(lambda find: find['English'] == ENG, reader))
            if a == 0:
                j = data[0]['French']
            else:
                j = data[0]['French']
                j = j.capitalize()
                i = i.capitalize()

            my_regex = r'\b%s\b' % i
            res_1 = re.subn(my_regex, j, data1, aaa)
            print("Count:" + str(res_1[1]))

            data1 = res_1[0]
            print("English:" + i + " " + "French:" + " " + j)



with open("C:\\Users\\Dell\\Maghe\\New folder\\t8.shakespeare_translated.txt", 'w') as wt:
    wt.write(data1)
print("Text Replaced")
end_time=datetime.now()
print('Time to process:{}'.format(end_time-start_time))
def app():
    lt=[]
    for i in range(0,100000):
        lt.append(i)
tracemalloc.start()
app()
print("Memory used:",tracemalloc.get_tracemalloc_memory())
tracemalloc.stop()



