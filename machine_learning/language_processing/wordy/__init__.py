from operator import mul, add, sub
from sys import version_info

# version imports to make sure it works with Python 2.x.x
if version_info.major == 2:
    from operator import div
else:
    from operator import floordiv as div

# operators that will be used for evaluating which calculation to perform
OPERATIONS = {"plus": add, "minus": sub, "multiplied by": mul, "divided by": div}


def calculate(question):
    """
    Calculates a mathematical expression from a given question.
    :param question: The question to evaluate, usually starts with What is ...?
    :return: The result of the calculation
    :rtype: int
    :raises: ValueError
    """

    # check if it is in a valid question format
    if not question.startswith("What is ") and question.endswith("?"):
        raise ValueError("Invalid question")

    # obtain the actual question as a list
    que = question[8:-1].strip().lower().split()

    # check for validity
    if not que:
        raise ValueError("Invalid question")

    # reverse the list and obtain the last num
    que.reverse()
    try:
        num1 = int(que.pop())
    except ValueError:
        raise ValueError("Invalid question")

    while que:
        # obtain the operation
        operation = [que.pop()]
        while que:
            # try obtaining the next number,
            # if it is a word, such as by, then update the operation instead and break
            try:
                nxt = que.pop()
                num2 = int(nxt)
                break
            except ValueError:
                # update the operation to perform
                operation.append(nxt)
        else:
            raise ValueError("Invalid question")

        # the full operation to be used for the dict
        operation = " ".join(operation)

        # try performing the calculation
        try:
            num1 = OPERATIONS[operation](num1, num2)
        except KeyError:
            raise ValueError("Invalid question")
    return num1
