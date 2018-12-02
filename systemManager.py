from UserManagement import setContext
from optionHelper import optionHelper

def systemManager(restaurantDict, customerDict, accountDict):

    print("Welcome to Order Manager 3000!")

    userContext = setContext(accountDict, customerDict)

    if userContext != None:
        print("\nWelcome {} {}\n".format((userContext.getFirstName()), (userContext.getLastName())))
        optionHelper(userContext, restaurantDict)
    else:
        exit("Shutting down")



