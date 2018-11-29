from utilities.customerCreation import createCustomer
from utilities.restaurantCreation import restaurantSetup

customerDictionary = {}
accountDictionary = {}
restaurantDictionary = {}

def dataSetup():
    global customerDictionary, accountDictionary, restaurantDictionary
    isDataSetup = False
    try:
        customer_account_list = createCustomer()
        customerDictionary = customer_account_list[0]
        accountDictionary = customer_account_list[1]
        restaurantDictionary = restaurantSetup()

        isDataSetup = True

    except RuntimeError as e:
        print (e.__str__())
    finally:
        return isDataSetup


dataSetup()