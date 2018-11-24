import customerCreation

def main():
    customerDictionary = customerCreation.createCustomer()
    for i in customerDictionary:
        print(customerDictionary[i].getCustomer())

main()