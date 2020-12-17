DEFAULT_MAX_VALUE = 1000


def sum_args(max_value, args):
    s = 0
    if not is_int_or_float(max_value):
        max_value = DEFAULT_MAX_VALUE
    for num in args:
        if not is_int_or_float(num):
            continue
        if num > max_value:
            continue
        s += num
    return s


def is_int_or_float(obj):
    return isinstance(obj, int) or isinstance(obj, float)
