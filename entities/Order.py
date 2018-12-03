class Order:
    def __init__(self):
        self.restaurantName = ""
        self.menuItems = []
        self.customerId = 0
        self.price = 0.0

    def setRestaurantName(self, restaurantName):
        self.restaurantName = restaurantName

    def setMenuItem(self, menuItem):
        self.menuItems.append(menuItem)

    def setCustomerId(self, customerId):
        self.customerId = customerId

    def setPrice(self, price):

        self.price += float(price)

    def sefCustomerId(self, customerId):
        self.customerId = customerId

    def getPrice(self):
        return self.price

    def getMenuItems(self):
        return self.menuItems

    def getCustomerId(self):
        return self.customerId

    def getRestaurantName(self):
        return self.restaurantName