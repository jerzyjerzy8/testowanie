def capital_case(s):
    if isinstance(s, str):
        return s.capitalize()
    else:
        raise TypeError('Argument must be str type')
