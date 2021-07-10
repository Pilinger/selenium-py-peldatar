import csv

with open('table_in.csv', 'r', encoding='utf-8') as full_csv:  # opening the file for reading
    csv_reader = csv.reader(full_csv, delimiter=',')
    # opening the file for writing with newline='' for avoiding blank lines
    with open('short.csv', 'w', newline='', encoding='utf-8') as short_csv:
        csv_writer = csv.writer(short_csv, delimiter=',')
        # writing only the Email and Name fields
        for row in csv_reader:
            csv_writer.writerow([row[1], row[0]])
