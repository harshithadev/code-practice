
def hcf(x, y):
    """ function to return hcf given two numbers. """
    while(y):
       x, y = y, x % y
    return x
