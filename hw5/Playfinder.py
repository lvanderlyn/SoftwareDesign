# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:39:59 2014

@author: ddiggins
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

