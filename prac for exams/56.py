
def processstring(x):
    if not isinstance(x,str):
        raise TypeError("x must be a string")
    else:
        print("processing string",x)
        
try:
    processstring("this")
    processstring(123)
except TypeError as e:
    print(e)