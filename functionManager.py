from orderManager import orderManager

def orderFood(customer, restaurantDict):
    orderManager(customer, restaurantDict)

def viewOrderHistory(userContext):
    userOrders = userContext.getOrders()
    print("\nYour details are below: ")
    print("-------------------------------------------")
    if len(userOrders) > 0:
        for i in userOrders:
            print(i)
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