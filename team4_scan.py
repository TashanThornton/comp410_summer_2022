import glob
import re

from scan import get_file_text
from team4_pii import find_us_phone_numbers, find_twitter_usernames, find_email_handle, find_credit_card_numbers, find_account_number

if __name__ == '__main__':

    test_funcs = [find_us_phone_numbers, find_twitter_usernames, find_email_handle, find_credit_card_numbers, find_account_number]

    for file in glob.iglob('files/**/*', recursive=True):
        valid_file = re.search(r'.\.pdf$|.\.docx$|.\.xlsx$|.\.txt$', file)

        if not valid_file:
            continue

        for func in test_funcs:
            has_pii = func(str(get_file_text(file)))
            if has_pii:
                print('file at {0} has PII'.format(file))
            else:
                print('file at {0} does NOT contain PII'.format(file))
