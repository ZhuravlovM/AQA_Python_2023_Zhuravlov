import datetime


def age_calculation(birth_date):
    current_date = datetime.datetime.now()
    current_age = round((current_date - birth_date).days/365)
    age_timestamp = birth_date.timestamp()
    return current_age, age_timestamp


birthday = datetime.datetime(year=1998, month=5, day=20, hour=14, minute=15, second=00)
age, timestamp = age_calculation(birthday)
print("Точний вік:", age)
print("Timestamp:", timestamp)
