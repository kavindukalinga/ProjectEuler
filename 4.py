'''                       ____Welcome____
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''

def pal(n):
    x=str(n)
    y=x[::-1]
    if x==y:
        return True
    else:
        return False

y=0
for i in range(100,1000):
    for x in range(100,1000):
        if pal(i*x) is True:
            if i*x>=y:
                y=i*x
                
print(y)
