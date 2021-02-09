#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

from math import factorial as fct

def sf(n): # sum of factorials  |
    m=str(n)
    z=0
    for i in range(len(m)):
        z=z+fct(int(m[i]))
    return z

y=0
for i in range(3,100000):
    if sf(i)==i:
        y=y+i

print(y)



# Answer: 40730     
