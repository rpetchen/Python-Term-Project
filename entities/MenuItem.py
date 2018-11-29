class MenuItem:
    def __init__(self, menuItemId, itemName, itemPrice):
        self.menuItemId = menuItemId
        self.itemName = itemName
        self.itemPrice = itemPrice

    def getMenuItemId(self):
        return self.menuItemId

    def setItemName(self, itemName):
        self.itemName = itemName

    def setItemPrice(self, itemPrice):
        self.itemPrice = itemPrice

    def getItemName(self):
        return self.itemName

    def getItemPrice(self):
        return self.itemPrice