'''                       ____Welcome____
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''

import eulerlib

n=2000000
x=0

for i in range(1,n+1):
    if eulerlib.is_prime(i) is True:
        x+=i
print(x)
        
    
# This will take too much time because the answer is 142913828922 (huge amount)
# I will think about anouther method next time
