# PII: files/november_statement.pdf: Name: John Smith
# NO_PII: files/november_statement.pdf: MyBank.com - Banking Statement
from scan import get_file_text, scan_files
from team1_pii import find_us_phone_numbers, find_us_street_address, find_twitter_handle, find_credit_card_number, \
    find_bank_acc_number, find_email_address, find_us_social_security, find_personal_names



def find_pii(text):
    detected_pii_list = []

    if find_us_phone_numbers(text):
        detected_pii_list.append('US_Phone_Number')

    if find_email_address(text):
        detected_pii_list.append('Email_Address')

    if find_bank_acc_number(text):
        detected_pii_list.append('Banking_Account_Number')

    if find_credit_card_number(text):
        detected_pii_list.append('Credit_Card_Number')

    if find_us_street_address(text):
        detected_pii_list.append('US_Street_Address')

    if find_twitter_handle(text):
        detected_pii_list.append('Twitter_Handle')

    if find_us_social_security(text):
        detected_pii_list.append('US_SSN')

    if find_personal_names(text):
        detected_pii_list.append('Personal_Name')

    return detected_pii_list



def main():
    # get list of files to be scanned
    files_list = scan_files()
    for f in files_list:
        # get the text from the file
        for text in get_file_text(f):
            result = find_pii(text)
            if result:
                # PII was found
                print(': '.join(['PII', f, text]))
                print(result)
            else:
                # No PII found in this file
                print(': '.join(['NO_PII', f, text]))


if __name__ == '__main__':
    main()
