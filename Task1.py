"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print(calls[1][:])
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
records=set()

for text in texts:
    records.add(text[0])
    records.add(text[1])

for call in calls:
    records.add(call[0])
    records.add(call[1])    

print(f"There are {len(records)} different telephone numbers in the records.")

