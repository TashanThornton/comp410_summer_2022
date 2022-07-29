from scan import scan_files, get_file_text
import re

# https://developers.google.com/edu/python/regular-expressions
# https://regex101.com/
def find_us_phone_numbers(text):
    match = re.search(r'(\d{3}[-.]\d{3}[-.]\d{4})', text)
    if match:
        return True
    return False

def find_us_ssn(text):
    match = re.search(r'(\d{3})-(\d{2})-(\d{4})', text)
    if match:
        match_lst = match.groups()
        first = match_lst[0]
        second = match_lst[1]
        third = match_lst[2]
        if first == '000' or second == '00' or third == '0000':
            return False
        return True
    return False

def find_credit_card_number(text):
    match = re.search(r'([0-9]{4}[- ][0-9]{4,6}[- ][0-9]{4,5}[- ]?[0-9]{0,4})', text)
    if match:
        return True
    return False

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

def find_dob(text):
    match = re.search(r'(\d{1,2})[-|\/](\d{1,2})[-|\/]((\d{4})|(\d{2}))', text)
    if match:
        dob_lst = match.groups()
        month = int(dob_lst[0])
        day = int(dob_lst[1])
        year = int(dob_lst[2])

        if (month < 1 or month > 12) or (day < 1 or day > 31):
            return False
        elif (month == 2 and (day > 29 or (day == 29 and not is_leap_year(year)))):
            return False
        else:
            return True
    return False

def find_us_twitter_handle(text):
    match = re.search(r'^[@](\w){1,15}$', text)
    if match:
        return True
    return False

def find_us_email(text):
    match = re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', text)
    if match:
        return True
    return False

def find_us_bank_account(text):
    match = re.search(r'^(\d{8,12})$', text)
    if match:
        return True
    return False

def find_us_address(text):
    match = re.search(r'(\d{1,5}\s{1}[\w\s]*,\s{1}[\w\s-]*,\s{1}[A-Z]{2},\s{1}(\d{5}-\d{4}|\d{5}))', text)
    if match:
        return True
    return False
