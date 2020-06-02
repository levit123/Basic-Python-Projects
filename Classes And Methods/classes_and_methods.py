class User:
    #the properties of the class
    name = 'No name provided'
    email = ' '
    password = '1234abcd'
    account = 0

    #constructor for the User class
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account
    
    #methods of the User class
    def login(self):
        #user enters their email and password
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        #if the info the user entered matches the info of the class object,
        #then it prints a welcome message. If not, it prints a message
        #saying they are not authorized due to incorrect info
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")


#child classes that inherit from the User class
class Employee(User):
    base_page = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True

#creates a new object of the User class
new_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)
