#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        x = fct(*args)
    except Exception as e:
        with open(2, "w") as stderr:
            stderr.write("Exception: {}\n".format(e))
            return None
    else:
        return x
