from dataSetup import dataSetup
from systemManager import systemManager

def main():
    applicationData = dataSetup()
    if applicationData != None:
        restarauntDictionary = applicationData[2]
        customerDictionary = applicationData[0]
        accountDictionary = applicationData[1]

        systemManager(restarauntDictionary, customerDictionary, accountDictionary)

    else:
        print("An error has occured, please contact support")
main()