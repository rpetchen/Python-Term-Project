import os.path, csv

def customerOrderFileWriter(order):
    row_count = 0
    ORDER_HISTORY_FILE = 'data_source/orderHistory.csv'
    fileExists = os.path.isfile(ORDER_HISTORY_FILE)

    if fileExists is False:
        print("")
        with open(ORDER_HISTORY_FILE, "w", newline='') as f:
            writer = csv.writer(f)
            row = ['ord_id', 'cust_id', 'rest_name', 'menu_id']
            writer.writerow(row)
        f.close()

    row_count = sum(1 for line in open(ORDER_HISTORY_FILE))

    with open (ORDER_HISTORY_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        for menuItem in order.getMenuItems():
            row = [row_count, order.getCustomerId(), order.getRestaurantName(), menuItem.getMenuItemId()]
            writer.writerow(row)

        f.close()

