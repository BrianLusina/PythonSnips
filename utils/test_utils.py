from parameterized import parameterized


def custom_test_name_func(testcase_func, param_num, param):
    """
    A custom name function that displays the name of the function under test along with the arguments and parameters
    """
    return f"{testcase_func.__name__}, {parameterized.to_safe_name("_".join(str(x) for x in param.args))}"
