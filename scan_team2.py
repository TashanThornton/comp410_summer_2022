from scan import scan_files, get_file_text
from team2_pii import find_us_ssn
from team2_pii import find_credit_card_number
from team2_pii import find_dob
from team2_pii import find_us_address
from team2_pii import find_us_phone_numbers
from team2_pii import find_name

file_list = scan_files()
for f in file_list:
    txt_list = get_file_text(f)

    for t in txt_list:
        ssn_found = find_us_ssn(t)
        ccn_found = find_credit_card_number(t)
        dob_found = find_dob(t)
        add_found = find_us_address(t)
        phone_found = find_us_phone_numbers(t)
        names_lst = find_name(t)
        
        if ssn_found or ccn_found or dob_found or add_found or phone_found:
            print("PII: " + f + ": " + t)
        elif names_lst != [[], []]:
            for pii in names_lst[0]:
                print("PII: " + f + ": " + pii)
            for no_pii in names_lst[1]:
                print("NO_PII: " + f + ": " + no_pii)
        else:
            print("NO_PII: " + f + ": " + t)
    
    print()