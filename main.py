from dataSetup import dataSetup
from orderManager import orderManagementSystem

def main():
    applicationData = dataSetup()
    if applicationData != None:
        restarauntDictionary = applicationData[2]
        customerDictionary = applicationData[0]
        accountDictionary = applicationData[1]

        orderManagementSystem( restarauntDictionary, customerDictionary, accountDictionary)

    else:
        print("An error has occured, please contact support")
main()