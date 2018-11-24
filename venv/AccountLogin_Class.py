class AccountLogin:
    def __init__(self, accountName, accountPassword):
       self.accountName = accountName
       self.accountPassword = accountPassword

    def validateAccount(self, accountPassword):
        if accountPassword == self.accountPassword:
            return True
        else:
            return False
