#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

def pal(n):     # Define palindromic    |
    m=str(n)
    if m==m[::-1] and m[-1]!=0:
        return True
    else:
        return False

def pb(n):      # Palindromic Both
    p=str(bin(n))
    q=int(p[2:])
    if pal(n)is True and pal(q) is True:
        return True
    else:
        return False

z=0

for i in range(1,10**6):
    if pb(i) is True:
        z=z+i

print(z)




# Answer: 872187
