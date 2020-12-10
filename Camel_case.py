#!/usr/bin/python3

"""
Complete the method/function so that it converts dash/underscore
delimited words into camel casing. The first word within the 
output should be capitalized only if the original word was capatalized 
(known as Upper Camel Case, also often referred to as Pascal case).
"""


import re

def to_camel_case(text):
    strr = re.split('[-_]', text)
    new_strr = strr[0] + ''.join(i.title() for i in strr[1:])
    return new_strr


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-stealth-warrior"))
