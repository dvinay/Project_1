from csv import reader, writer

out_2015 = writer(open("./angeles_parking/parking-2015.csv", "w"), delimiter=",")
out_2016 = writer(open("./angeles_parking/parking-2016.csv", "w"), delimiter=",")
out_2017 = writer(open("./angeles_parking/parking-2017.csv", "w"), delimiter=",")
out_2018 = writer(open("./angeles_parking/parking-2018.csv", "w"), delimiter=",")
out_2019 = writer(open("./angeles_parking/parking-2019.csv", "w"), delimiter=",")
out_other = writer(open("./angeles_parking/parking-other.csv", "w"), delimiter=",")

line_count = 0
for row in reader(open("./angeles_parking/parking.csv", "r"), delimiter=","):
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        out_2015.writerow(row)
        out_2016.writerow(row)
        out_2017.writerow(row)
        out_2018.writerow(row)
        out_2019.writerow(row)
        out_other.writerow(row)
        line_count = line_count+1
    else:
        if row[1].find("2015-") >= 0:
            out_2015.writerow(row)
        elif row[1].find("2016-") >= 0:
           out_2016.writerow(row)
        elif row[1].find("2017-") >= 0:
            out_2017.writerow(row)
        elif row[1].find("2018-") >= 0:
           out_2018.writerow(row)
        elif row[1].find("2019-") >= 0:
            out_2019.writerow(row)
        else:
            out_other.writerow(row)
        line_count = line_count + 1
print(f'Processed {line_count} lines.')






