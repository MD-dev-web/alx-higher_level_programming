#!/usr/bin/python3

import sys


def safe_function(fctn, *args):
    """
    Safe function
    """
    try:
        result = fctn(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
