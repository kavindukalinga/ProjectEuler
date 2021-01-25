'''                       ____Welcome____
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''

for x in range(1,500):
    for y in range(1,500):
        for z in range(1,500):# in a triangle, x+y>z, so maximum z is 500
            if x+y+z==1000 and x**2+y**2==z**2:
                print(x*y*z)
