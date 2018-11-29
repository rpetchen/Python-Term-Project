from dataSetup import dataSetup, restaurantDictionary, customerDictionary, accountDictionary
from orderManager import orderManagementSystem

def main():
    isDataSetup = dataSetup()
    if isDataSetup:
       orderManagementSystem(restaurantDictionary, customerDictionary, accountDictionary)

    else:
        print("An error has occured, please contact support")
main()