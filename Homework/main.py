import csv

with open('Homework/customers.csv','r') as file:
  customer_base = csv.reader(file)
  
  for customer in customer_base:
    print(f"Customer #{customer[0]}, {customer[2]} {customer[3]},{customer[9]}.")
    