### About Eulerlib
'''https://pypi.org/project/eulerlib/#:~:text=eulerlib%20is%20a%20library%20of,Divisor%20functions%20(sigma%20functions)'''

## Project description

'''Eulerlib is a library of recreational mathematics and number theory
related functions inspired by Project Euler. Available functions include:

 1. Prime number generation
 2. Divisor functions (sigma functions)
 3. Euler’s totient function
 4. Greatest Common Divisor (GCD) using Euclid’s algorithm
 5. Least Common Multiple (LCM)
 6. Integer square root
 7. Fibonacci numbers
 8. Pandigital numbers
 9. Palindrome numbers
10. Pythagorean triples

Functions from this library can be used to solve recreational mathematics
and programming problems such as problems in Project Euler.'''

## Installation

'''eulerlib is avalaible through Python Package Index (PyPI) using pip.'''
#    >>> pip install --upgrade eulerlib

## Import
import eulerlib

## Modules
print(dir(eulerlib))
'''>>>['Divisors', '__all__', '__builtins__', '__cached__', '__doc__',
'__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__',
'_exceptions', 'collapse_lists', 'decimal_to_base', 'digital_root',
'digital_sum', 'etc', 'fibo_gen', 'fibo_less_than', 'fibo_num_digits',
'fibonacci', 'first_n_fibo', 'gcd', 'is_palindrome', 'is_pandigital',
'is_prime', 'is_square', 'lcm', 'lcm_n', 'list_to_num', 'nCr', 'nPr',
'num_to_list', 'numtheory', 'prime_gen', 'prime_numbers', 'prime_wheel_fact_gen',
'primes', 'primes_wheel_fact', 'primitive_triples', 'pythagoras', 'triplet_gen',
'word_numerical_val', 'write_number']'''


#prime_numbers.py
'''Functions to generate lists of primes.'''

#numtheory.py	
'''Euler’s divisor functions (sigma funtions)
Euler’s totient function (phi function)
Prime factors of a number
Divisors of a number
Greatest Common Divisor (GCD)
Least Common Multiple (LCM)
Digital root and digital sum of a number'''

#fibonacci.py
'''Functions related to the Fibonacci sequence.'''

#pythagoras.py
'''Functions related to Pythagorean triples.'''

#etc.py	    Miscellaneous functions:
'''Pandigital numbers
Conversion from decimal to base n (2-36)
Number to lists and vice versa
Palindrome numbers'''

## Development
'''Source code repositories (GitHub, BitBucket) are available.
Bug reports and suggestions are most welcome.'''

## License
'''eulerlib is licensed under Apache License 2.0.'''
