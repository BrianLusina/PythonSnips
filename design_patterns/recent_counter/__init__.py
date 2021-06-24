from collections import deque


class RecentCounter(object):
    """
    Iteration over a Sliding Window

    First of all, let us clarify the problem a bit. We are given a sequence of ping calls, i.e. [t_1, t_2, t_3, ... t_n]
    ordered by the chronological order of their arrival time.

    Given the current ping call ti, we are asked to count the number of previous calls that fall in the range of
    [ti - 3000, \ti]

    This is how we can reformulate the problem with the basic data structure such as Array. Note, the sequence of calls
     is ever-increasing, and we are given the call one at a time.

    The idea is that we can use a container such as array or list to keep track of all the incoming ping calls.
    At each occasion of ping(t) call, first we append the call to the container, and then starting from the current call
     we iterate backwards to count the calls that fall into the time range of [t-3000, t].

     One observation is that the sequence is ever-growing, so is our container.

     On the other hand, once the ping calls become outdated, i.e. out of the scope of [t-3000, t], we do not need to
     keep them any longer in the container, since they will not contribute to the solution later.

     As a result, one optimization that we could do is that rather than keeping all the historical ping calls in the
     container, we could remove the outdated calls on the go, which can avoid the overflow of the container and reduce
     the memory consumption to the least.

     In summary, our container will function like a sliding window over the ever-growing sequence of ping calls.

     Based on the above description, the list data structure seems to be more fit as the container for our tasks,
     than the array. Because the list is more adapted for the following two operations:

        Appending: we will append each incoming call to the tail of the sliding window.
        Popping: we need to pop out all the outdated calls from the head of the sliding window.

    Algorithm

    To implement the sliding window, we could use the deque

    Then the ping(t) function can be implemented in two steps:
        Step 1): we append the current ping call to the tail of the sliding window.
        Step 2): starting from the head of the sliding window, we remove the outdated calls, until we come across a
        still valid ping call.

    As a result, the remaining calls in the sliding window are the ones that fall into the range of [t - 3000, t].

    Complexity Analysis

    First of all, let us estimate the upper-bound on the size of our sliding window. Here we quote an important
    condition from the problem description: "It is guaranteed that every call to ping uses a strictly larger value of t
    than before." Based on the above condition, the maximal number of elements in our sliding window would be 30003000,
    which is also the maximal time difference between the head and the tail elements.

    Time Complexity: O(1)

        The main time complexity of our ping() function lies in the loop, which in the worst case would run 3000
        iterations to pop out all outdated elements, and in the best case a single iteration.

        Therefore, for a single invocation of ping() function, its time complexity is O(3000)=O(1).

        If we assume that there is a ping call at each timestamp, then the cost of ping() is further amortized,
        where at each invocation, we would only need to pop out a single element, once the sliding window reaches its
        upper bound.

    Space Complexity: O(1)

        As we estimated before, the maximal size of our sliding window is 3000, which is a constant.
    """

    def __init__(self):
        self.container = deque()

    def ping(self, t: int) -> int:
        self.container.append(t)

        while self.container[0] < t - 3000:
            self.container.popleft()

        return len(self.container)
