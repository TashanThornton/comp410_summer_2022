import unittest
from team1_pii import find_us_social_security, find_us_phone_numbers, find_us_street_address, find_twitter_handle, \
    find_credit_card_number, find_bank_acc_number, find_email_address, find_personal_names


class Team1TestCases(unittest.TestCase):
    def test_us_phone(self):
        # Test valid phone number
        phone = '336-555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '336.555.1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '(336) 555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        # Test invalid
        phone = 'My number is 336-42-1212'
        self.assertFalse(find_us_phone_numbers(phone))

    def test_us_street_address(self):
        # Test valid street address
        streetAddress = '1234 Sesame Street, Bronx, NY, 12345-6789'
        self.assertTrue(find_us_street_address(streetAddress))

        streetAddress = '6789 Baker Street, Atlanta, GA, 12345'
        self.assertTrue(find_us_street_address(streetAddress))

        # Test invalid
        streetAddress = 'My street address is 12 Invalid Input Drive'
        self.assertFalse(find_us_street_address(streetAddress))

    def test_credit_card_number(self):
        # Test Valid
        cardNum = '1234 5678 9012 3456'
        self.assertTrue(find_credit_card_number(cardNum))

        cardNum = '1234 5678 3495 3456'
        self.assertTrue(find_credit_card_number(cardNum))

        cardNum = '6543 5678 9012 3456'
        self.assertTrue(find_credit_card_number(cardNum))

        # Test invalid
        cardNum = '123B4 5678 9012 3456'
        self.assertFalse(find_credit_card_number(cardNum))

        cardNum = '1234 5678 9012'
        self.assertFalse(find_credit_card_number(cardNum))

    def test_twiter_handle(self):
        # Test valid
        userName = '@MHAOfficial'
        self.assertTrue(find_twitter_handle(userName))

        userName = '@sza'
        self.assertTrue(find_twitter_handle(userName))

        userName = '@netflix'
        self.assertTrue(find_twitter_handle(userName))

        # Test Invalid

        userName = 'my email is jon@smith.com'
        self.assertFalse(find_twitter_handle(userName))

        userName = 'powerade'
        self.assertFalse(find_twitter_handle(userName))

    def test_bank_acc_number(self):
        # Test valid bank account numbers
        acc = '0123456789'
        self.assertTrue(find_bank_acc_number(acc))

        acc = '010234567891'
        self.assertTrue(find_bank_acc_number(acc))

        # Invalid Test
        acc = '012.90.a89'
        self.assertFalse(find_bank_acc_number(acc))

    def test_email_address(self):
        # Test valid email address
        email = 'aBc12@email.com'
        self.assertTrue(find_email_address(email))

        email = 'ro1s3@email.com'
        self.assertTrue(find_email_address(email))

        # Invalid Test
        email = '@twitter'
        self.assertFalse(find_email_address(email))

    def test_social_security(self):
        # Test valid social security
        ssn = '702-02-0202'
        self.assertTrue(find_us_social_security(ssn))

        ssn = 'This is a SSN: 123-12-1234'
        self.assertTrue(find_us_social_security(ssn))

        ssn = '111-09-3401'
        self.assertTrue(find_us_social_security(ssn))

        # Invalid Test
        ssn = '09-09-0909'
        self.assertFalse(find_us_social_security(ssn))

        ssn = '000-09-0909'
        self.assertFalse(find_us_social_security(ssn))

    def test_personal_names(self):
        # Test valid Name
        name = 'Kaylin Burgess'
        self.assertTrue(find_personal_names(name))

        name = 'Name: John Smith'
        self.assertTrue(find_personal_names(name))

        # Test invalid names
        name = "Banking Statement"
        self.assertFalse(find_personal_names(name))


if __name__ == '__main__':
    unittest.main()
