import unittest
from user_credentials import User, Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each check if pyperclip is installedtest cases.
        '''
        self.new_user = User('Kevin', 'Kili', 'kilitasha123') # create user object


    def test__init__(self):
        '''
        Test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.first_name, "Kevin")
        self.assertEqual(self.new_user.last_name, "Kili")
        self.assertEqual(self.new_user.password, "kilitasha123")

    def test_save_credentials(self):
        '''
        Test case to check if we can save credentials to the credentials list.
        '''
        self.new_credential.save_credential()
        facebook = Credentials("Stacie", "Facebook", "Staciey", "stac123")
        facebook.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        '''
        A method that clears the users credentials list after every test.
        '''
        Credentials.credentials_list = []

    def test_display_credentials(self):
        '''
        Test case to test if our objects show.
        '''
        self.new_credential.save_credential()
        facebook = Credentials("Stacie", "Facebook", "Staciey", "stac123")
        facebook.save_credential()
        gmail = Credentials('Sheila','Gmail','shy6','sheilaegeidza6')
        gmail.save_credential()
        self.assertEqual(len(Credentials.display_credential(facebook.user_name)), 1)
       


if __name__ == '__main__':
    unittest.main()
