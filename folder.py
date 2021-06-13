import os
import csv

day = input('日付を入力して下さい')

os.makedirs(day)
stores_path = "viecle.csv"

with open(stores_path, encoding="cp932") as f:
    reader = csv.reader(f)
    for row in reader:
        folder_name = row[0] + '_' + row[1]
        folder_name = day + '/' + folder_name
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
    
            


