import billboard1,re
from billboard1 import ChartData
import csv
start_date='1990-01-01'
file_object = open('baa8.csv', 'a')
csv_file_writer = csv.writer(file_object, delimiter=",", quoting=csv.QUOTE_ALL, quotechar="'")
csv_file_reader = csv.reader(open('baa.csv', "rb"), delimiter=",")
chart=ChartData('hot-100', date=start_date, fetch=True, timeout=25)
flag=True


while chart.date<'2018-12-30':
    chart = ChartData('hot-100', date=start_date, fetch=True, timeout=25)
    print("The date going on is:",start_date)
    for i in range(100):
        string = str(chart[i])
        cleaned = string.replace("'", "")
        cleaned=cleaned.replace(",","|")
        cleaned = cleaned.split(sep=' by ')
        for row  in csv_file_reader:
            if row[0]==cleaned[0]:
                flag=False
        if flag:
            csv_file_writer.writerow(cleaned)
    start_date=chart.nextDate
