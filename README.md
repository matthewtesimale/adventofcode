# adventofcode challenges

These are my solutions to the yearly Advent of Code challenges put on by Eric Wastl.
(https://adventofcode.com/2022/about)

## Day 1
Not completed

## Day 2
I decided to take a more 'file upload' approach to be able to separate the data from the processing program.
Initially, I wrote the code to include only one function necessary, but often times you want to separate functions
according to their respective task.

So, in the "_clean" program, I separated the victor determination from the scoring.
I also improved the logic with the determineVictor function by utilizing an 'in' operator as opposed to multiple
if statements. This increased the number of lines but hopefully provides and easier to read experience. However, it can be noted that in Part 2, the results was determined, so a single function would suffice.
Added doc strings to each function for more clarity.

**CAUTION:** The guide in PART 1 provides that your opponents entry comes first, however, I wrote the function to test against
the FIRST argument winning or losing. Thus, the reversed() and tuple() functions over-utilized in the for loop thru each line.

(https://adventofcode.com/2022/day/2)