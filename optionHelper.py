from OptionConstants import ORDER_FOOD, VIEW_ACCOUNT, VIEW_ORDER, optionsDictionary


def optionHelper():
    loggedIn = True
    while loggedIn:
        displayOptions()
        try:
            option = int(input("Please select from one of the numeric options above, or enter 0 to log out: "))

            if option == 0:
                loggedIn = False
                exit("GoodBye")
                break

            elif optionsDictionary[option] in optionFunctions:
                optionFunction = optionFunctions[optionsDictionary[option]]
                optionFunction()
            else:
                print("Option not found")
        except Exception as e:
            print(e)


def displayOptions():
    for i in optionsDictionary:
        print (i, " ", optionsDictionary[i])


def executeOption(option):
    option()

def orderFood():
    print("Order Food")

def viewOrderHistory():
    print("View Order History")

def viewAccountDetails():
    print("view Account Details")


optionFunctions = {
     ORDER_FOOD: orderFood,
     VIEW_ORDER: viewOrderHistory,
     VIEW_ACCOUNT: viewAccountDetails
}
