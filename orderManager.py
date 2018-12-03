from entities.Order import Order
from utilities.customerOrderFileWriter import customerOrderFileWriter

def orderManager(customer, restaurantDict):

    restaurant = selectRestaurant(restaurantDict)

    menuOrderItems = orderMenuItems(restaurant)
    if menuOrderItems:
        order = Order()
        order.setRestaurantName(restaurant.getRestaurantName())
        order.setCustomerId(customer.getID())
        orderPrice = 0.0
        for menuItem in menuOrderItems:
            order.setMenuItem(menuItem)
            orderPrice += float(menuItem.getItemPrice())
        order.setPrice(orderPrice)
    customer.addOrder(order)
    customerOrderFileWriter(order)


def selectRestaurant(restaurantDict):
    selectionActive = True

    while selectionActive:
        print("\nProvide number for associated restuarant, or input 0 to exit: \n")
        for key in restaurantDict:
            print(key, " ", restaurantDict[key].getRestaurantName())

        restInput = input( "\nEnter: ")
        if restInput in restaurantDict:
            return restaurantDict[restInput]
        elif restInput == "0":
            selectionActive = False
        else:
            print("Restaurant not found")

def orderMenuItems(restaurant):
    menuItem = restaurant.getMenu()
    orderList = []
    orderActive = True

    while orderActive:
        print("\nEnter the number for one of the following items, or enter 0 to complete order\n")

        for key, item in menuItem.items():
            print("{} -- {} : ${}".format((item.getMenuItemId()),(item.getItemName()),(item.getItemPrice())))

        orderInput = input("\nEnter: ")

        if orderInput in menuItem:
            print(menuItem[orderInput].getItemName(), " added to order")
            orderList.append(menuItem[orderInput])
        elif orderInput == "0":
            return orderList
        else:
            print("Invalid Selection")