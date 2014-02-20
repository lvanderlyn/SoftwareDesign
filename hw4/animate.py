# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:20:12 2014

@author: koenigin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import math

import Image

def build_random_function(min_depth, max_depth):
    """Function takes in an input of the minimum and maximum depth of 
    recursion and generates a random function based on that"""
    
    choices = [['prod'], ['sin_pi'], ['cos_pi'], ['X'], ['Y'], ['T']] #list of functions to randomly choose #Now includes 'T'
    
    #Creates a base case    
    if max_depth == 1:                 
        return ['X']#, ['Y']]         #when the maximum depth is reached, return the base case 
    
    #If min depth reached, can also choose base case
    elif min_depth <= 1:  
              
        function_choice = choices[randint(0,5)]   #chooses random list index to build function from 
        #allows products to take two inputs         
        if function_choice == ['prod']:            
           return function_choice + [build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth, max_depth)]
        #If base case reached, ends recursion
        elif function_choice == ['X'] or function_choice == ['Y'] or function_choice == ['T']:
            return function_choice
        #otherwise function recurses normally (only one input)        
        else:
           return function_choice + [build_random_function(min_depth-1, max_depth-1)]
    
    #If min/max depth not reached goes through again subtracting one from min/max counters
    else:                            
        function_choice = choices[randint(0, 2)]
        #allows products to take two inputs
        if function_choice != ['prod']:
            return function_choice + [(build_random_function(min_depth-1, max_depth-1))]
        #Otherwise recurses normally
        else:
            return function_choice + [build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]

#if __name__ == "__main__":
    #print build_random_function(3, 5)
    
    
def evaluate_random_function(f, x, y, t):
    """This function takes in a list of strings standing for functions and
    recursively evaluates it in terms of inputted values for x, y, and t"""
    #changed to include T 
    if f[0] == 'prod':
        return evaluate_random_function(f[1], x, y, t) * evaluate_random_function(f[2], x,y,t)
    elif f[0] == 'cos_pi':
        return math.cos(math.pi * evaluate_random_function(f[1], x, y, t))
    elif f[0] == 'sin_pi':
        return math.sin(math.pi * evaluate_random_function(f[1],x, y, t))
    elif f[0] == 'X':
        return x
    elif f[0] == 'T':
        return t
    else:
        return y   

#if __name__ == '__main__':
#    print evaluate_random_function(build_random_function(3,5), math.pi*6, math.pi*8)              

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
    """
    
    zero = (output_interval_start - input_interval_start)
    change_factor = float(output_interval_end)/ (input_interval_end + zero)
    new_value = (val+zero)*change_factor
    return new_value
    
    
if __name__ == '__main__':
    #function = build_random_function(3,5)
   # value = evaluate_random_function(function, math.pi*6, math.pi*8)
  #  print value
    #print remap_interval(350,0, 350, -1, 1)   
    
    
    img = Image.new('RGB', (350, 350))
    pixels = img.load() # create the pixel map
    functionR = build_random_function(6,15)
    print functionR
    functionG = build_random_function(9,11)
    print functionG
    functionB = build_random_function(5,12)
    print functionB 

    for t in range(1, 100):        
        for i in range(img.size[0]):    # for every pixel:
            for j in range(img.size[1]):
                time = remap_interval(t, 1, 40,  -1, 1)
                posX = remap_interval(i, 0, 350, -1, 1)
                posY = remap_interval(j, 0, 350, -1, 1)
                rawR = evaluate_random_function(functionR, posX, posY, time)
                rawG = evaluate_random_function(functionG, posX, posY, time)
                rawB = evaluate_random_function(functionB, posX, posY, time)
                filterR = int(remap_interval(rawR, -1, 1, 0, 255))
                filterG = int(remap_interval(rawG, -1, 1, 0, 255))
                filterB = int(remap_interval(rawB, -1, 1, 0, 255))
                pixels[i,j] = (filterR, filterG, filterB ) # set the colour accordingly
                
        img.save("frameAttemptThree" + str(t) +".jpg", "JPEG") #saves all frames to be easily accessed
