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
    end_of_boilerplate = play.index(">>")
    end_of_play = play.index("Exeunt omnes")
    playtext = play[end_of_boilerplate:end_of_play]
    return playtext

def act_scene_isolator(playtext):
    totalacts = []
    acts = ['I', 'II', 'III', 'IV', 'V']
    for act in range(len(acts)):
        start_of_act = playtext.index("ACT " + acts[act] + ". SCENE 1.")
        if acts[act] == 'V':
            newact = playtext[start_of_act:]
            totalacts.append(newact)
        else:
            newact = playtext[start_of_act:]
            end_of_act = newact.index("ACT " + acts[act+1] + ". SCENE 1.")
            newact = newact[:end_of_act]
            totalacts.append(newact)
    
    return totalacts

act_scene_isolator(story_isolator(fullText))