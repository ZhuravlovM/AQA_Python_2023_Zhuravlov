import csv


class CSVController:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def add_row(self, row_data):
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_data)

    def delete_row(self, row_index):
        rows = []
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)

        if 0 <= row_index < len(rows):
            rows.pop(row_index)

        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
