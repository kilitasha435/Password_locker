import unittest
from user_credentials import User

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

if __name__ == '__main__':
    unittest.main()
