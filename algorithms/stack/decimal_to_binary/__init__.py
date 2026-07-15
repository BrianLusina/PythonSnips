from datastructures.stacks.dynamic import DynamicSizeStack as Stack


def convert_int_to_bin(dec_num: int) -> int:
    """
    Converts a decimal integer to binary using a stack data structure. Uses the division by 2 method to perform the
    conversion. Each remainder from the division is stored on the stack and popped off until we have the binary
    number
    Args:
        dec_num (int): Decimal Number
    Return:
        int: binary representation
    """

    stack = Stack()
    current = dec_num

    while current != 0:
        current, rem = divmod(current, 2)
        stack.push(rem)

    bin_num = ""
    while not stack.is_empty():
        binary = stack.pop()
        bin_num += str(binary)

    return int(bin_num)
