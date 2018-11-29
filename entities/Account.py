class Account:
    def __init__(self, accountName, accountPassword, cust_id):
        self.accountName = accountName
        self.accountPassword = accountPassword
        self.custId = cust_id

    def getAccountName(self):
        return self.accountName

    def getPassword(self):

        return self.accountPassword

    def getCustId(self):
        return self.custId