class User:
    '''
    Class that generates instances of user credentials
    '''

    users_list = [] # Empty list where users will be saved

    def __init__(self, first_name, last_name, password):
        '''
        __init__ method that helps us define properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save_user method that saves user objects in the users_list
        '''
        User.users_list.append(self)

    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method that checks if the name and the password entered match entries in the users list.
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

class Credentials:
    '''
    Class that generates instances of account credentials, generate passwords and save information
    '''

    credentials_list = []
    users_credentials_list = []

    def __init__(self, user_name, site_name, account_name, password):
        '''
        __init__ method that helps us define properties for our objects
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password