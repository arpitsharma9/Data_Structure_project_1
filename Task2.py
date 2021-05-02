"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict
call_time=defaultdict(int)

for call in calls:
		 
    call_time[call[0]] += int(call[3])
    call_time[call[1]] += int(call[3])

max_val = max(call_time.items(), key=lambda x: x[1])
longest_call_time=max_val[1]
tel_number=max_val[0]

print(f"{tel_number} spent longest time, {longest_call_time} seconds, on the phone during September 2016.")
