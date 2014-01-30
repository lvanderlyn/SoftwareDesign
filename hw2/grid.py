# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:12:00 2014

@author: koenigin
"""


def grid_part():
    """Draws the top of a 2 x 2 grid"""
    line =   '+ - - - - + - - - - +'
    column = '|         |         |'
    print(line)
    print(column)
    print(column)
    print(column)
    print(column)
    
def small_grid():
    """puts the peices of a 2x2 grid together"""
    line =   '+ - - - - + - - - - +'    
    grid_part()
    grid_part()
    print(line)
    
def big_grid_part():
    """Draws the top of a 4x4 grid"""
    big_line =   '+ - - - - + - - - - + - - - - + - - - - +'
    big_column = '|         |         |         |         |'
    print(big_line)
    print(big_column)
    print(big_column)
    print(big_column)
    print(big_column)
    
def large_grid():
    """puts the pieces of a 4x4 grid together"""
    big_line =   '+ - - - - + - - - - + - - - - + - - - - +'
    big_grid_part()
    big_grid_part()
    big_grid_part()
    big_grid_part()
    print(big_line)
    
large_grid()
