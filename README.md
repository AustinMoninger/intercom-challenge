### The Problem

We have some customer records in a text file (Customer List.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our SF office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

### Before Running the Program

Make sure that you have Python 3 🐍 installed before attempting to run the program.

Then you can run the following in the project directory to install all necessary dependencies.

    pip3 install -r requirements.txt

The only dependency in this requirements file is `demjson`. Since the provided JSON data is dirty (keys do not have double quotes), the function `demjson.decode` helped me parse the customer data.

### Running the Program

To run the program, you can run the following in the project directory.

    python3 nearby_customers.py

This will output all the customers and their associated id's in ascending order.

There are also some optional command line arguments you can provide like `--latitude`,  `--longitude`,  `--customer_data_filename`,  and `--distance`. Try running `python3 nearby_customers.py --help` to learn more. Here is an example.

    python3 nearby_customers.py --latitude=27.35 --longitude=120.43 --customer_data_filename='fake.txt' --distance=350

This will show you the customers that are within `distance` kilometers of the center at `latitude`, `longitude` with customer data from `fake.txt`. 🌍

### Testing the Program

In order to run the tests, you can run the following in the project directory.

    python3 nearby_customers_test.py





