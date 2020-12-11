#!/usr/bin/python3

"""
Given: an array containing hashes of names

Return: a string formatted as a list of names
separated by commas except for the last two 
names, which should be separated by an ampersand.


EXAMPLE:

nameList([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])

returns 'Bart, Lisa & Maggie
"""


def namelist(names):
    strr = ''
    if len(names) != 0:
        array = []
        for name in range(0, len(names) - 1):
            array.append(names[name]['name'])
        strr = ', '.join(array)
        strr += ' & ' + names[-1]['name'] if strr != '' else names[-1]['name']
    return strr
