#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        output = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    else:
        return output
