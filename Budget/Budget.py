#new function named "calcBills"
def calcBills():
    #creates a variable with the following properties
    myBills = {'Electric': 120.00, 'Rent': 1200.00, 'Water_Sewer': 60.00, 'Car_Insurance': 75.00, 'Phone': 65.00}
    #creates an integer and sets its value to 0
    total = 0
    #uses a for loop to add all the numbers in "myBills" to "total"
    for i in myBills:
        total += myBills[i]
    #creates a string that has a sentence with the "total"
    owed = 'The total cost for bills this month is: ${}'.format(total)
    #returns the "owed" string
    return owed
    
