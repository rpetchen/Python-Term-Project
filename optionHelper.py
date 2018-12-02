from OptionConstants import ORDER_FOOD, VIEW_ACCOUNT, VIEW_ORDER, optionsDictionary
from functionManager import orderFood, viewAccountDetails, viewOrderHistory

optionFunctions = {
     ORDER_FOOD: orderFood,
     VIEW_ORDER: viewOrderHistory,
     VIEW_ACCOUNT: viewAccountDetails
}

def optionHelper(customer, restaurantDict):
    customer = customer
    loggedIn = True
    while loggedIn:
        displayOptions()
        try:
            option = int(input("\nPlease select from one of the numeric options above, or enter 0 to log out: \n"))

            if option == 0:
                loggedIn = False
                exit("GoodBye")
                break

            elif optionsDictionary[option] in optionFunctions:
                optionFunction = optionFunctions[optionsDictionary[option]]
                if optionsDictionary[option] == VIEW_ORDER or optionsDictionary[option] == VIEW_ACCOUNT:
                    optionFunction(customer)
                elif optionsDictionary[option] == ORDER_FOOD:
                    optionFunction(customer, restaurantDict)
            else:
                print("Option not found")
        except Exception as e:
            print(e)


def displayOptions():
    for i in optionsDictionary:
        print (i, " ", optionsDictionary[i])



