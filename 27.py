#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

import eulerlib
import math

def test():
    z=0
    y=0
    for n in range (0,int(math.fabs(a)+1)):
        t=n**2+a*n+b
        if eulerlib.is_prime(t):
            z=z+1
        else:
            break
    if z>=y and z>50:
        print(z,'Answer is',a*b)
        y=z
    

for a in range (-1000,1000):
   for b in range (-1001,1001):
        test()


# Answer: -59231
