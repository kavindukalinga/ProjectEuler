'''                       ____Welcome____
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''


import eulerlib
i=2
y=0
while True:
    if eulerlib.is_prime(i) is True:
        y=y+1
    if y==10001:
        print(i)
        break
    i+=1
    

# You can add Eulerlib module usin pip to your pc\it's not an inbuilt module
