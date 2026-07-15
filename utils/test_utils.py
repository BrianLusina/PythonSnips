def custom_test_name_func(testcase_func, param_num, param):
    """
    A custom name function that displays the name of the function under test along with the arguments and parameters
    """
    len_args = len(param.args)
    expected = param.args[len(param.args) - 1]
    test_inputs = param.args[: len_args - 1]

    formatted_test_input = ""
    for idx, test_input in enumerate(test_inputs):
        formatted_test_input += f"(argument={idx}, value={test_input}) "

    return f"{testcase_func.__name__}, test_number={param_num} inputs={formatted_test_input}, expected={expected}"
