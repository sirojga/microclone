def func1(a=2,b=3):
    return a+b

def func2(x):
    c=1
    d=2
    return x(c,d)

a=None


print(func2(a=func1))
