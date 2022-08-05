from scan import scan_files, get_file_text
import re


# https://developers.google.com/edu/python/regular-expressions
# https://regex101.com/
def find_us_phone_numbers(text):
    match = re.search(r'(\(?\d{3}\)?(\s{1}|[-.])\d{3}[-.]\d{4})', text)
    if match:
        return True
    return False


def find_us_street_address(text):
    matchLong = re.search(r'(\d{3,4}\s{1}[a-zA-z\s]*,\s{1}[a-zA-z\s-]*,\s{1}[A-Z]{2},\s{1}(\d{5}-\d{4}|\d{5}))', text)
    matchShort = re.search(
        r'\d{3,4}\s{1}[a-zA-Z]*\s((\d{1,3}[a-zA-Z]*\s?)*|[a-zA-Z\s]*)(Street|Terrace|Lane|Lanes|Drive|Alley|Circle|Avenue|Boulevard){1}',
        text)

    if matchLong or matchShort:
        return True
    return False


def find_credit_card_number(text):
    match = re.search(r'\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}', text)
    if match:
        return True
    return False


def find_twitter_handle(text):
    match = re.search(r'\B@\w*([A-Za-z0-9_]+)\w*', text)
    if match:
        return True
    return False


def find_bank_acc_number(text):
    match = re.search(r'(?:\d{3,4}\-\d{5}|\d{10}|\d{12})', text)
    if match:
        return True
    return False


def find_email_address(text):
    match = re.search(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$', text)
    if match:
        return True
    return False


def find_us_social_security(text):
    match = re.search(r'((?!666|000)[0-8][0-9\_]{2}\-(?!00)[0-9\_]{2}\-(?!0000)[0-9\_]{4})', text)
    if match:
        return True
    return False


def find_personal_names(text):
    exclude_list = ['Full', 'Name', 'Banking', 'Statement', 'Account', 'Number', 'Last', 'Social', 'Security', 'Test',
                    'Document', 'Phone', 'Card', 'Credit', 'Terrace', 'Lane', 'FitnessGram']
    pii_list = []
    # find all the regex matches in text
    for match in re.findall(r'[A-Z][A-Za-z]+\s+[A-Z][A-Za-z]+', text):
        # if nothing from exclude_list is in this match then it is pii
        if not any(e in match for e in exclude_list):
            pii_list.append(match)
            return True
    return False
