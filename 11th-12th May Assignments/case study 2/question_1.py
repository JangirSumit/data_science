import csv

csv_data = []

with open("bank-data.csv")as f:
    reader = csv.DictReader(f)
    csv_data = [r for r in reader]

###### Enhancement Codes #######
# Max and Min age for loan eligibility
ages = list([float(data['age']) for data in csv_data])

# Dictionary of max min ages
max_min_age = {"max": max(ages), "min": min(ages)}

print("Max age for loan eligibility " + str(max_min_age['max']))
print("Min age for loan eligibility " + str(max_min_age['min']))


###### Required Codes ########

# Unique Jobs
unique_jobs = set([data['job'].lower() for data in csv_data])
print("Unique jobs")
print(unique_jobs)

print("****** Bank of Portugal Portal *******")
print("Check your eligibility for loan")

# While loop to check profession without ending except user ends
while True:
    user_input = input("Enter END/end to quit else continue>>> ")

    if user_input.lower() != "end":
        print("Enter the profession")
        client_profession = input(">>> ").strip()

        # Profession check with case insensitive by making it lower/upper
        if client_profession.lower() in unique_jobs:
            print("Given profession exists in list")
            print("\n")
            print(
                "Please enter the below details to check whether you are eligible or not for Loan")
            client_age = input("Age >>> ").strip()
            marital_status = input(
                "Marital Status [Married/Single/Divorced] >>> ").strip()
            print("\n")

            check_eligibility = set([data['y'] for data in csv_data if (int(data['age']) == int(client_age) and data['job'].lower(
            ) == client_profession.lower() and data['marital'].lower() == marital_status.lower())])

            if "yes" in check_eligibility:
                print("Congratulations!! You are eligible for loan.")
            else:
                print("Sorry!! You are not eligible for loan.")
        else:
            print("Given profession does not exist in list")
    else:
        break
