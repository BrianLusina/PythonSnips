Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.


# Solution

Knowing that, the brute force solution is to simply keep an array of all the stock prices for all days, then simply start with the current day and decrement the current index while the current is greater than previous days. Return the size - decremented index for the # of days.

But, that's not very efficient. The problem warns about runtime. So two things, first, at each call we are doing work by checking out many days the current value is greater than the previous values, so we should save that. Second, do we really need every historic price? No, we only need the larger rightmost price, the smaller prices before those do not matter, so we can collapse them.

Take the example of $10, $2, $4, $5 and the new value of $7, we have to check 7>5, 7>5, 7>5 before stopping at 10!<7... BUT we already now that 5>4, 5>2 ,5!>10 when we calculated for 5 (before we even got the 7), we aleady knew that 5 was greater than the 2 elements before it. Does it matter that the elements were $2, and $4? no, only that they are some number less then $5.

So, before evaluating $7, when the new number was $5, we could have evaluated $10, <$5, <$5, $5, and just keep a counter to the larget elm and number of lessor elms(2+1). For example [[10,1], [5,3]]. If our new value is $7, we check it against the prev value 5, it's greater and 5 also represents a group of 3 lessor elements, so rather then check them, just add 3 to our counter. We stop on the next one, 10. Now we can collapse the 7 with the < values before it, so we are left with [10,1], [7,4] for the next number. No need to save the numbers between the last highest, and the current high number, just their count.