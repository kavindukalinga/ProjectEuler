'''                  ___Welcome___
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''


y=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        y+=i
    else:
        pass
print(y)

'''
easy answer

ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
print(ans)

'''
	
