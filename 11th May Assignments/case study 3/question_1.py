from customer import Customer
import csv
import re

csv_data = []

with open("FairDealCustomerData.csv") as f:
    reader = csv.reader(f)
    csv_data = list([r for r in reader])

# Full name customers
fullname_data = list([data for data in csv_data if re.match(r"([a-zA-Z].+)\s(\w+)\s(\w+)", data[1].strip(), re.IGNORECASE)])

# Adding cutomers data to GoodsKart data
customerList = []
for data in fullname_data:
    customerList.append(Customer(productname = data[0].strip(), customername = data[1].strip(), isblacklisted = bool(data[2].strip())))

# Check whether the customer is allowed to create the order or not?

customer = Customer(productname = "XYZ", customername = "Sumit Jangir", isblacklisted = True)

customer.createOrder()