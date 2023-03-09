import csv

product_dictionary = {}
with open("C:\\Users\\Jacob Bode\\Downloads\\products.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        product_dictionary[row[0]] = row[1]
with open("C:\\Users\\Jacob Bode\\Downloads\\tr-75k.csv", mode="r") as reading:
    csv_reader = csv.reader(reading, delimiter=",")
    with open("C:\\Users\\Jacob Bode\\Downloads\\tr-75k-canonical.csv", mode="w") as writing:
        csv_writer = csv.writer(writing, delimiter=",")
        for row in csv_reader:
            new_row = []
            row.pop(0)
            for i in range(len(row)):
                new_row.append(product_dictionary[row[i].strip()])
            csv_writer.writerow(new_row)

