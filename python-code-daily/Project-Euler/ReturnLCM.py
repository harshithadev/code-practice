def hcf(x,y):
    while(y):
        x,y = y, x%y
    return x

def lcm(x,y):
    return (x*y)/hcf(x,y)

#print(lcm(100,200))