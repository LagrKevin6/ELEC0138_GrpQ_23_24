import string
from itertools import product
from numpy import loadtxt


def bruteforce(strategy = "common_pass", max_nchar=8):
    """
    Password brute-force algorithm.

    Parameters
    ----------
    strategy : string
        Password strategy
    max_nchar : int
        Maximum number of characters of password.

    Return
    ------
    bruteforce_password : string list
        Brute-forced password list
    """
    match strategy:
        case "common_pass":
            # Comparing with most common passwords / first names
            common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
            return common_pass
        case "common_name":
            common_names = loadtxt('middle-names.txt', dtype=str)
            return common_names
        case "digit":
            # Digits cartesian product
            for l in range(1, 9):
                generator = product(string.digits, repeat=int(l))
            return generator
        case "digitAndLowercase":
            # Digits + ASCII lowercase
            for l in range(1, max_nchar + 1):
                generator = product(string.digits + string.ascii_lowercase,
                                    repeat=int(l))
            return generator
        case "fullCase":
            # Digits + ASCII lower / upper + punctuation
            # If it fails, start brute-forcing the 'hard' way
            all_char = string.digits + string.ascii_letters + string.punctuation
            for l in range(1, max_nchar + 1):
                generator = product(all_char, repeat=int(l))
            return generator
