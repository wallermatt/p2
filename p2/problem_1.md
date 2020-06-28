# problem_1 Finding the Floored Square Root of an Integer
- Expected time was O(log(n)) so I went for a binary search approach.
- The alogrithm makes an initial guess at the sqrt halfway between 1 and the number.
- If the number floor divided by the guess is greater than the guess, then the guess needs to be higher.
- However, if the next integer is higher than the actual square root then the current guess is the right one - this was the trickiest part.
- If the number floor divided by the guess is less than the guess, then the guess needs to be lower.
- When recalculating guesses I used the mid point +/- 1 as the new low/high.
- I suspect that the test examples supplied were chosen to give a false sense of security!
