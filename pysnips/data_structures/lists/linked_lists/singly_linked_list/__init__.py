def contains_cycle(first_node):
    fast_runner = first_node
    slow_runner = first_node

    # until we reach the end of the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # fast runner is about to lap slow runner
        if fast_runner is slow_runner:
            return True

    # fast runner hit the end of the list
    return False
