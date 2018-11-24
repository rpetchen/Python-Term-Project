class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.state = state
        self.city = city
        self.zip = zip

    def getAddress(self):
        return "{} {} {} {}".format((self.street),(self.city),(self.state),(self.zip))