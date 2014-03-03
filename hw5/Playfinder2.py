# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:39:59 2014

@author: ddiggins, koenigin
"""

import re

f = open('Shakespeare.txt')
fullText = f.read()
f.close

def story_isolator(play, title):
    """Passes in the complete works of Shakespeare, and returns only the text of
    Alls Well that Ends Well
    
    Play input play must be in the format of the plaintex Project Gutenberg document
    
    Title input must be string and an actual play that Shakespeare wrote
    """
    titlefinder = play.index(title.upper()) #Traverses works to find play title in text
    play = play[titlefinder:]
    end_of_play = play.index("THE END") #Finds end of play
    playtext = play[:end_of_play] #Isolates the full play text
    return playtext

story = story_isolator(fullText, "Alls Well That Ends Well")

def personae_isolator(play):
    """Finds and returns the Dramatis Personae of a Shakespearian play
    
    Input must be a play that has been cut out from the main text through story_isolator
    """
    start_of_personae= play.index("Dramatis Personae") #Finds beginning of Personae
    end_of_personae = play.index("<<") #Project Gutenberg documents end Personae with long copyright notices
    personae = play[start_of_personae:end_of_personae] #Isolates the personae
    return personae


personae = personae_isolator(story)


def character_isolator(dramatispersonae):
    characters = {} #Creates empty dictionary for character names
    play = re.findall("[\w'\.\!\?\-]+", dramatispersonae)#Translates dramatis personae into list of words
    for word in play:
        if word == word.upper(): #Names appear in capital letters in Personae
            if word not in characters: #Adds character if they are not yet in the dictionary
                if word != 'THE':
                    if word != 'OF':
                        if word != 'A': #Getting rid of common extraneous words here
                            characters[word] = []
    
    return characters


print character_isolator(personae)

def act_isolator(playtext):
    """ Isolates Acts
    """
    totalacts = []
    acts = ['I', 'II', 'III', 'IV', 'V']
    scenes = range(8)
    for act in range(len(acts)):
        start_of_act = playtext.index("ACT " + acts[act])
        if acts[act] == acts[-1]:
            newact = playtext[start_of_act:]
            totalacts.append(newact)
        else:
            newact = playtext[start_of_act:]
            end_of_act = newact.index("<<THIS ELECTRONIC VERSION")
            newact = newact[:end_of_act]
            totalacts.append(newact)    
    
    print totalacts[1]
    return totalacts


#print act_isolator(story)


def scene_isolator(acts):
    """ Takes an input of acts output by act_isolator and cuts them into a list of scenes
    
    THIS FUNCTION ISN'T DONE DON'T RUN IT GOD DAMMIT
    """
    scenes = range(1,8)
    totalscenes = []
    for act in acts:#Takes a list of all of the acts in the play
        for scene in scenes:#Makes a list of the number of scenes
            scene_start = act.index("SCENE " + scenes[scene])#Searches and hopefully finds scene 1
            scene_end = act.index("Exeunt")#Continues to search until it finds the beginning of scene 2
    #Then starts again at scene 2
    #If it can't find the next scene in the play, it searches instead for 
    