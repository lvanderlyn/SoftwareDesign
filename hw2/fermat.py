# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:51:17 2014

@author: koenigin
"""

def check_fermat(a,b,c,n):
    """function which, if n > 2 checks to Fermat's last theorum"""
    if n > 2:
        if a**n + b**n == c**n:
            return "Holy smokes, Fermat was wrong!"
        else:
            return "No, that doesn't work."
    else:
        print('"n" needs to be greater than 2')
            
def use_fermat():
    """Allows a user to input value for a,b,c,n to check Fermat"""
    a = int(raw_input('please enter your number for "a": '))
    b = int(raw_input('please enter your number for "b": '))
    c = int(raw_input('please enter your number for "c": '))
    n = int(raw_input('please enter your number for "n": '))
    return check_fermat(a,b,c,n)
    
print use_fermat()
    
    