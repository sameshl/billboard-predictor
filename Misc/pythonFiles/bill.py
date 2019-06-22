import billboard,re
from billboard import ChartData,ChartEntry
import csv
start_date='2008-01-19'
file_object = open('baa.csv', 'a')
csv_file_writer = csv.writer(file_object, delimiter=",", quoting=csv.QUOTE_ALL, quotechar="'")
chart=ChartData('hot-100', date=start_date, fetch=True, timeout=25)

'''
c=chart[10]
string = str(c)
cleaned = string.replace("'", "")
print(cleaned)
cleaned=cleaned.replace(",","|")
#cleaned = re.sub('\sby\s', '&&&', cleaned)
#print(cleaned)
cleaned = cleaned.split(sep=' by ')
print(cleaned)
'''

while chart.date<'2018-12-30':
    chart = ChartData('hot-100', date=start_date, fetch=True, timeout=25)
    print("The date going on is:",start_date)
    for i in range(100):
        string = str(chart[i])
        cleaned = string.replace("'", "")
        cleaned=cleaned.replace(",","|")
        cleaned = cleaned.split(sep=' by ')
        csv_file_writer.writerow(cleaned)
    start_date=chart.nextDate

#print(cleaned)


#chart.date=chart.nextDate
#print(chart)
