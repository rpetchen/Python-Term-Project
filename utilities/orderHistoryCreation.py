import os.path, csv
from entities.Order import Order



def ordersSetup(menuDictionary, customerDictionary):

    orderHistoryDictionary = createOrderHistoryFromCSV(menuDictionary)
    if len(orderHistoryDictionary) > 0:
        assignOrdersToCustomers(customerDictionary, orderHistoryDictionary)


def createOrderHistoryFromCSV(menuDictionary):
    orderHistoryDictionary = {}

    ORDER_HISTORY_FILE = 'data_source/orderHistory.csv'

    if os.path.isfile(ORDER_HISTORY_FILE):
        f = open(ORDER_HISTORY_FILE)
        csv_f = csv.DictReader(f)

        for row in csv_f:
            try:
                ord_id = row['ord_id']
                cust_id = row['cust_id']
                rest_name = row['rest_name']
                menu_id = row['menu_id']
                keyTuple = (ord_id, cust_id)

                menuItem = menuDictionary[menu_id]


                if keyTuple in orderHistoryDictionary:
                    orderHistoryDictionary[keyTuple].setMenuItem(menuItem)
                    orderHistoryDictionary[keyTuple].setPrice(menuItem.getItemPrice())
                else:
                    order = Order()
                    order.setCustomerId(cust_id)
                    order.setPrice(menuItem.getItemPrice())
                    order.setMenuItem(menuItem)
                    order.setRestaurantName(rest_name)

                    orderHistoryDictionary[keyTuple] = order

            except Exception as e:
                print(e)
                break
        f.close()

    return orderHistoryDictionary


def assignOrdersToCustomers(customerDictionary, orderHistoryDicitonary):

    for customer, order in orderHistoryDicitonary.items():
        cust = customer[1]
        customerDictionary[cust].addOrder(order)