def start(nice=0, mean=0, name=""):
    #gets user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

#checks to see if this is a new game or not. If it is new, gets the user's name.
# if it is not a new game, display a message thanking the player and continues
# with the game
def describe_game(name):
    if name != "":
        print("\nThank you for playing, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people.\nYou can choose to be nice or mean, but at the end of the game you will have to face the consequences.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        # displays a message, and user inputs if they want to be nice or mean
        pick = input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? (N/M) >>>: ").lower()
        #if user enters "N" for nice, displays a message and increments "nice" by 1
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        #if user enters "M" for mean, displays a message and increments "mean" by 1
        if pick == "m":
            print("\nThe stranger glares at you menacingly and storms off...")
            mean = mean + 1
            stop = False
    #pass the three variables to the score
    score(nice, mean, name)

def show_score(nice, mean, name):
    print("\n{}, your current total:({}, Nice) and ({}. Mean)".format(name, nice, mean))

#score function is being passed the values stored within the 3 variables
def score(nice, mean, name):
    #if "nice" is more than 2, call the "win" function passing in the variables
    if nice > 2:
        win(nice, mean, name)
    #if "mean" is more than 2, call the "lose" function passing in the variables
    if mean > 2:
        lose(nice, mean, name)
    #otherwise, call the "nice_mean" function passing in the variables
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    #substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! Everyone loves you and you've made lots of friends along the way!".format(name))
    #call the "again" function and pass in our variables
    again(nice, mean, name)

def lose(nice, mean, name):
    #substitute the {} wildcards with our variable values
    print("\nToo bad, {}, game over! \n{}, by being mean, you've ruined your life. Now, you live in a vaaaaan, down by tha riverrr!".format(name))
    #call the "again" function and pass in our variables
    again(nice,mean,name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter [ Y ] for 'YES', or [ N ] for 'NO':>>> ")

#resets the game's scores, but keeps the user's name the same, since they are playing again
def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice,mean,name)

if __name__ == "__main__":
    start()
