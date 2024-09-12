from scan import scan_files, get_file_text
from team4_pii import find_us_phone_numbers, find_twitter_usernames, find_email_handle, find_credit_card_numbers, find_account_number

if __name__ == '__main__':

    test_funcs = [find_us_phone_numbers, find_twitter_usernames, find_email_handle, find_credit_card_numbers, find_account_number]

    for file in scan_files():

        file_text_line_by_line = get_file_text(file)
        pii_lines = []

        for line in file_text_line_by_line:
            for func in test_funcs:
                is_pii = func(line)
                if is_pii:
                    pii_lines.append(line)

        if len(pii_lines) > 0:
            print('file at {0} has PII'.format(file))
            for pii in pii_lines:
                print(pii)
            print('---------------------------------------------')
        else:
            print('file at {0} does NOT have PII'.format(file))
            print('---------------------------------------------')
