#!/usr/bin/python3

if __name__ == "__main__":
    
    """Print he sum, difference, product, division
    of two integer like 10 and 5."""
    
    from calculation_1 import add, sub, mul, div

    a = 10
    b = 5
    
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
