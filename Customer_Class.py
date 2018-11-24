class Customer:
    def __init__(self, cust_id):
        self.cust_id = cust_id

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
        if len(self.order < 1):
            self.order = []
        self.order.append(order)

    def getCustomer(self):
        return "Customer {} {} lives at {}  and the account is {}". \
            format((self.firstName),(self.lastName),(self.address.getAddress()),(self.account.getAccountName()))
