# Write a recursive function for generating all permutations of an input string. Return them as a set.

Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

To start, assume every character in the input string is unique.

Your function can have loops—it just needs to also be recursive.

Breakdown Let's break the problem into subproblems. How could we re-phrase the problem of getting all permutations for "
cats" in terms of a smaller but similar subproblem?

Let's make our subproblem be getting all permutations for all characters except the last one. If we had all permutations
for "cat," how could we use that to generate all permutations for "cats"?

We could put the "s" in each possible position for each possible permutation of "cat"!

These are our permutations of "cat":

cat cta atc act tac tca For each of them, we add "s" in each possible position. So for "cat":

cat scat csat cast cats And for "cta":

cta scta csta ctsa ctas And so on.

Now that we can break the problem into subproblems, we just need a base case and we have a recursive algorithm!

