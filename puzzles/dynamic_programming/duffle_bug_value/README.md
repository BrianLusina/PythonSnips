You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane
profit margins. You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes—the
vault of the Queen of England. While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply
of each type.

Each type of cake has a weight and a value, stored in a tuple with two indices:

An integer representing the weight of the cake in kilograms An integer representing the monetary value of the cake in
British pounds For example:

```bash
# weighs 7 kilograms and has a value of 160 pounds
(7, 160)

# weighs 3 kilograms and has a value of 90 pounds
(3, 90)

```

You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the
maximum monetary value the duffel bag can hold.

For example:

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

max_duffel_bag_value(cake_tuples, capacity)

returns 555 (6 of the middle type of cake and 1 of the last type of cake)

Weights and values may be any non-negative integer. Yes, it's weird to think about cakes that weigh nothing or duffel
bags that can't hold anything. But we're not just super mastermind criminals—we're also meticulous about keeping our
algorithms flexible and comprehensive.

This is a classic computer science puzzle called "the unbounded knapsack problem."

We use a bottom-up ↴ approach to find the max value at our duffel bag's weight_capacity by finding the max value at
every capacity from 0 to weight_capacity.

We allocate a list max_values_at_capacities where the indices are capacities and each value is the max value at that
capacity.

For each capacity, we want to know the max monetary value we can carry. To figure that out, we go through each cake,
checking to see if we should take that cake.

Complexity O(n*k)O time, and O(k) space, where n is number of types of cake and k is the capacity of the
duffel bag. We loop through each cake (n cakes) for every capacity (k capacities), so our runtime is O(n∗k), and
maintaining the list of k+1 capacities gives us the O(k) space.

Congratulations! Because of dynamic programming, you have successfully stolen the Queen's cakes and made it big.

Keep in mind: in some cases, it might not be worth using our optimal dynamic programming solution. It's a pretty slow
algorithm—without any context (not knowing how many cake types we have, what our weight capacity is, or just how they
compare) it's easy to see O(n∗k) potentially being as bad as O(n^2) if n is close to k.

If we cared about time, like if there was an alarm in the vault and we had to move quickly, it might be worth using a
faster algorithm that gives us a good answer, even if it's not always the optimal answer. Some of our first ideas in the
breakdown were to look at cake values or value/weight ratios. Those algorithms would probably be faster, taking O(nlgn) time (we'd have to start by sorting the input).

Sometimes an efficient, good answer might be more practical than an inefficient, optimal answer.