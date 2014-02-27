# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:58:46 2014

@author: koenigin
"""
import re

f = open('Shakespeare.txt')
fullText = f.read()
f.close

def story_isolator(play):
    end_of_boilerplate = play.index("all in black")
    end_of_play = play.index("Enter PAGE")
    playtext = play[end_of_boilerplate:end_of_play]
    return playtext

def assignLine(play, d):
    """Takes in a play and a dictionary of charactars in the play and assigns
    the lines to each character in the play"""
 
    index = 0
    while index < (len(play) -1):
        if play[index] in d:                    #finds first character
            speech = []
            character = play[index]            
            for place in range(index+1, len(play)):       #adds from start until stop (exlculsive)
                if play[place] not in d:
                    speech.append(play[place])
                    if place == len(play)-1:            #If no end codon, closes ORF and adds to all_ORFs
                        d[character] += speech
                        index = place 
                        break
                else:                               #closes ORF and adds codons to all_ORFs
                    d[character] += speech
                    index = place
                    break
        else:
            index += 1      #increases index to check next one for start codon
       
    return d

d = {'KING' : [], 'DUKE' : [], 'BERTRAM' : [], 'LAFEU' : [], 'PAROLLES' : [], 'FRENCH LORD' : [], 'STEWARD' : [], 'LAVACHE' : [], 'PAGE' : [], 'COUNTESS' : [], 'HELENA' : [],' WIDOW' : [], 'DIANA' : [], 'VIOLENTA' : [],  'MARIANA' : []}
play = re.findall("[\w'\-]+", story_isolator(fullText))
print assignLine(play,d) 
                 