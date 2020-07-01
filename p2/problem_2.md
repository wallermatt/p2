# problem_2 Search in a Rotated Sorted Array
- O(log(n)) expected performance so I used a binary search algorithm.
- If the section between start and end was sorted correctly (i.e. didn't contain the pivot) then could proceed as a normal binary search.
- If there is a pivot in the list section then can determine which side of pivot mid and number are on.
- If they're both on the same side, then can binary search as normal.
- if they're on different sides then normal binary search behaviour should be reversed.
