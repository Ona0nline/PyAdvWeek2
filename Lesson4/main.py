import csv

with open('Lesson4/cities.csv','r') as file:
  csv_file = csv.reader(file)
  
try:
  
  for lines in csv_file:
    print(f"It is {lines[1]} degrees celsius in {lines[0]}.")
    
except IndexError:
  print("Line empty")
  
except ValueError:
  print("File is closed")
    
