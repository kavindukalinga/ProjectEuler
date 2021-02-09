#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#


def sp(n):    # sum of powers   |
    m=str(n)
    z=0
    for i in range(len(m)):
        z=z+(int(m[i]))**5
    return z

y=0
for i in range(1000,1000000):
    if sp(i)==i:
        y=y+i

print(y)




# Answer: 443839
