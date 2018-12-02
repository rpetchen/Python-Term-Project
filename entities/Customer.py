from utilities.customerOrderFileWriter import customerOrderFileWriter

class Customer:
    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.orders = []

    def setName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getID(self):
        return self.cust_id

    def setAddress(self, address):
        self.address = address

    def setAccount(self, account):
        self.account  = account

    def addOrder(self, order):
        self.orders.append(order)
        customerOrderFileWriter(order)

    def getOrders(self):
       return self.orders


    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAccountDetails(self):
        return "{} {} at address {} {} {} ".format((self.firstName),(self.lastName), \
                                                  (self.address.street), (self.address.city), (self.address.state) )