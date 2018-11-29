import csv
from entities.MenuItem import MenuItem
from entities.Address import Address
from entities.Restaurant import Restaurant


def restaurantSetup():
    restuarantDictionary = createRestaurantFromCSV()
    createRestaurantMenuFromCSV(restuarantDictionary)
    return restuarantDictionary


def createRestaurantFromCSV():

    restaurantDictionary = {}
    isDataValid = True

    f = open(r'C:\Users\Ryan\PycharmProjects\PythonTermProject\data_source\restaurantNames.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
        try:
            restID = row['rest_id']
            rest_name = row['rest_name']
            newRestaurant = Restaurant(restID, rest_name)
            restaurantDictionary[newRestaurant.getId()] = newRestaurant
        except KeyError as e:
            isDataValid = False
            raise RuntimeError("Restaurant Error - {} is a required field when creating restaurants".format(e.__str__()))
            break

    if isDataValid:
         return restaurantDictionary
    else:
         raise RuntimeError("Restaurant Data not set up")


def createRestaurantMenuFromCSV(restuarantDictionary):
    isDataValid = True

    f = open(r'C:\Users\Ryan\PycharmProjects\PythonTermProject\data_source\menuItems.csv')
    csv_f = csv.DictReader(f)

    for row in csv_f:
        try:
            menuId = row['menu_id']
            rest_id = row['rest_id']
            item_name = row['item_name']
            item_price = row['item_price']
            newMenuItem = MenuItem(menuId, item_name, item_price)
            restuarantDictionary[rest_id].addMenuItem(newMenuItem)
        except Exception as e:
            print(e)
            raise RuntimeError("Menu Error - {} is a required field when creating restaurants".format(e.__str__()))
            break


restaurantSetup()