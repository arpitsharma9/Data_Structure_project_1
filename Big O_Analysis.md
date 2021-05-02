# Run time analysis (Worst Case Big-O Notation)
## Task 0 

There are 2 print statements for printing "First record of texts" and "Last record of calls" in the code. So, as the run time does not change as a function of the input, the run time for this code is constant. 
So, worst case Big O = O(1)

## Task 1

The objective of this task is to find unique telehphone mumbers in the text and call records. So, for finding those numbers we used for loops. We iterate n times(# of records - text or call) in both loops. Also, for large values of n the other terms become irrelevant in their size and therefore can be discarded. 
Big O for this task is 2n and can be represnted as O(n).

## Task 2
The objective is to find the telephone number which spent the longest time on the phone
during the period. 
We iterate n times in "for loop".
we also iterate through dict n items for identify the longest call time along with telephone number using max() method.
Other terms become irrelevant for large value of n and therefore can be discarded. 
Big O for this task is 2n and can be represnted as O(n).

## Task 3
The objective is to find solution for beblow tasks-
Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
We iterate n times in "for loop".
sorted method used in code has a worst-case time-complexity of O(n log n)
Another for loop is having time complexity of O(n)
Other terms become irrelevant for large value of n and therefore can be discarded. 
Big O for this task is 2n+nlogn and can be represnted as O(nlogn) after omiting 2n.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore.

There is one "for loop" which has time complexity of n.
so big O of Part B is n. 

The overall Big O for this problem is O(nlogn)

## Task 4
The objective is to identify numbers that might be doing telephone marketing.

there are 2 "for loops" in this problem which have time complexity of 2n.
Other terms become irrelevant for large value of n and therefore can be discarded. 
Big O for this task is 2n and can be represnted as O(n).
