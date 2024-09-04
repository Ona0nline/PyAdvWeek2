file = open('Lesson1/TODO.txt','r')

tasks = file.readlines()

for task in tasks:
  # Strip() packs the information neatly
  print(f"These are my tasks {task.strip()}")