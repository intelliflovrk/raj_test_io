import random
import string

import utils
from utils import *

GMAIL_ADDRESS = "ifloqa@gmail.com"


def rand_suffix(value, k=6):
    return value + ''.join(random.choices(string.ascii_letters, k=k))


def rand_prefix(value, k=6):
    return ''.join(random.choices(string.ascii_letters, k=k)) + value


def rand_text(k=6):
    return ''.join(random.choices(string.ascii_letters, k=k))


def rand_range(start=0, stop=10, step=1):
    return random.randrange(start, stop, step)


def rand_intsuffix(value, n=9):
    return value + ''.join(random.choices(string.digits, k=n))


def rand_int(n=9):
    return ''.join(random.choices(string.digits, k=n))


def rand_intprefix(value, n=9):
    return ''.join(random.choices(string.digits, k=n)) + value


def rand_firstname(config, name_type):
    return rand_intsuffix(rand_suffix(utils.get_client_name(config, name_type), 3), 2)


def rand_lastname(config, name_type):
    return rand_intsuffix(rand_suffix(utils.get_client_name(config, name_type), 3), 2)


def rand_email(username=None):
    if not username:
        username = rand_text(7)
    email_parts = GMAIL_ADDRESS.split('@')
    return f"{email_parts[0]}+{username}@{email_parts[1]}"


def rand_addressline1():
    return f"{rand_int(3)} NotARealStreet{rand_text(4)}"


def rand_postcode():
    return f"{rand_text(2).upper()}{rand_int(2)} {rand_int(1)}{rand_text(2).upper()}"
