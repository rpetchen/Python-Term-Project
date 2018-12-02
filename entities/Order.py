class Order:
    def __init__(self):
        self.restaurantName = ""
        self.menuItemsName = []
        self.customerId = 0
        self.price = 0

    def setRestaurantName(self, restaurantName):
        self.restaurantName = self.restaurantName

    def setMenuItem(self, menuItemsName):
        self.menuItemsName = menuItemsName

    def setCustomerId(self, customerId):
        self.customerId = customerId

    def setPrice(self, price):
        self.price = price

    def sefCustomerId(self, customerId):
        self.customerId = customerId

    def getPrice(self):
        return self.price

    def getMenuItemsName(self):
        return self.menuItemsName

    def getCustomerId(self):
        return self.customerId

    def getRestaurantName(self):
        return self.restaurantName