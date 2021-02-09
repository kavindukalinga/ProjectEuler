#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

import eulerlib

y=4  # {2,3,5,7} below 10

for n in range(10,10**6):
    if eulerlib.is_prime(n):
        k=str(n)
        z=1
        for i in range(len(k)-1):
            m=k[i+1:]+k[0:i+1]
            if eulerlib.is_prime(int(m)):
                z=z+1
        if z==len(k):
            y=y+1

print(y)

# Answer: 55
