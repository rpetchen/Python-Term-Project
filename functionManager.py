from orderManager import orderManager

def orderFood(customer, restaurantDict):
    orderManager(customer, restaurantDict)

def viewOrderHistory(userContext):
    userOrders = userContext.getOrders()
    print("\nYour details are below: ")
    print("-------------------------------------------")
    if len(userOrders) > 0:
        for order in userOrders:
            listItems = [i.getItemName() for i in order.getMenuItems()]
            print("\nYou ordered from the following restaurant: {}".format(order.getRestaurantName()))
            print("The following items were ordered: ", end="")
            for i in listItems:
                print (i, end = ",")
            print("\nYour total for this order was ${}".format(order.getPrice()))
            print("\n")
    else:
        print("User has no previous orders!")
    print("""-------------------------------------------
Returning to options\n""")

def viewAccountDetails(userContext):
    print("\nYour details are below: ")
    print("-------------------------------------------")
    print(userContext.getAccountDetails())
    print("""-------------------------------------------
Returning to options\n""")