#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#


#1 -  1                 
#2 -  3  5  7  9    
#3 - 13 17 21 25
#4 - 31 37 43 49
#5 - 57 65 73 81

d= (1001+1)/2 # 1001 by 1001 spiral formed

z=25
n=3
k=13
while True:
    t=2*(n-1)    # 4
    z=z+4*k+t*6
    if n>=d:
        break
    k=k+8*n-6  # 31
    n+=1

print(z)

# Answer: 669171001
