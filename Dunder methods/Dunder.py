import app

def print_Dunder():
    name = (__name__)
    return name

if __name__ == "__main__":
    #the following is calling code from within this script
    print("I am running code from {}".format(print_Dunder()))
    #the following line is calling code from the "app.py" file
    print("I am running code from {}".format(app.print_app()))
