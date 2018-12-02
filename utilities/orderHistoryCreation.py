import os.path, csv
from entities.Order import Order



def orodersSetup():
    createOrderHistoryFromCSV()


def createOrderHistoryFromCSV():

    ORDER_HISTORY_FILENAME = 'data_source/restaurantNames.csv'
    os.path.isfile(ORDER_HISTORY_FILENAME)
    f = open('data_source/restaurantNames.csv')
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



