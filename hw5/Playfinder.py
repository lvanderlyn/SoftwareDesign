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

<<<<<<< .merge_file_LOL2gX
=======
def act_scene_isolator(playtext):
    acts = ['I']
    for act in range(len(acts)):
        start_of_act = playtext.index("ACT " + acts[act] + ". SCENE 1.")
        newact = playtext[start_of_act:]
        if act >= len(acts) + 1 :
            end_of_act = newact.index("ACT " + acts[act+1] + ". SCENE 1.")
        else:
            end_of_act = newact.index("ACT " + acts[act+1] + ". SCENE 1.")
        newact = newact[:end_of_act]
        return newact

print act_scene_isolator(story_isolator(fullText))
>>>>>>> .merge_file_NBhSU5
