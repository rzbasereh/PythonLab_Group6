import csv
with open("data.csv",mode="r+") as file:
    m=csv.reader(file)
    with open("csv_text.csv",mode="w") as file_csv:
        file_write = csv.writer(file_csv)
        for line in m:
            file_write.writerow(line[1:])

