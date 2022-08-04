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

def find_name(text):
    exclude_lst = ['St', 'Dr', 'Street', 'Drive', 'Full', 'Name', 'Banking', 'Statement',
                    'MyBank', 'Account', 'Number', 'Period', 'November', 'Balance', 'This',
                    'The', 'document', 'contains', 'sample', 'PII', 'detect', 'twitter',
                    'secret', 'this', 'but', 'Gender', 'Social', 'Security', 'Your', 'Address',
                    'Terrace', 'West', 'Lane', 'Neque', 'Quis', 'Nulla', 'viverra', 'purus',
                    'eros', 'vehicula', 'Suspendisse', 'ultrices', 'pacer', 'beep', 'ding', 'name',
                    'hotmail', 'rutrum', 'aol', 'icloud', 'ante', 'Lorem', 'Esterdayyay', 'Ethay',
                    'Ityay', 'stinks', ',ut', 'Pacer', 'after', 'single', 'over', 'start',
                    'Female', 'Male', 'June']
    pii_lst = []
    no_pii_lst = []
    matches = re.findall(r'([a-zA-Z\s\',-.]+[ ]?)', text)
    no_pii = re.findall(r'([\$]*[\d]+[\.]*[,]*[-]*[\d]*)', text)
    #print("text = " + text)
    #print("matches = " + str(matches))
    if matches != []:
        for match in matches:
            if match == ' ' or match == '.' or match == '-' or match == ',':
                continue
            elif not any(e in match for e in exclude_lst):
                pii_lst.append(match)
            else:
                no_pii_lst.append(match)
    if no_pii != []:
        for match in no_pii:
            no_pii_lst.append(match)
    return [pii_lst, no_pii_lst]

def find_us_twitter_handle(text):
    match = re.search(r'\B@\w*([A-Za-z0-9_]+)\w*', text)
    if match:
        return True
    return False

def find_us_email(text):
    match = re.search(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[(gov|com|edu)]+)', text)
    if match:
        return True
    return False

def find_us_bank_account(text):
    hyphen_match = re.search(r'(\d{4}-\d{5})', text)
    no_hyphen_match = re.search(r'^(\d{8,12})$', text)
    if hyphen_match or no_hyphen_match:
        return True
    return False

def find_us_address(text):
    match = re.search(r'(\d{1,5}\s{1}[\w\s]*,\s{1}[\w\s-]*,\s{1}[A-Z]{2},\s{1}(\d{5}-\d{4}|\d{5}))', text)
    if match:
        return True
    elif re.search(r'(\d{1,5}\s{1}[\w\s]*)', text):
        if "20 meter" not in text and "30 seconds" not in text:
            return True
    return False