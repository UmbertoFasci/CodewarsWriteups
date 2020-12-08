#!/usr/bin/python3

"""
Codewars Kata Writeup

The goal of this exercise is to convert a stringto
a new string where each character in the new
string is "(" if that character appears only
once in the original string, or ")" if that
character appears more than once in the
original string. Ignore capitalization when
determining if a character is a duplicate

"din" -> "((("
"recede" -> "()()()"
"Success" -> ")())())" *** Notice that case is ignored***
"(( @" -> "))(("

"""

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(x) == 1 else ")" for x in word.lower()])


print(duplicate_encode("recede")) #result = ()()()
print(duplictae_encode("Success")) #result = )())())











