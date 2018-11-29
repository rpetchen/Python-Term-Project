import csv
from entities.Customer import Customer
from entities.Address import Address
from entities.Account import Account


def createCustomer():
    customerDictionary = createCustomersFromCSV()
    createAndSetAddress(customerDictionary)
    accountDictionary = createAndSetAccountLogin(customerDictionary)
    return [customerDictionary, accountDictionary]

def createCustomersFromCSV():
    customerDictionary = {}
    isDataValid = True

    f = open('data_source/customerNames.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
        try:
            custID = row['cust_id']
            firstName = row['first_name']
            lastName = row['last_name']
            newCustomer = Customer(custID)
            newCustomer.setName(firstName, lastName)
            customerDictionary[newCustomer.getID()] = newCustomer
        except KeyError as e:
            raise RuntimeError("{} is a required field when creating customers".format(e.__str__()))
            break

    if isDataValid:
        return customerDictionary
    else:
        raise RuntimeError("Customer Data not set up")

def createAndSetAddress(customerDictionary):
    f = open('data_source/customerAddress.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
        try:
            custID = row['cust_id']
            street = row['street']
            city = row['city']
            state = row['state']
            zip = row['zip']
            customerAddress = Address(street, city, state, zip)
            customerDictionary[custID].setAddress(customerAddress)
        except KeyError as e:
            raise RuntimeError("{} is a required field when creating address".format(e.__str__()))
            break


def createAndSetAccountLogin(customerDictionary):

    accountDictionary = {}
    isDataValid = True

    f = open('data_source/customerAccounts.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
        try:
            custID = row['cust_id']
            accountName = row['account_name']
            accountPassword = row['account_password']
            customerAccount = Account(accountName, accountPassword, custID)
            customerDictionary[custID].setAccount(customerAccount)
            accountDictionary[accountName] = customerAccount
        except KeyError as e:
            isDataValid = False
            raise RuntimeError("{} is a required field when creating account".format(e.__str__()))
            break
    if isDataValid:
        return accountDictionary
    else:
        raise RuntimeError("Customer Data not set up")


