import datetime

data1 = datetime.date(2022, 10, 8)
data2 = datetime.date(2023, 8, 8)

if data1 > data2:
    print("data 1 maggiore -> ", data1.strftime('%d/%m/%Y'))
else:
    print("data 2 maggiore -> ", data2.strftime('%d/%m/%Y'))
