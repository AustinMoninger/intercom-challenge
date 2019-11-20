import unittest
from nearby_customers import *

class TestRunner(unittest.TestCase):

    def test_get_radians_from_degrees(self):
        self.assertEqual(get_radians_from_degrees(-360), -2 * pi)
        self.assertEqual(get_radians_from_degrees(-270), -3 * pi / 2)
        self.assertEqual(get_radians_from_degrees(-180), -pi)
        self.assertEqual(get_radians_from_degrees(-90), -pi / 2)
        self.assertEqual(get_radians_from_degrees(0), 0)
        self.assertEqual(get_radians_from_degrees(90), pi / 2)
        self.assertEqual(get_radians_from_degrees(180), pi)
        self.assertEqual(get_radians_from_degrees(270), 3 * pi / 2)
        self.assertEqual(get_radians_from_degrees(360), 2 * pi)

        # Based on Google's degrees to radians calculator
        self.assertAlmostEqual(get_radians_from_degrees(14.43), 0.25185101)
        self.assertAlmostEqual(get_radians_from_degrees(-265.3443), -4.6311316864)

    def test_get_earth_arc_length(self):
        # Based on this calculator that takes in degrees and outputs up to 6 decimal places:
        # https://keisan.casio.com/exec/system/1224587128
        decimal_places = 6

        self.assertAlmostEqual(get_earth_arc_length(
            get_radians_from_degrees(37.788802),
            get_radians_from_degrees(37.788802),
            get_radians_from_degrees(37.788802),
            get_radians_from_degrees(37.788802)), 0, decimal_places)

        self.assertAlmostEqual(get_earth_arc_length(
            get_radians_from_degrees(37.788802), 
            get_radians_from_degrees(-122.4025067),
            get_radians_from_degrees(37.7451022), 
            get_radians_from_degrees(-122.238335)), 15.226919, decimal_places)

        self.assertAlmostEqual(get_earth_arc_length(
            get_radians_from_degrees(432.4322),
            get_radians_from_degrees(-122.5478),
            get_radians_from_degrees(37.38387),
            get_radians_from_degrees(-333.2357)), 7575.1193429, decimal_places)

    def test_get_customer_list(self):
        self.assertTrue(get_customer_list(CUSTOMER_LIST_FILE_NAME))
        self.assertRaises(FileNotFoundError, get_customer_list, 'fake.txt')

    def test_get_nearby_customers(self):
        customer_list = [{'latitude': '37.761389', 'user_id': 30, 'name': 'Nick Enright', 'longitude': '-140.2875'},
                         {'latitude': '38.080556', 'user_id': 23, 'name': 'Eoin Gallagher', 'longitude': '-122.361944'}, 
                         {'latitude': '36.833502', 'user_id': 25, 'name': 'David Behan', 'longitude': '-110.522366'}]
        center_lat = 34.5466
        center_long = -120.4843

        # print(get_nearby_customers(customer_list, distance_to_center, center_lat, center_long))

        self.assertEqual(get_nearby_customers(customer_list, 0, center_lat, center_long), [])
        self.assertEqual(get_nearby_customers(customer_list, 600, center_lat, center_long), [(23, 'Eoin Gallagher')])
        self.assertEqual(get_nearby_customers(customer_list, 1000, center_lat, center_long), [(23, 'Eoin Gallagher'), (25, 'David Behan')])
        self.assertEqual(get_nearby_customers(customer_list, 10000, center_lat, center_long), [(30, 'Nick Enright'), (23, 'Eoin Gallagher'), (25, 'David Behan')])

    def test_get_sorted_customers_by_user_id(self):
        customers = [(12, 'Christina McArdle'), (8, 'Eoin Ahearn'), (26, 'Stephen McArdle'), 
                    (6, 'Theresa Enright'), (4, 'Ian Kehoe'), (5, 'Nora Dempsey')]
        sorted_customers = [(4, 'Ian Kehoe'), (5, 'Nora Dempsey'), (6, 'Theresa Enright'),
                            (8, 'Eoin Ahearn'), (12, 'Christina McArdle'), (26, 'Stephen McArdle')]

        self.assertEqual(get_sorted_customers_by_user_id(customers), sorted_customers)

        single_customer = [(1, 'Austin')]

        self.assertEqual(get_sorted_customers_by_user_id(single_customer), single_customer)


    def test_parse_args(self):
        empty_parser = parse_args([])
        self.assertEqual(empty_parser.latitude, CENTER_LAT)
        self.assertEqual(empty_parser.longitude, CENTER_LONG)
        self.assertEqual(empty_parser.customer_data_filename, CUSTOMER_LIST_FILE_NAME)
        self.assertEqual(empty_parser.distance, DISTANCE_TO_CENTER)

        lat = 33.3244
        long = -170.3675
        filename = 'data.txt'
        distance = 400

        # Long versions of the arguments
        long_args_parser = parse_args(['--latitude={}'.format(lat), 
                                       '--longitude={}'.format(long),
                                       '--customer_data_filename={}'.format(filename),
                                       '--distance={}'.format(distance)])
        self.assertEqual(long_args_parser.latitude, lat)
        self.assertEqual(long_args_parser.longitude, long)
        self.assertEqual(long_args_parser.customer_data_filename, filename)
        self.assertEqual(long_args_parser.distance, distance)

        # Short versions of the arguments
        short_args_parser = parse_args(['-lat={}'.format(lat),
                                       '-long={}'.format(long),
                                       '-f={}'.format(filename),
                                       '-d={}'.format(distance)])
        self.assertEqual(short_args_parser.latitude, lat)
        self.assertEqual(short_args_parser.longitude, long)
        self.assertEqual(short_args_parser.customer_data_filename, filename)
        self.assertEqual(short_args_parser.distance, distance)

        # Mixed bag of optional args, short versions, and long versions
        mixed_args_parser = parse_args(['-lat={}'.format(lat),
                                        '--longitude={}'.format(long)])
        self.assertEqual(mixed_args_parser.latitude, lat)
        self.assertEqual(mixed_args_parser.longitude, long)
        self.assertEqual(mixed_args_parser.customer_data_filename, CUSTOMER_LIST_FILE_NAME)
        self.assertEqual(mixed_args_parser.distance, DISTANCE_TO_CENTER)


if __name__ == '__main__':
    unittest.main()
