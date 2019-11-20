import demjson
import argparse
import sys
from math import pi, sin, cos, acos

# The global average radius of the Earth in kilometers
EARTH_RADIUS_KM = 6371

# Default values for command line arguments
CUSTOMER_LIST_FILE_NAME = 'Customer List.txt'
DISTANCE_TO_CENTER = 100
CENTER_LAT = 37.788802
CENTER_LONG = -122.4025067


def get_radians_from_degrees(degrees):
    """
    Converts from degrees to radians.
    """
    return degrees * pi / 180

def get_earth_arc_length(lat_1, long_1, lat_2, long_2):
    """
    Computes the distance between two points on the surface of the Earth, 
    measured along the surface of the Earth.
    """
    delta_long = abs(long_1 - long_2)
    term_1 = sin(lat_1) * sin(lat_2)
    term_2 = cos(lat_1) * cos(lat_2) * cos(delta_long)
    central_angle = acos(term_1 + term_2)
    return EARTH_RADIUS_KM * central_angle

def get_customer_list(customer_list_file_name):
    """
    Reads from the input file to form the list of customer data.
    """
    customer_list = []
    with open(customer_list_file_name) as text_file:
        for line in text_file:
            customer_data = demjson.decode(line)
            customer_list.append(customer_data)
    return customer_list

def get_nearby_customers(customer_list, distance_to_center, center_lat, center_long):
    """
    Finds the nearby customers to the center.
    """
    center_lat_radians = get_radians_from_degrees(center_lat)
    center_long_radians = get_radians_from_degrees(center_long)
    nearby_customers = []

    for customer_data in customer_list:
        lat_radians = get_radians_from_degrees(float(customer_data['latitude']))
        long_radians = get_radians_from_degrees(float(customer_data['longitude']))
        arc_length = get_earth_arc_length(
            lat_radians, long_radians, center_lat_radians, center_long_radians)
        if arc_length <= distance_to_center:
            nearby_customers.append((customer_data['user_id'], customer_data['name']))

    return nearby_customers

def get_sorted_customers_by_user_id(customers):
    """
    Returns the list of customers sorted by the user_id.
    """
    return sorted(customers, key=lambda x: x[0])

def parse_args(args):
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--customer_data_filename', default=CUSTOMER_LIST_FILE_NAME, help='File with customer data')
    parser.add_argument('-lat', '--latitude', default=CENTER_LAT, type=float, help='Latitude of the center location to be compared with the customer location')
    parser.add_argument('-long', '--longitude', default=CENTER_LONG, type=float, help='Longitude of the center location to be compared with the customer location')
    parser.add_argument('-d', '--distance', default=DISTANCE_TO_CENTER, type=float, help='Include all customers within this distance of the center')
    return parser.parse_args(args)

def main():
    parser = parse_args(sys.argv[1:])
    customer_list = get_customer_list(parser.customer_data_filename)
    nearby_customers = get_nearby_customers(customer_list, parser.distance, parser.latitude, parser.longitude)
    sorted_customers = get_sorted_customers_by_user_id(nearby_customers)

    for user_id, name in sorted_customers:
        print(user_id, name)


if __name__ == '__main__':
    main()
