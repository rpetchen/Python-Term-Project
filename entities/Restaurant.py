

class Restaurant:
    def __init__(self, restaurantId, restaurantName):
        self.restaurantName = restaurantName
        self.restaurantId = restaurantId
        self.menu = {}

    def getId(self):
        return self.restaurantId

    def addMenuItem(self, menuItem):
        self.menu[menuItem.getMenuItemId()] = menuItem

    def getMenu(self):
        if len(self.menu) > 0:
            return self.menu
        else:
            return "No menu"

    def setAddress(self, address):
        self.address = address

    def getRestaurantInfo(self):
        print (self.restaurantName, "has the following items")
        menuDict = self.getMenu()
        for i in menuDict:
            menu = menuDict[i].getItemName()
            print (" ---------------", menu)

