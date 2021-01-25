#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#

count=725760
Set={'p'}  #cant open a blank set, they think it's a Dictionary 
Set.clear()
for x in range (2013456789,9876543210,9):
    string=str(x)
    for c in string:
        Set.add(c)
        if len(Set)==10: count+=1
    if count==10**6:
        break
    Set.clear()
print(x)

# Answer: 2783915460


##from itertools import permutations
##
####l=list(permutations(range(0,10)))
####
####t=[]
####
####for i in range(len(l)):
####    s=str()
####    for j in range(10):
####        s=s+str(l[i][j])
####    t.append(int(s))
####
####t.sort()
####
####print(t[10**6-1])
##
##l=list(permutations(range(0,10)))
##l.sort()
##s=('')
##for i in l[10**6-1]:
##    s=s+str(i)
##print(s)


# Answer: 2783915460
