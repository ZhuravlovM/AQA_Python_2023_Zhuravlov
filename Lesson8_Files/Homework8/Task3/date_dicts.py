import re


def parse_dates_from_file(processed_file):
    dates = []
    with open(processed_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            date_lookup = re.search(r'\d{1,2}(st|nd|rd|th)?\s+([A-Za-z]+)\s+\d{4}', line)
            if date_lookup:
                date = date_lookup.group()
                dates.append({"date": date})
    return dates


file_name = 'authors.txt'
result = parse_dates_from_file(file_name)
print('Dates from authors.txt:\n', result)
