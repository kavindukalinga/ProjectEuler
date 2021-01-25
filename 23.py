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
            z+=i
    return(z)

ab=[]

for x in range(12,28123):
    if d(x)>x:
        ab.append(x)
''' # Another method for above part       |
from math import sqrt
def divisors(n):
    divs=[1]
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            divs.extend([i,n/i])
    return list(set(divs))

ab=[]
for i in range(12,28123):
    if sum(divisors(i))>i:
        ab.append(i)
'''

non_ab_sum=[x for x in range(28123)]

for i in range(len(ab)):
    for j in range(len(ab)):
        if ab[i]+ab[j]<28123:
            non_ab_sum[ab[i]+ab[j]]=0
        else:
            break

print(sum(non_ab_sum))
'''
al=[x for x in range(28123)]
non=[]
for i in ab:
    for j in ab:
        if i+j<28123:
            non.append(i+j)
        else:
            break

non=list(set(non))
print(sum(al)-sum(non))
'''
# Answer: 4179871
