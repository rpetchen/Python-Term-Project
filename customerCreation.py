import csv
from Customer_Class import Customer
from Address_Class import Address
from Account_class import Account

customerDictionary = {}

def createCustomer():
    createCustomersFromCSV()
    createAndSetAddress()
    createAndSetAccountLogin()
    return customerDictionary

def createCustomersFromCSV():
    f = open('customerNames.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
            custID = row['Cust_ID']
            firstName = row['First_Name']
            lastName = row['Last_Name']
            newCustomer = Customer(custID)
            newCustomer.setName(firstName, lastName)
            customerDictionary[newCustomer.getID()] = newCustomer


def createAndSetAddress():
    f = open('customerAddress.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
        custID = row['cust_id']
        street = row['street']
        city = row['city']
        state = row['state']
        zip = row['zip']
        customerAddress = Address(street, city, state, zip)
        customerDictionary[custID].setAddress(customerAddress)


def createAndSetAccountLogin():
    f = open('customerAccounts.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
        custID = row['cust_id']
        accountName = row['account_name']
        accountPassword = row['account_password']
        customerAccount = Account(accountName, accountPassword)
        customerDictionary[custID].setAccount(customerAccount)



