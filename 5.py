'''                       ____Welcome____
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''

'''
def div(i):
    n=20
    y=0
    for x in range(1,n+1):
        if  i%x==0:
            y+=1
    if y==n:
        return True
    else:
        return False

    
i=1
while True:
    if div(i) is True:
        print(i)
        break
    i+=1
'''
# This will take too much time because the answer is 232792560 (huge amount)
# I will think about anouther method next time using least common factor
# You can try it your own self 

def div(i):
    n=20
    y=0
    for x in range(1,n+1):
        if  i%x==0:
            y+=1
    if y==n:
        return True
    else:
        return False

    
i=1
while True:
    if i%7==0 and i%13==0 and i%17==0 and  i%19==0 and i%11==0:
        if div(i) is True:
            print(i)
            break
    i+=1
