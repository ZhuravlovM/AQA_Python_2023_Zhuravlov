# Write a function to validate the correctness of entered email address

import re


def email_validation(email):
    pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


email_example = "sample_mail@mail.com"

if email_validation(email_example):
    print("Email is valid")
else:
    print("Entered email is not valid")