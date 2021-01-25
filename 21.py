#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#


def d(n):
    z=0
    for i in range(1,(int((n+1)/2))+1):
        if n%i==0:
            z=z+i
    return(z)

y=0
for x in range(1,10001):
    if x==d(d(x)) and x!=d(x): # if x is an amicable number?
        y=y+x


print(y)




# Answer: 31626
