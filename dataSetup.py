from utilities.customerCreation import createCustomer
from utilities.restaurantCreation import restaurantSetup

def dataSetup():

    isDataSetup = False


    try:
        customer_account_list = createCustomer()
        customerDictionary = customer_account_list[0]
        accountDictionary = customer_account_list[1]
        restaurantDictionary = restaurantSetup()

        applicationData = (customerDictionary, accountDictionary, restaurantDictionary)
        isDataSetup = True

    except RuntimeError as e:
        print (e.__str__())
    finally:
        if isDataSetup:
            return applicationData
        else:
            return None


dataSetup()