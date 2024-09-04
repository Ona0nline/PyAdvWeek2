import csv

with open('Lesson2/temperatures.csv','r') as file:
  csvFile = csv.reader(file)
  
  for lines in csvFile:
    print(f"It is {lines[1]} degrees celsius in {lines[0]}")