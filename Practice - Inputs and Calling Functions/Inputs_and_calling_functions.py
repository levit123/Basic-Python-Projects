#function that calls the a series of other function and displays
#their return values
def start():
    print(get_number())
    print("Hello {}".format(get_name()))

#function that defines a variable and sets it equal to a number, then returns
#the value of that number
def get_number():
    number = 12
    return number

#function that defines a variable based off of user input, then returns the
#value of that variable
def get_name():
    name = input("What is your name? ")
    return name

#kicks off the whole program starting from the "start" function
if __name__ == "__main__":
    start();
