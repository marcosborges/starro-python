import re
import math


def complete(arg):
    """Turns all characters to an string

    Args:
        arg (str): string to be converted

    Returns:
        str: converted string on string
    """
    return '*' * len(str(arg))


def password(arg):
    return complete(arg)


def token(arg):
    return complete(arg)


def accesskey(arg):
    return complete(arg)


def secret(arg):
    return complete(arg)


def ssn(arg):
    return fix_right(arg, 5)


def phone(arg):
    count = re.sub(r'\d', '*', arg).count('*') - 4
    return re.sub(r'\d', '*', arg, count=count)


def name(arg):
    return re.sub(r'\B([^\W])', '*', arg)


def cpf(arg):
    count = re.sub(r'\d', '*', arg).count('*') - 5
    return arg[:3] + re.sub(r'\d', '*', arg[3:], count=count)


# pylint: disable=C0103
def rg(arg):
    return arg[:3] + re.sub(r'\d', '*', arg[3:], count=6)


def pis(arg):
    return arg[:3] + re.sub(r'\d', '*', arg[3:], count=7)


def votercard(arg):
    return arg[:3] + re.sub(r'\d', '*', arg[3:], count=6)


# pylint: disable=C0103
def ie(arg):
    return arg[:3] + re.sub(r'\d', '*', arg[3:], count=6)


def cnh(arg):
    count = re.sub(r'\d', '*', arg).count('*') - 5
    return arg[:3] + re.sub(r'\d', '*', arg[3:], count=count)


def mail(arg):
    pattern = r'(?<=.)[^@](?=[^@]*?@)|(?:(?<=@.)|(?!^)\\G(?=[^@]*$)).(?=.*\\.)'
    return re.sub(pattern, "*", arg)


def gender(arg):
    return complete(arg)


def address(arg):
    return re.sub(r'\d', '*', arg)


def ethnicity(arg):
    return complete(arg)


def religion(arg):
    return complete(arg)


def health(arg):
    return complete(arg)


def politic(arg):
    return complete(arg)


def bank_number(arg):
    return arg[:2] + re.sub(r'\d', '*', arg[2:])


def account_number(arg):
    return arg[:2] + re.sub(r'\d', '*', arg[2:])


def platecar(arg):
    return re.sub(r'\d', '*', arg[:len(arg)-1]) + arg[len(arg)-1:]


def creditcard(arg):
    return arg[:4] + re.sub(r'\d', '*', arg[4:], count=8)


def sexual(arg):
    return complete(arg)


def crm(arg):
    return arg[:1] + re.sub(r'\d', '*', arg[1:], count=3)


def oab(arg):
    return arg[:2] + re.sub(r'\d', '*', arg[2:], count=4)


def mask_left(arg, size):
    return '*' * size + arg[size:]


def mask_right(arg, size):
    return arg[:(len(arg)-size)] + '*' * size


def mask_center(arg, size):
    total = len(arg)
    if total < size:
        return '*' * total
    result = math.ceil((total - size) / 2)
    return arg[:result] + ('*' * (len(arg) - size)) + arg[-result:]


def fix_left(arg, size):
    return arg[:size] + ('*' * (len(arg) - size))


def fix_right(arg, size):
    return ('*' * (len(arg) - size)) + arg[-size:]


def fix_center(arg, size):
    total = len(arg)
    if total < size:
        return '*' * total
    start = math.ceil((total - size) / 2)
    end = math.floor((total - size) / 2)

    return ('*' * start) + arg[start:-end] + ('*' * end)


# pylint: disable=W0123
def starrofy(filter_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # pylint: disable=global-statement
            return eval(filter_name + '("' + result + '")')
        return wrapper
    return decorator
