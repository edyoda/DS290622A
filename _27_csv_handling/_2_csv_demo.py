import csv

# header = ["rno","name"]
# data = [[1,"Bharati"],[2,"Puneet"]]
fieldnames = ["rno","name"]
rows = [{"rno":1,"name":"Bharati"}]

with open("B:\\DS290622A\\DS290622A\\_27_csv_handling\\csv_file1.csv","w") as file:
    # writer = csv.writer(file)
    writer = csv.DictWriter(file,fieldnames)

    # writer.writerow(header)
    # writer.writerows(data)

    writer.writeheader()
    writer.writerows(rows)