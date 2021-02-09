'''                  ___Welcome___
                         | Programmed by : Kavindu Kalinga (UOM)
.......................................................................'''


# This is the function "eulerlib.is_prime( )" I've called in some files.

# If you don't have eulerlib library installed yet;
#       you can add this function to your code


def is_prime(n):
    for i in range(2,int(n**0.5)+1): # Factors are only between 2 and sqrt(n)
        if n%i==0:
            return False
            break
    else: return True


# Example: is_prime(12)     >>> FALSE
# Example: is_prime(13)     >>> TRUE


### Example code: Check numbers' primability below 100
##for i in range(2,100):
##    if is_prime(i): print(i,'  \tPrime')
##    else: print(i,'  \tNot Prime')
