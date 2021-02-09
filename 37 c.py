#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

import eulerlib

ans=0

for n in range(10,10**6):   # you can increase the value, if you want ;-)
    if eulerlib.is_prime(n):
        k=str(n)
        z=0
        for i in range (len(k)):
            m=k[i:]
            if eulerlib.is_prime(int(m)): #12345,2345,345,45,5
                z=z+1
            h=k[:len(k)-i]
            if eulerlib.is_prime(int(h)): #12345,1234,123,12,1
                z=z+1
        if z==len(k)*2:
            ans=ans+n

print(ans)

# Answer: 748317
