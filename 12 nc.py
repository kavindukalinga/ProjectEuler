'''                       ____Welcome____
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''
'''

# Let's define triangle number as tr() \ n is the #th number
def tr(n):
    return(int(n*(n+1)/2)) # we need the int, but this division(/2) gives float

i=1
while True:
    x=tr(i)
    z=0
    for y in range(1,x+1):
        if x%y==0:
            z+=1
            print(x)
    if z>500:
         print('answer',x)
         break
    i+=1
    
    
    

# This will take tooooo much time because the answer is 76576500 (huge amount)
# I will think about anouther method next time
'''
# Proof
n=76576500
z=0
for i in range(1,n+1):
    if n%i==0:
        z+=1
print('Divisors',z)
'''
w2=0
for n in range(10000,15000):
    k=int(n*(n+1)/2)
    w1=0
    for i in range(1,k+1):
        if k%i==0:
            #print(k,i)
            w1+=1
    if w1>w2:
        w2=w1
        print(w1,'Divisors for ',i)
'''
