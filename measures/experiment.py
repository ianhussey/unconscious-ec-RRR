#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.4),
    on Thu Feb 21 21:00:34 2019
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
expName = 'unconscious_ec_RRR'  # from the Builder filename that created this script
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
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='[instructions]',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
learning_phase_image = visual.ImageStim(
    win=win, name='learning_phase_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='[instructions]',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
learning_phase_image = visual.ImageStim(
    win=win, name='learning_phase_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='[instructions]',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
learning_phase_image = visual.ImageStim(
    win=win, name='learning_phase_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='[instructions]',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
learning_phase_image = visual.ImageStim(
    win=win, name='learning_phase_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='[instructions]',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
learning_phase_image = visual.ImageStim(
    win=win, name='learning_phase_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_continue = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [key_resp_continue, text_instructions]
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
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    
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
block_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/trials.csv', selection=eval(range(((int(expInfo['participant'])-1)*430+1), ((int(expInfo['participant'])-1)*430+87), 1))),
    seed=None, name='block_1')
thisExp.addLoop(block_1)  # add the loop to the experiment
thisBlock_1 = block_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_1.rgb)
if thisBlock_1 != None:
    for paramName in thisBlock_1:
        exec('{} = thisBlock_1[paramName]'.format(paramName))

for thisBlock_1 in block_1:
    currentLoop = block_1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_1.rgb)
    if thisBlock_1 != None:
        for paramName in thisBlock_1:
            exec('{} = thisBlock_1[paramName]'.format(paramName))
    
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
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if learning_phase_response.keys == []:  # then this was the first keypress
                    learning_phase_response.keys = theseKeys[0]  # just the first key pressed
                    learning_phase_response.rt = learning_phase_response.clock.getTime()
        
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
    block_1.addData('learning_phase_response.keys',learning_phase_response.keys)
    if learning_phase_response.keys != None:  # we had a response
        block_1.addData('learning_phase_response.rt', learning_phase_response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_1'


# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_continue = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [key_resp_continue, text_instructions]
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
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    
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
block_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/trials.csv', selection=eval(range(((int(expInfo['participant'])-1)*430+87), ((int(expInfo['participant'])-1)*430+173), 1))),
    seed=None, name='block_2')
thisExp.addLoop(block_2)  # add the loop to the experiment
thisBlock_2 = block_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
if thisBlock_2 != None:
    for paramName in thisBlock_2:
        exec('{} = thisBlock_2[paramName]'.format(paramName))

for thisBlock_2 in block_2:
    currentLoop = block_2
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
    if thisBlock_2 != None:
        for paramName in thisBlock_2:
            exec('{} = thisBlock_2[paramName]'.format(paramName))
    
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
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if learning_phase_response.keys == []:  # then this was the first keypress
                    learning_phase_response.keys = theseKeys[0]  # just the first key pressed
                    learning_phase_response.rt = learning_phase_response.clock.getTime()
        
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
    block_2.addData('learning_phase_response.keys',learning_phase_response.keys)
    if learning_phase_response.keys != None:  # we had a response
        block_2.addData('learning_phase_response.rt', learning_phase_response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_2'


# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_continue = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [key_resp_continue, text_instructions]
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
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    
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
block_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/trials.csv', selection=eval(range(((int(expInfo['participant'])-1)*430+173), ((int(expInfo['participant'])-1)*430+259), 1))),
    seed=None, name='block_3')
thisExp.addLoop(block_3)  # add the loop to the experiment
thisBlock_3 = block_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_3.rgb)
if thisBlock_3 != None:
    for paramName in thisBlock_3:
        exec('{} = thisBlock_3[paramName]'.format(paramName))

for thisBlock_3 in block_3:
    currentLoop = block_3
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_3.rgb)
    if thisBlock_3 != None:
        for paramName in thisBlock_3:
            exec('{} = thisBlock_3[paramName]'.format(paramName))
    
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
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if learning_phase_response.keys == []:  # then this was the first keypress
                    learning_phase_response.keys = theseKeys[0]  # just the first key pressed
                    learning_phase_response.rt = learning_phase_response.clock.getTime()
        
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
    block_3.addData('learning_phase_response.keys',learning_phase_response.keys)
    if learning_phase_response.keys != None:  # we had a response
        block_3.addData('learning_phase_response.rt', learning_phase_response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_3'


# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_continue = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [key_resp_continue, text_instructions]
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
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    
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
block_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/trials.csv', selection=eval(range(((int(expInfo['participant'])-1)*430+259), ((int(expInfo['participant'])-1)*430+345), 1))),
    seed=None, name='block_4')
thisExp.addLoop(block_4)  # add the loop to the experiment
thisBlock_4 = block_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_4.rgb)
if thisBlock_4 != None:
    for paramName in thisBlock_4:
        exec('{} = thisBlock_4[paramName]'.format(paramName))

for thisBlock_4 in block_4:
    currentLoop = block_4
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_4.rgb)
    if thisBlock_4 != None:
        for paramName in thisBlock_4:
            exec('{} = thisBlock_4[paramName]'.format(paramName))
    
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
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if learning_phase_response.keys == []:  # then this was the first keypress
                    learning_phase_response.keys = theseKeys[0]  # just the first key pressed
                    learning_phase_response.rt = learning_phase_response.clock.getTime()
        
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
    block_4.addData('learning_phase_response.keys',learning_phase_response.keys)
    if learning_phase_response.keys != None:  # we had a response
        block_4.addData('learning_phase_response.rt', learning_phase_response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_4'


# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_continue = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [key_resp_continue, text_instructions]
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
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    
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
block_5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/trials.csv', selection=eval(range(((int(expInfo['participant'])-1)*430+345), ((int(expInfo['participant'])-1)*430+431), 1))),
    seed=None, name='block_5')
thisExp.addLoop(block_5)  # add the loop to the experiment
thisBlock_5 = block_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_5.rgb)
if thisBlock_5 != None:
    for paramName in thisBlock_5:
        exec('{} = thisBlock_5[paramName]'.format(paramName))

for thisBlock_5 in block_5:
    currentLoop = block_5
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_5.rgb)
    if thisBlock_5 != None:
        for paramName in thisBlock_5:
            exec('{} = thisBlock_5[paramName]'.format(paramName))
    
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
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if learning_phase_response.keys == []:  # then this was the first keypress
                    learning_phase_response.keys = theseKeys[0]  # just the first key pressed
                    learning_phase_response.rt = learning_phase_response.clock.getTime()
        
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
    block_5.addData('learning_phase_response.keys',learning_phase_response.keys)
    if learning_phase_response.keys != None:  # we had a response
        block_5.addData('learning_phase_response.rt', learning_phase_response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_5'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
