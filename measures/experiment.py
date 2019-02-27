#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.4),
    on Wed Feb 27 17:29:01 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('3.0.5')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.4'
expName = 'ec_RRR'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Ian/git/unconscious-ec-RRR/measures/experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1600, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "first_instructions"
first_instructionsClock = core.Clock()
text_instructions_2 = visual.TextStim(win=win, name='text_instructions_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
from numpy.random import randint
condition_randomisation = randint(1, 3, size = 1)
if condition_randomisation == 1:
    condition = "CS1_USpos"
elif condition_randomisation == 2:
    condition = "CS1_USneg"

#file_name = "trials/trials_participant_" + str(expInfo['participant']) + "_condition_" + condition + ".csv"
example = visual.ImageStim(
    win=win, name='example',
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.3, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_instructions_top = visual.TextStim(win=win, name='text_instructions_top',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_instructions_bottom = visual.TextStim(win=win, name='text_instructions_bottom',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
learning_phase_image = visual.ImageStim(
    win=win, name='learning_phase_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.78, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions_1.xlsx'),
    seed=None, name='instructions_loop')
thisExp.addLoop(instructions_loop)  # add the loop to the experiment
thisInstructions_loop = instructions_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
if thisInstructions_loop != None:
    for paramName in thisInstructions_loop:
        exec('{} = thisInstructions_loop[paramName]'.format(paramName))

for thisInstructions_loop in instructions_loop:
    currentLoop = instructions_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
    if thisInstructions_loop != None:
        for paramName in thisInstructions_loop:
            exec('{} = thisInstructions_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "first_instructions"-------
    t = 0
    first_instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_continue_2 = event.BuilderKeyResponse()
    text_instructions_2.setText(first_instructions_text)
    # keep track of which components have finished
    first_instructionsComponents = [key_resp_continue_2, text_instructions_2]
    for thisComponent in first_instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "first_instructions"-------
    while continueRoutine:
        # get current time
        t = first_instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_continue_2* updates
        if t >= 0.0 and key_resp_continue_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_continue_2.tStart = t
            key_resp_continue_2.frameNStart = frameN  # exact frame index
            key_resp_continue_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_continue_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_instructions_2* updates
        if t >= 0.0 and text_instructions_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_instructions_2.tStart = t
            text_instructions_2.frameNStart = frameN  # exact frame index
            text_instructions_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in first_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "first_instructions"-------
    for thisComponent in first_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "first_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructions_loop'


# set up handler to look after randomisation of conditions etc
blocks_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions_2.xlsx'),
    seed=None, name='blocks_loop')
thisExp.addLoop(blocks_loop)  # add the loop to the experiment
thisBlocks_loop = blocks_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
if thisBlocks_loop != None:
    for paramName in thisBlocks_loop:
        exec('{} = thisBlocks_loop[paramName]'.format(paramName))

for thisBlocks_loop in blocks_loop:
    currentLoop = blocks_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
    if thisBlocks_loop != None:
        for paramName in thisBlocks_loop:
            exec('{} = thisBlocks_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #file_name = "trials/" + block_id + ".csv" 
    #file_name = "trials/" + "condition_" + condition + "_" + block_id + ".csv"
    file_name = "trials/trials_participant_" + str(expInfo['participant']) + "_condition_" + condition + "_" + block_id + "_.csv"
    key_resp_continue = event.BuilderKeyResponse()
    example.setImage(example_image)
    text_instructions_top.setText(instructions_text_top)
    text_instructions_bottom.setText(instructions_text_bottom)
    # keep track of which components have finished
    instructionsComponents = [key_resp_continue, example, text_instructions_top, text_instructions_bottom]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *key_resp_continue* updates
        if t >= 0.0 and key_resp_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_continue.tStart = t
            key_resp_continue.frameNStart = frameN  # exact frame index
            key_resp_continue.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_continue.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *example* updates
        if t >= 0.0 and example.status == NOT_STARTED:
            # keep track of start time/frame for later
            example.tStart = t
            example.frameNStart = frameN  # exact frame index
            example.setAutoDraw(True)
        
        # *text_instructions_top* updates
        if t >= 0.0 and text_instructions_top.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_instructions_top.tStart = t
            text_instructions_top.frameNStart = frameN  # exact frame index
            text_instructions_top.setAutoDraw(True)
        
        # *text_instructions_bottom* updates
        if t >= 0.0 and text_instructions_bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_instructions_bottom.tStart = t
            text_instructions_bottom.frameNStart = frameN  # exact frame index
            text_instructions_bottom.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(file_name),
        seed=None, name='trials_loop')
    thisExp.addLoop(trials_loop)  # add the loop to the experiment
    thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop:
            exec('{} = thisTrials_loop[paramName]'.format(paramName))
    
    for thisTrials_loop in trials_loop:
        currentLoop = trials_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
        if thisTrials_loop != None:
            for paramName in thisTrials_loop:
                exec('{} = thisTrials_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        learning_phase_response = event.BuilderKeyResponse()
        learning_phase_image.setImage(stimulus)
        # keep track of which components have finished
        trialComponents = [learning_phase_response, learning_phase_image]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *learning_phase_response* updates
            if t >= 0.0 and learning_phase_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                learning_phase_response.tStart = t
                learning_phase_response.frameNStart = frameN  # exact frame index
                learning_phase_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(learning_phase_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if learning_phase_response.status == STARTED and t >= frameRemains:
                learning_phase_response.status = FINISHED
            if learning_phase_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['space', 'None'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if learning_phase_response.keys == []:  # then this was the first keypress
                        learning_phase_response.keys = theseKeys[0]  # just the first key pressed
                        learning_phase_response.rt = learning_phase_response.clock.getTime()
                        # was this 'correct'?
                        if (learning_phase_response.keys == str(correct_response)) or (learning_phase_response.keys == correct_response):
                            learning_phase_response.corr = 1
                        else:
                            learning_phase_response.corr = 0
            
            # *learning_phase_image* updates
            if t >= 0.0 and learning_phase_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                learning_phase_image.tStart = t
                learning_phase_image.frameNStart = frameN  # exact frame index
                learning_phase_image.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if learning_phase_image.status == STARTED and t >= frameRemains:
                learning_phase_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if learning_phase_response.keys in ['', [], None]:  # No response was made
            learning_phase_response.keys=None
            # was no response the correct answer?!
            if str(correct_response).lower() == 'none':
               learning_phase_response.corr = 1;  # correct non-response
            else:
               learning_phase_response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_loop (TrialHandler)
        trials_loop.addData('learning_phase_response.keys',learning_phase_response.keys)
        trials_loop.addData('learning_phase_response.corr', learning_phase_response.corr)
        if learning_phase_response.keys != None:  # we had a response
            trials_loop.addData('learning_phase_response.rt', learning_phase_response.rt)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_loop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'blocks_loop'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
