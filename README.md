# Intercom Challenge

Hi Anisha and Todd! 😀

I have noticed that Intercomrades really [appreciate](https://www.intercom.com/blog/emoji-and-stickers-are-just-the-beginning/) [emojis](https://www.intercom.com/blog/emoji-ratings/), so I think you might also like [this memory card game 🃏 I have made here](https://github.com/AustinMoninger/memory-card-game), all about remembering emojis 👻.

And this was a lot of fun, thanks for the assignment. My `Proudest Achievement` answer is at the bottom of this README. The output of the running the program can be found in the `output.txt`.

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

### Proudest Achievement

_What's your proudest achievement? It can be a personal project or something you've worked on professionally. Just a short paragraph is fine, but we'd love to know why you're proud of it, what impact it had (If any) and any insights you took from it._

Feeling useful and solving *real* problems is a great experience. This summer at Nylas (a product that is like Twilio for email/calendar; Intercom is a customer!) I had a chance to do just that and grow my product development skills (building things people want!). 🧠

At Nylas, folks on our sales and marketing teams had no way of knowing how customers used our API (the core product). That data lived in our logs in Elasticsearch and only for 2 weeks because S3 storage is expensive. For an engineer to gather any meaningful insights from that log data they would have to figure out how to do Elasticsearch aggregations and would only have 2-week old data to work with.

I got to build a solution to this problem without just being fed requirements——I had to learn about the sales and marketing teams' workflows and how they find the information they want, if at all, and balance that with the feasibility of different engineering solutions. The result was a dashboard where a user could see metrics such as which customers were hitting which API endpoints, from which email providers, whether those were read or write operations, etc. This was something that was not possible before.

While I was still at Nylas, the sales team used the dashboard to be more informed about how a customer used the product prior to follow-up sales calls and closed a couple of deals because of it! The marketing team used the dashboard to provide more targeted email outreach to users in the free trial period. 💯

I was really proud of this project because I was laser-focused on my users' needs and iterated quickly based on their feedback. And the result of that focus showed! I grew a lot as an engineer and product developer through this experience and look forward to growing even more——hopefully as an intern at Intercom. 😄





