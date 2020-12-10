#! /usr/bin/python3

"""
Jamie is a programmer, and James' girlfriend.
She likes diamonds, and wants a diamond
string from James. Since James doesn't know
how to make this happen, he needs your help.

You need to return a string that looks like a
diamond shape when printed on the screen,
using asterisk(*) characters. Trailing spaces
should be removed, and every line must be
terminated with a newline character( \n).

Return null/nil/None/... if the input is an
even number or negative, as it is not possible
to print a diamond of even or negative size.

n = 3

 *
***
 *


n = 5

  *
 ***
*****
 ***
  *

"""

"""
THOUGHTS:

n corresponds to the number of rows associated with
the diamond shape. n also corresponds to the number
of asterisks of the center row. The spaces required 
at the beginning and end of the shape has the property
(n-1)/2.
"""

def diamond(n):
    if n <1 or not n % 2:                                                 # this satifies the requirement for shapes of odd size.
        return null
    r = ''
    for i in range(n):                                                    # loop necessary to build the asterisks for the line.
        asterisk = '*'*(i * 2 + 1) if i <= n/2 else '*'*((n-i) * 2 - 1)
        r += ' ' * int((n - len(asterisk)) / 2) + asterisk + '\n'         # necessary for adding the next row of the shape.
    return r


print(diamond(5))
