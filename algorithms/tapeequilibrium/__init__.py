import sys


def tape_equilibrium(tape: list) -> int:
    parts = [0] * len(tape)
    parts[0] = tape[0]

    for index in range(1, len(tape)):
        parts[index] = tape[index] + parts[index - 1]

    result = sys.maxsize

    for idx in range(0, len(parts) - 1):
        result = min(result, abs(parts[-1] - 2 * parts[idx]))

    return result
