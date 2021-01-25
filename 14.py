#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

y=0
z=0

for i in range(1,1000000):
    k=i
    y=0
    while True:
        if i==1:
            break
        
        elif i%2==0:
             i=i/2
             y+=1
        else:
            i=3*i+1
            y+=1
    if y>=z:
        z=y
        m=k
print(z,' Answer is',m)

# This will take too much time because the answer is 837799 (huge amount)
# I will think about anouther method next time
