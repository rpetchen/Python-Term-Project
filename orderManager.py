from UserManagement import setContext
from optionHelper import optionHelper

def orderManagementSystem(restaurantDict, customerDict, accountDict):

    print("Welcome to Order Manager 3000! Please select from the following accounts: ")

    userContext = setContext(accountDict, customerDict)

    if userContext != None:
        print("Welcome {} {}".format((userContext.getFirstName()), (userContext.getLastName())))
        optionHelper()
    else:
        exit("Shutting down")



