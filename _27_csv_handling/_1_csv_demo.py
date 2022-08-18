# CSV
# extension .csv
# it stands for Comma Seperated Value
# all the data in this file are seperated by comma

import csv
rows = []
with open("B:\\DS290622A\\DS290622A\\_27_csv_handling\\csv_file.csv","r") as file:
    data = csv.reader(file) # csv.DictReader(file)

    header = next(data)
    print(header)

    print()

    for row in data:
        rows.append(row)

    print(rows)

    print()
    for i in rows[:2]:
        print(i)

    count = data.line_num
    print("Row Count : ",count)