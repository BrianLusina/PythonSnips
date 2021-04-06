def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}() " f"with {args} {kwargs}")

        original_result = func(*args, **kwargs)

        print(f"TRACE: {func.__name__}() " f"returned {original_result!r}")

        return original_result

    return wrapper


@trace
def say(name, line):
    return f"{name}: {line}"


if __name__ == "__main__":
    say("Jane", "Hello, there")
    # expected output
    # TRACE: calling say() with ('Jane', 'Hello, there') {}
    # TRACE: say() returned 'Jane: Hello, there'
    # Jane: Hello, there
