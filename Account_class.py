class Account:
    def __init__(self, accountName, accountPassword):
        self.accountName = accountName
        self.accountPassword = accountPassword

    def getAccountName(self):
        return self.accountName