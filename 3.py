#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#




n=600851475143  # n kiyala apita oni anke danna.
def primeda(i):   #Api define karaganna oni function ekak numbers primeda kiyala balanna
    y=0
    for x in range(2,i):
        if i%x==0:
            y=y+1
    if y>=1:
        return False
    else:
        return True
    
for i in range(2,n):
    if n%i==0 and primeda(i)==True:
        print(i)


'''
# Easy Eulerlib Method
import eulerlib
def fact(n):
    for i in range(2,n):
        if n%i==0 and eulerlib.is_prime(i):
            print(i)
fact(600851475143)
'''
