#                          ____Welcome____
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
                          #Programmed by : Kavindu Kalinga (UOM)
print("\t\t\t___Welcome___\n\t\t\t\tProgrammed by : Kavindu Kalinga (UOM)")
print('.....................................................................')
#______________________________________________________________________________#


a=[75]
b=[95,64]
c=[17,47,82]
d=[18,35,87,10]
e=[20,4,82,47,65]
f=[19,1,23,75,3,34]
g=[88,2,77,73,7,63,67]
h=[99,65,4,28,6,16,70,92]
i=[41,41,26,56,83,40,80,70,33]
j=[41,48,72,33,47,32,37,16,94,29]
k=[53,71,44,65,25,43,91,52,97,51,14]
l=[70,11,33,28,77,73,17,78,39,68,17,57]
m=[91,71,52,38,17,14,91,43,58,50,27,29,48]
n=[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
o=[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

lett=[o,n,m,l,k,j,i,h,g,f,e,d,c,b,a]

for j in range(14):
    for i in range(len(lett[j])-1):
        lett[j+1][i]=lett[j+1][i]+max(lett[j][i],lett[j][i+1])

print(a)
# Answer: 1074
