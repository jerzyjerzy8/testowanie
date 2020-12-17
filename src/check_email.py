import re


def check_email_format(email):
    """
    Function checking format of input email.
    :param email: email to check
    :return: info if email is proper
    """
    if not re.match(r"(^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception('Invalid email format')
    else:
        return 'Email format OK'
