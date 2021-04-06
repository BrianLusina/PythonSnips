import dis
import sys


def sample(a, b):
    x = a + b
    y = x * 2
    print("Sample: ", y)
    return y


dis.dis(sample)
"""
Expected output
  5           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 BINARY_ADD
              7 STORE_FAST               2 (x)

  6          10 LOAD_FAST                2 (x)
             13 LOAD_CONST               1 (2)
             16 BINARY_MULTIPLY
             17 STORE_FAST               3 (y)

  7          20 LOAD_GLOBAL              0 (print)
             23 LOAD_CONST               2 ('Sample: ')
             26 LOAD_FAST                3 (y)
             29 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             32 POP_TOP

  8          33 LOAD_FAST                3 (y)
             36 RETURN_VALUE
"""


def trace_calls(frame, event, arg):
    if frame.f_code.co_name == "sample":
        print(frame.f_code)


sample(3, 2)
sys.settrace(trace_calls)
