def positive_divide(numerator, denominator):
    try:
        result = numerator/denominator
    except TypeError:
        raise TypeError
    except ZeroDivisionError:
        return 0
    if result < 0:
        raise ValueError
    return result