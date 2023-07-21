from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    # used to store the final asteroid list, this results in a space complexity of O(N), where it is possible that no
    # collisions ever happen
    stack = []

    # time complexity incurred here is O(N) as we iterate over all the asteroids
    for asteroid in asteroids:

        # we only add an asteroid if it's positive(moving in the right direction) or stack is empty
        if not stack or asteroid > 0:
            stack.append(asteroid)
        else:
            # we pop the top most asteroid seen so far only if it is less than the size of the current asteroid, meaning
            # collision and also if it is greater than 0, meaning moving in the opposite direction as the current
            # asteroid
            while stack and 0 < stack[-1] < abs(asteroid):
                stack.pop()

            # if we have an element in the stack, check that the top element is equal in size fo the current asteroid
            # pop it, this implies collision
            if stack and stack[-1] == abs(asteroid):
                stack.pop()
            else:
                # else, we can add this asteroid to the stack and continue checking for other collisions
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)

    return stack
