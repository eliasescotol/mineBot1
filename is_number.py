import math


def is_number(s):
    try:
        # Try converting the string to a float
        float_value = float(s)

        # Check if the float is finite (not infinity or NaN)
        if not math.isfinite(float_value):
            return False

        return True
    except ValueError:
        return False