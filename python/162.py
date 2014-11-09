x=z

def getValues(y,z):
    return (y-1)*(y)**(z-1) - (3*y-5)*(y-1)**(z-1) + (3*y-7)*(y-2)**(z-1) - (y-3)**(z)


def convToHex(x):
    s=""
    while(1):
        y=x%16
        x=x/16
        s=s+","+`int(y)`
        if(x<16):
                s=s+","+`int(x)`
                break
    
    return s[::-1]

A 10
B 
C 12
D 13
E 
F 15

