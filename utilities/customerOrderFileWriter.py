import os.path, csv

def customerOrderFileWriter(order):
    row_count = 0
    ORDER_HISTORY_FILE = 'data_source/orderHistory.csv'
    fileExists = os.path.isfile(ORDER_HISTORY_FILE)

    if fileExists is False:
        print("")
        with open(ORDER_HISTORY_FILE, "w") as f:
            writer = csv.writer(f)
            row = ['ord_id', 'cust_id', 'rest_name', 'menu_item', 'order_total']
            writer.writerow(row)
        f.close()

    row_count = sum(1 for line in open(ORDER_HISTORY_FILE))

    with open (ORDER_HISTORY_FILE, 'a') as f:
        writer = csv.writer(f)
        for menuItem in order.getMenuItemsName():
            row = [row_count, order.getCustomerId(), order.getRestaurantName, menuItem, order.getPrice()]
            writer.writerow(row)
            row_count += 1
        f.close()

