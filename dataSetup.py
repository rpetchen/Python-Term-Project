from utilities.customerCreation import createCustomer
from utilities.restaurantCreation import restaurantSetup
from utilities.orderHistoryCreation import ordersSetup

def dataSetup():

    isDataSetup = False


    try:
        customer_account_list = createCustomer()
        customerDictionary, accountDictionary = customer_account_list[0], customer_account_list[1]


        restaurantAccounts = restaurantSetup()
        restaurantDictionary, menuDictionary   = restaurantAccounts[0], restaurantAccounts[1]

        ordersSetup(menuDictionary, customerDictionary)
        applicationData = (customerDictionary, accountDictionary, restaurantDictionary)

        isDataSetup = True

    except RuntimeError as e:
        print (e)
    finally:
        if isDataSetup:
            return applicationData
        else:
            return None
