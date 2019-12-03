#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.4),
    on November 07, 2019, at 16:46
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
expInfo = {'age': '', 'gender': '', 'participant': '', 'UseMonkey': 'n'}
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
    originPath='C:\\Users\\tmoranyo\\Documents\\GitHub\\RRR_fazio-olson2001-local\\tal-creation\\4 site-specific measures for data collection\\Hütter\\experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.ERROR)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1600, 900], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
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
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "surveillance_instructions_2"
surveillance_instructions_2Clock = core.Clock()
# dependencies
from numpy.random import randint
from psychopy.hardware.emulator import ResponseEmulator

# randomly assign to condition
condition_randomisation = randint(1, 3, size = 1)
if condition_randomisation == 1:
    condition = "CS1_USpos"
elif condition_randomisation == 2:
    condition = "CS1_USneg"

# write this value to disk
thisExp.addData('condition', condition)

# auto response monkey 
if str(expInfo['UseMonkey']) == 'y':
    monkey = True
    surveillance_duration = 0.1
else: 
    monkey = False
    surveillance_duration = 1.5


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

# Initialize components for Routine "surveillance_trial"
surveillance_trialClock = core.Clock()

surveillance_image = visual.ImageStim(
    win=win, name='surveillance_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.3, 0.73),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "filler_1"
filler_1Clock = core.Clock()

filler_1_rating = visual.RatingScale(win=win, name='filler_1_rating', lineColor='Black', textColor='Black', low=1, high=7, scale="")
filler_1_text = visual.TextStim(win=win, name='filler_1_text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "filler_2"
filler_2Clock = core.Clock()

filler_2_rating = visual.RatingScale(win=win, name='filler_2_rating', lineColor='Black', textColor='Black', low=1, high=5, scale="")
filler_2_text = visual.TextStim(win=win, name='filler_2_text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "evaluation_trial"
evaluation_trialClock = core.Clock()
# get evaluation file
evaluation_file_name = "trials/evaluation_trials_participant_" + str(expInfo['participant']) + ".csv"


evaluation_image = visual.ImageStim(
    win=win, name='evaluation_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.6, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_evaluations_instruction_middle = visual.TextStim(win=win, name='text_evaluations_instruction_middle',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_evaluations_instruction_left_top = visual.TextStim(win=win, name='text_evaluations_instruction_left_top',
    text='default text',
    font='Arial',
    pos=(-0.3, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_evaluations_instruction_right_top = visual.TextStim(win=win, name='text_evaluations_instruction_right_top',
    text='default text',
    font='Arial',
    pos=(0.3, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_evaluations_instruction_left_bottom = visual.TextStim(win=win, name='text_evaluations_instruction_left_bottom',
    text='e',
    font='Arial',
    pos=(-0.3, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_evaluations_instruction_right_bottom = visual.TextStim(win=win, name='text_evaluations_instruction_right_bottom',
    text='i',
    font='Arial',
    pos=(0.3, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "awareness_type_1_trial"
awareness_type_1_trialClock = core.Clock()
inputText = ""
box = visual.Rect(
    win=win, name='box',
    width=(1.1, 0.4)[0], height=(1.1, 0.4)[1],
    ori=0, pos=[0, -0.15],
    lineWidth=2, lineColor='black', lineColorSpace='rgb',
    fillColor='lightgrey', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
awareness_type_1_question = visual.TextStim(win=win, name='awareness_type_1_question',
    text='default text',
    font='Arial',
    pos=(0, 0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
awareness_type_1_show_response = visual.TextStim(win=win, name='awareness_type_1_show_response',
    text='default text',
    font='Arial',
    pos=[-0.5, -0.15], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "awareness_type_2a_trial"
awareness_type_2a_trialClock = core.Clock()

awareness_type_2a_rating = visual.RatingScale(win=win, name='awareness_type_2a_rating', lineColor='Black', textColor='Black', low=1, high=2, scale="")
awareness_type_2a_text = visual.TextStim(win=win, name='awareness_type_2a_text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "awareness_type_2b_trial"
awareness_type_2b_trialClock = core.Clock()

awareness_type_2b_rating = visual.RatingScale(win=win, name='awareness_type_2b_rating', lineColor='Black', textColor='Black', low=1, high=6, scale="")
awareness_type_2b_text = visual.TextStim(win=win, name='awareness_type_2b_text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "awareness_type_2c_trial"
awareness_type_2c_trialClock = core.Clock()

awareness_type_2c_rating = visual.RatingScale(win=win, name='awareness_type_2c_rating', lineColor='Black', textColor='Black', low=1, high=9, scale="")
awareness_type_2c_text = visual.TextStim(win=win, name='awareness_type_2c_text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
record_data_collection_site_variable = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('text/data_collection_site.xlsx'),
    seed=None, name='record_data_collection_site_variable')
thisExp.addLoop(record_data_collection_site_variable)  # add the loop to the experiment
thisRecord_data_collection_site_variable = record_data_collection_site_variable.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRecord_data_collection_site_variable.rgb)
if thisRecord_data_collection_site_variable != None:
    for paramName in thisRecord_data_collection_site_variable:
        exec('{} = thisRecord_data_collection_site_variable[paramName]'.format(paramName))

mouse = event.Mouse(visible=False)

for thisRecord_data_collection_site_variable in record_data_collection_site_variable:
    currentLoop = record_data_collection_site_variable
    # abbreviate parameter names if possible (e.g. rgb = thisRecord_data_collection_site_variable.rgb)
    if thisRecord_data_collection_site_variable != None:
        for paramName in thisRecord_data_collection_site_variable:
            exec('{} = thisRecord_data_collection_site_variable[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    surveillance_instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions.xlsx', selection='0:4'),
        seed=None, name='surveillance_instructions_loop')
    thisExp.addLoop(surveillance_instructions_loop)  # add the loop to the experiment
    thisSurveillance_instructions_loop = surveillance_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSurveillance_instructions_loop.rgb)
    if thisSurveillance_instructions_loop != None:
        for paramName in thisSurveillance_instructions_loop:
            exec('{} = thisSurveillance_instructions_loop[paramName]'.format(paramName))
    
    for thisSurveillance_instructions_loop in surveillance_instructions_loop:
        currentLoop = surveillance_instructions_loop
        # abbreviate parameter names if possible (e.g. rgb = thisSurveillance_instructions_loop.rgb)
        if thisSurveillance_instructions_loop != None:
            for paramName in thisSurveillance_instructions_loop:
                exec('{} = thisSurveillance_instructions_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(2, 'space')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        instructions_response = event.BuilderKeyResponse()
        text_instructions.setText(instructions_text)
        # keep track of which components have finished
        instructionsComponents = [instructions_response, text_instructions]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *instructions_response* updates
            if t >= 0.0 and instructions_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructions_response.tStart = t
                instructions_response.frameNStart = frameN  # exact frame index
                instructions_response.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if instructions_response.status == STARTED:
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
    # completed 1 repeats of 'surveillance_instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    surveillance_blocks_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions_surveillance.xlsx'),
        seed=None, name='surveillance_blocks_loop')
    thisExp.addLoop(surveillance_blocks_loop)  # add the loop to the experiment
    thisSurveillance_blocks_loop = surveillance_blocks_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSurveillance_blocks_loop.rgb)
    if thisSurveillance_blocks_loop != None:
        for paramName in thisSurveillance_blocks_loop:
            exec('{} = thisSurveillance_blocks_loop[paramName]'.format(paramName))
    
    for thisSurveillance_blocks_loop in surveillance_blocks_loop:
        currentLoop = surveillance_blocks_loop
        # abbreviate parameter names if possible (e.g. rgb = thisSurveillance_blocks_loop.rgb)
        if thisSurveillance_blocks_loop != None:
            for paramName in thisSurveillance_blocks_loop:
                exec('{} = thisSurveillance_blocks_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "surveillance_instructions_2"-------
        t = 0
        surveillance_instructions_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        surveillance_file_name = "trials/surveillance_trials_participant_" + str(expInfo['participant']) + "_condition_" + condition + "_" + block_id + "_.csv"
        
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(1, 'space')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        key_resp_continue = event.BuilderKeyResponse()
        example.setImage(example_image)
        text_instructions_top.setText(instructions_text_top)
        text_instructions_bottom.setText(instructions_text_bottom)
        # keep track of which components have finished
        surveillance_instructions_2Components = [key_resp_continue, example, text_instructions_top, text_instructions_bottom]
        for thisComponent in surveillance_instructions_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "surveillance_instructions_2"-------
        while continueRoutine:
            # get current time
            t = surveillance_instructions_2Clock.getTime()
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
            for thisComponent in surveillance_instructions_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "surveillance_instructions_2"-------
        for thisComponent in surveillance_instructions_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "surveillance_instructions_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        surveillance_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(surveillance_file_name),
            seed=None, name='surveillance_trials_loop')
        thisExp.addLoop(surveillance_trials_loop)  # add the loop to the experiment
        thisSurveillance_trials_loop = surveillance_trials_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSurveillance_trials_loop.rgb)
        if thisSurveillance_trials_loop != None:
            for paramName in thisSurveillance_trials_loop:
                exec('{} = thisSurveillance_trials_loop[paramName]'.format(paramName))
        
        for thisSurveillance_trials_loop in surveillance_trials_loop:
            currentLoop = surveillance_trials_loop
            # abbreviate parameter names if possible (e.g. rgb = thisSurveillance_trials_loop.rgb)
            if thisSurveillance_trials_loop != None:
                for paramName in thisSurveillance_trials_loop:
                    exec('{} = thisSurveillance_trials_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "surveillance_trial"-------
            t = 0
            surveillance_trialClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # write this value to disk
            thisExp.addData('condition', condition)
            surveillance_response = event.BuilderKeyResponse()
            surveillance_image.setImage(stimulus)
            # keep track of which components have finished
            surveillance_trialComponents = [surveillance_response, surveillance_image]
            for thisComponent in surveillance_trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "surveillance_trial"-------
            while continueRoutine:
                # get current time
                t = surveillance_trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *surveillance_response* updates
                if t >= 0.0 and surveillance_response.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    surveillance_response.tStart = t
                    surveillance_response.frameNStart = frameN  # exact frame index
                    surveillance_response.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(surveillance_response.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + surveillance_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
                if surveillance_response.status == STARTED and t >= frameRemains:
                    surveillance_response.status = FINISHED
                if surveillance_response.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space', 'None'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if surveillance_response.keys == []:  # then this was the first keypress
                            surveillance_response.keys = theseKeys[0]  # just the first key pressed
                            surveillance_response.rt = surveillance_response.clock.getTime()
                            # was this 'correct'?
                            if (surveillance_response.keys == str(surveillance_correct_response)) or (surveillance_response.keys == surveillance_correct_response):
                                surveillance_response.corr = 1
                            else:
                                surveillance_response.corr = 0
                
                # *surveillance_image* updates
                if t >= 0 and surveillance_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    surveillance_image.tStart = t
                    surveillance_image.frameNStart = frameN  # exact frame index
                    surveillance_image.setAutoDraw(True)
                frameRemains = 0 + surveillance_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
                if surveillance_image.status == STARTED and t >= frameRemains:
                    surveillance_image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in surveillance_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "surveillance_trial"-------
            for thisComponent in surveillance_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if surveillance_response.keys in ['', [], None]:  # No response was made
                surveillance_response.keys=None
                # was no response the correct answer?!
                if str(surveillance_correct_response).lower() == 'none':
                   surveillance_response.corr = 1;  # correct non-response
                else:
                   surveillance_response.corr = 0;  # failed to respond (incorrectly)
            # store data for surveillance_trials_loop (TrialHandler)
            surveillance_trials_loop.addData('surveillance_response.keys',surveillance_response.keys)
            surveillance_trials_loop.addData('surveillance_response.corr', surveillance_response.corr)
            if surveillance_response.keys != None:  # we had a response
                surveillance_trials_loop.addData('surveillance_response.rt', surveillance_response.rt)
            # the Routine "surveillance_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'surveillance_trials_loop'
        
    # completed 1 repeats of 'surveillance_blocks_loop'
    
    mouse.setVisible(1)
    
    # set up handler to look after randomisation of conditions etc
    filler_1_instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions.xlsx', selection='4:6'),
        seed=None, name='filler_1_instructions_loop')
    thisExp.addLoop(filler_1_instructions_loop)  # add the loop to the experiment
    thisFiller_1_instructions_loop = filler_1_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFiller_1_instructions_loop.rgb)
    if thisFiller_1_instructions_loop != None:
        for paramName in thisFiller_1_instructions_loop:
            exec('{} = thisFiller_1_instructions_loop[paramName]'.format(paramName))
    
    for thisFiller_1_instructions_loop in filler_1_instructions_loop:
        currentLoop = filler_1_instructions_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFiller_1_instructions_loop.rgb)
        if thisFiller_1_instructions_loop != None:
            for paramName in thisFiller_1_instructions_loop:
                exec('{} = thisFiller_1_instructions_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(2, 'space')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        instructions_response = event.BuilderKeyResponse()
        text_instructions.setText(instructions_text)
        # keep track of which components have finished
        instructionsComponents = [instructions_response, text_instructions]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *instructions_response* updates
            if t >= 0.0 and instructions_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructions_response.tStart = t
                instructions_response.frameNStart = frameN  # exact frame index
                instructions_response.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if instructions_response.status == STARTED:
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
    # completed 1 repeats of 'filler_1_instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    filler_1_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/filler_1.xlsx'),
        seed=None, name='filler_1_loop')
    thisExp.addLoop(filler_1_loop)  # add the loop to the experiment
    thisFiller_1_loop = filler_1_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFiller_1_loop.rgb)
    if thisFiller_1_loop != None:
        for paramName in thisFiller_1_loop:
            exec('{} = thisFiller_1_loop[paramName]'.format(paramName))
    
    for thisFiller_1_loop in filler_1_loop:
        currentLoop = filler_1_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFiller_1_loop.rgb)
        if thisFiller_1_loop != None:
            for paramName in thisFiller_1_loop:
                exec('{} = thisFiller_1_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "filler_1"-------
        t = 0
        filler_1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(0.3, '3'), (0.6, 'return')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # write this value to disk
        thisExp.addData('condition', condition)
        filler_1_rating.reset()
        filler_1_text.setText(filler_1_items)
        # keep track of which components have finished
        filler_1Components = [filler_1_rating, filler_1_text]
        for thisComponent in filler_1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "filler_1"-------
        while continueRoutine:
            # get current time
            t = filler_1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *filler_1_rating* updates
            if t >= 0.0 and filler_1_rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                filler_1_rating.tStart = t
                filler_1_rating.frameNStart = frameN  # exact frame index
                filler_1_rating.setAutoDraw(True)
            continueRoutine &= filler_1_rating.noResponse  # a response ends the trial
            
            # *filler_1_text* updates
            if t >= 0.0 and filler_1_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                filler_1_text.tStart = t
                filler_1_text.frameNStart = frameN  # exact frame index
                filler_1_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in filler_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "filler_1"-------
        for thisComponent in filler_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # store data for filler_1_loop (TrialHandler)
        filler_1_loop.addData('filler_1_rating.response', filler_1_rating.getRating())
        filler_1_loop.addData('filler_1_rating.rt', filler_1_rating.getRT())
        # the Routine "filler_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'filler_1_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    filler_2_instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions.xlsx', selection='6:7'),
        seed=None, name='filler_2_instructions_loop')
    thisExp.addLoop(filler_2_instructions_loop)  # add the loop to the experiment
    thisFiller_2_instructions_loop = filler_2_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFiller_2_instructions_loop.rgb)
    if thisFiller_2_instructions_loop != None:
        for paramName in thisFiller_2_instructions_loop:
            exec('{} = thisFiller_2_instructions_loop[paramName]'.format(paramName))
    
    for thisFiller_2_instructions_loop in filler_2_instructions_loop:
        currentLoop = filler_2_instructions_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFiller_2_instructions_loop.rgb)
        if thisFiller_2_instructions_loop != None:
            for paramName in thisFiller_2_instructions_loop:
                exec('{} = thisFiller_2_instructions_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(2, 'space')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        instructions_response = event.BuilderKeyResponse()
        text_instructions.setText(instructions_text)
        # keep track of which components have finished
        instructionsComponents = [instructions_response, text_instructions]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *instructions_response* updates
            if t >= 0.0 and instructions_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructions_response.tStart = t
                instructions_response.frameNStart = frameN  # exact frame index
                instructions_response.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if instructions_response.status == STARTED:
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
    # completed 1 repeats of 'filler_2_instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    filler_2_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/filler_2.xlsx'),
        seed=None, name='filler_2_loop')
    thisExp.addLoop(filler_2_loop)  # add the loop to the experiment
    thisFiller_2_loop = filler_2_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFiller_2_loop.rgb)
    if thisFiller_2_loop != None:
        for paramName in thisFiller_2_loop:
            exec('{} = thisFiller_2_loop[paramName]'.format(paramName))
    
    for thisFiller_2_loop in filler_2_loop:
        currentLoop = filler_2_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFiller_2_loop.rgb)
        if thisFiller_2_loop != None:
            for paramName in thisFiller_2_loop:
                exec('{} = thisFiller_2_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "filler_2"-------
        t = 0
        filler_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(0.3, '3'), (0.6, 'return')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # write this value to disk
        thisExp.addData('condition', condition)
        filler_2_rating.reset()
        filler_2_text.setText(filler_2_items)
        # keep track of which components have finished
        filler_2Components = [filler_2_rating, filler_2_text]
        for thisComponent in filler_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "filler_2"-------
        while continueRoutine:
            # get current time
            t = filler_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *filler_2_rating* updates
            if t >= 0.0 and filler_2_rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                filler_2_rating.tStart = t
                filler_2_rating.frameNStart = frameN  # exact frame index
                filler_2_rating.setAutoDraw(True)
            continueRoutine &= filler_2_rating.noResponse  # a response ends the trial
            
            # *filler_2_text* updates
            if t >= 0.0 and filler_2_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                filler_2_text.tStart = t
                filler_2_text.frameNStart = frameN  # exact frame index
                filler_2_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in filler_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "filler_2"-------
        for thisComponent in filler_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # store data for filler_2_loop (TrialHandler)
        filler_2_loop.addData('filler_2_rating.response', filler_2_rating.getRating())
        filler_2_loop.addData('filler_2_rating.rt', filler_2_rating.getRT())
        # the Routine "filler_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'filler_2_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    evaluation_instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions.xlsx', selection='7:9'),
        seed=None, name='evaluation_instructions_loop')
    thisExp.addLoop(evaluation_instructions_loop)  # add the loop to the experiment
    thisEvaluation_instructions_loop = evaluation_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEvaluation_instructions_loop.rgb)
    if thisEvaluation_instructions_loop != None:
        for paramName in thisEvaluation_instructions_loop:
            exec('{} = thisEvaluation_instructions_loop[paramName]'.format(paramName))
    
    for thisEvaluation_instructions_loop in evaluation_instructions_loop:
        currentLoop = evaluation_instructions_loop
        # abbreviate parameter names if possible (e.g. rgb = thisEvaluation_instructions_loop.rgb)
        if thisEvaluation_instructions_loop != None:
            for paramName in thisEvaluation_instructions_loop:
                exec('{} = thisEvaluation_instructions_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(2, 'space')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        instructions_response = event.BuilderKeyResponse()
        text_instructions.setText(instructions_text)
        # keep track of which components have finished
        instructionsComponents = [instructions_response, text_instructions]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *instructions_response* updates
            if t >= 0.0 and instructions_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructions_response.tStart = t
                instructions_response.frameNStart = frameN  # exact frame index
                instructions_response.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if instructions_response.status == STARTED:
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
    # completed 1 repeats of 'evaluation_instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    evaluation_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions_evaluation.xlsx'),
        seed=None, name='evaluation_loop')
    thisExp.addLoop(evaluation_loop)  # add the loop to the experiment
    thisEvaluation_loop = evaluation_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEvaluation_loop.rgb)
    if thisEvaluation_loop != None:
        for paramName in thisEvaluation_loop:
            exec('{} = thisEvaluation_loop[paramName]'.format(paramName))
    
    for thisEvaluation_loop in evaluation_loop:
        currentLoop = evaluation_loop
        # abbreviate parameter names if possible (e.g. rgb = thisEvaluation_loop.rgb)
        if thisEvaluation_loop != None:
            for paramName in thisEvaluation_loop:
                exec('{} = thisEvaluation_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        evaluation_trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(evaluation_file_name),
            seed=None, name='evaluation_trials')
        thisExp.addLoop(evaluation_trials)  # add the loop to the experiment
        thisEvaluation_trial = evaluation_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisEvaluation_trial.rgb)
        if thisEvaluation_trial != None:
            for paramName in thisEvaluation_trial:
                exec('{} = thisEvaluation_trial[paramName]'.format(paramName))
        
        for thisEvaluation_trial in evaluation_trials:
            currentLoop = evaluation_trials
            # abbreviate parameter names if possible (e.g. rgb = thisEvaluation_trial.rgb)
            if thisEvaluation_trial != None:
                for paramName in thisEvaluation_trial:
                    exec('{} = thisEvaluation_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "evaluation_trial"-------
            t = 0
            evaluation_trialClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # simulate responses using ResponseEmulator, for testing
            if monkey:
                simulated_responses = [(0.1, 'e'), (0.1, 'i')]
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # write this value to disk
            thisExp.addData('condition', condition)
            evaluation_response = event.BuilderKeyResponse()
            evaluation_image.setImage(evaluation_stimulus)
            text_evaluations_instruction_middle.setText(middle_text)
            text_evaluations_instruction_left_top.setText(left_text)
            text_evaluations_instruction_right_top.setText(right_text)
            # keep track of which components have finished
            evaluation_trialComponents = [evaluation_response, evaluation_image, text_evaluations_instruction_middle, text_evaluations_instruction_left_top, text_evaluations_instruction_right_top, text_evaluations_instruction_left_bottom, text_evaluations_instruction_right_bottom]
            for thisComponent in evaluation_trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "evaluation_trial"-------
            while continueRoutine:
                # get current time
                t = evaluation_trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *evaluation_response* updates
                if t >= 0.0 and evaluation_response.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    evaluation_response.tStart = t
                    evaluation_response.frameNStart = frameN  # exact frame index
                    evaluation_response.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(evaluation_response.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if evaluation_response.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if evaluation_response.keys == []:  # then this was the first keypress
                            evaluation_response.keys = theseKeys[0]  # just the first key pressed
                            evaluation_response.rt = evaluation_response.clock.getTime()
                            # was this 'correct'?
                            if (evaluation_response.keys == str(evaluation_response_indicating_CS1_preferred)) or (evaluation_response.keys == evaluation_response_indicating_CS1_preferred):
                                evaluation_response.corr = 1
                            else:
                                evaluation_response.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                
                # *evaluation_image* updates
                if t >= 0.0 and evaluation_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    evaluation_image.tStart = t
                    evaluation_image.frameNStart = frameN  # exact frame index
                    evaluation_image.setAutoDraw(True)
                
                # *text_evaluations_instruction_middle* updates
                if t >= 0.0 and text_evaluations_instruction_middle.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_evaluations_instruction_middle.tStart = t
                    text_evaluations_instruction_middle.frameNStart = frameN  # exact frame index
                    text_evaluations_instruction_middle.setAutoDraw(True)
                
                # *text_evaluations_instruction_left_top* updates
                if t >= 0.0 and text_evaluations_instruction_left_top.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_evaluations_instruction_left_top.tStart = t
                    text_evaluations_instruction_left_top.frameNStart = frameN  # exact frame index
                    text_evaluations_instruction_left_top.setAutoDraw(True)
                
                # *text_evaluations_instruction_right_top* updates
                if t >= 0.0 and text_evaluations_instruction_right_top.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_evaluations_instruction_right_top.tStart = t
                    text_evaluations_instruction_right_top.frameNStart = frameN  # exact frame index
                    text_evaluations_instruction_right_top.setAutoDraw(True)
                
                # *text_evaluations_instruction_left_bottom* updates
                if t >= 0.0 and text_evaluations_instruction_left_bottom.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_evaluations_instruction_left_bottom.tStart = t
                    text_evaluations_instruction_left_bottom.frameNStart = frameN  # exact frame index
                    text_evaluations_instruction_left_bottom.setAutoDraw(True)
                
                # *text_evaluations_instruction_right_bottom* updates
                if t >= 0.0 and text_evaluations_instruction_right_bottom.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_evaluations_instruction_right_bottom.tStart = t
                    text_evaluations_instruction_right_bottom.frameNStart = frameN  # exact frame index
                    text_evaluations_instruction_right_bottom.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in evaluation_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "evaluation_trial"-------
            for thisComponent in evaluation_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if evaluation_response.keys in ['', [], None]:  # No response was made
                evaluation_response.keys=None
                # was no response the correct answer?!
                if str(evaluation_response_indicating_CS1_preferred).lower() == 'none':
                   evaluation_response.corr = 1;  # correct non-response
                else:
                   evaluation_response.corr = 0;  # failed to respond (incorrectly)
            # store data for evaluation_trials (TrialHandler)
            evaluation_trials.addData('evaluation_response.keys',evaluation_response.keys)
            evaluation_trials.addData('evaluation_response.corr', evaluation_response.corr)
            if evaluation_response.keys != None:  # we had a response
                evaluation_trials.addData('evaluation_response.rt', evaluation_response.rt)
            # the Routine "evaluation_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'evaluation_trials'
        
    # completed 1 repeats of 'evaluation_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    awareness_instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions.xlsx', selection='9:10'),
        seed=None, name='awareness_instructions_loop')
    thisExp.addLoop(awareness_instructions_loop)  # add the loop to the experiment
    thisAwareness_instructions_loop = awareness_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAwareness_instructions_loop.rgb)
    if thisAwareness_instructions_loop != None:
        for paramName in thisAwareness_instructions_loop:
            exec('{} = thisAwareness_instructions_loop[paramName]'.format(paramName))
    
    for thisAwareness_instructions_loop in awareness_instructions_loop:
        currentLoop = awareness_instructions_loop
        # abbreviate parameter names if possible (e.g. rgb = thisAwareness_instructions_loop.rgb)
        if thisAwareness_instructions_loop != None:
            for paramName in thisAwareness_instructions_loop:
                exec('{} = thisAwareness_instructions_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(2, 'space')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        instructions_response = event.BuilderKeyResponse()
        text_instructions.setText(instructions_text)
        # keep track of which components have finished
        instructionsComponents = [instructions_response, text_instructions]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *instructions_response* updates
            if t >= 0.0 and instructions_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructions_response.tStart = t
                instructions_response.frameNStart = frameN  # exact frame index
                instructions_response.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if instructions_response.status == STARTED:
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
    # completed 1 repeats of 'awareness_instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    awareness_1_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/awareness_1.xlsx'),
        seed=None, name='awareness_1_trials_loop')
    thisExp.addLoop(awareness_1_trials_loop)  # add the loop to the experiment
    thisAwareness_1_trials_loop = awareness_1_trials_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAwareness_1_trials_loop.rgb)
    if thisAwareness_1_trials_loop != None:
        for paramName in thisAwareness_1_trials_loop:
            exec('{} = thisAwareness_1_trials_loop[paramName]'.format(paramName))
    
    for thisAwareness_1_trials_loop in awareness_1_trials_loop:
        currentLoop = awareness_1_trials_loop
        # abbreviate parameter names if possible (e.g. rgb = thisAwareness_1_trials_loop.rgb)
        if thisAwareness_1_trials_loop != None:
            for paramName in thisAwareness_1_trials_loop:
                exec('{} = thisAwareness_1_trials_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "awareness_type_1_trial"-------
        t = 0
        awareness_type_1_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        theseKeys=""
        shift_flag = False
        awareness_type_1_show_response.alignHoriz ='left'
        
        # write this value to disk
        thisExp.addData('condition', condition)
        
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(2, 'return')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        awareness_type_1_question.setText(awareness_1_question_text)
        awareness_1_response = event.BuilderKeyResponse()
        # keep track of which components have finished
        awareness_type_1_trialComponents = [box, awareness_type_1_question, awareness_type_1_show_response, awareness_1_response]
        for thisComponent in awareness_type_1_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "awareness_type_1_trial"-------
        while continueRoutine:
            # get current time
            t = awareness_type_1_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            n = len(theseKeys)
            i = 0
            while i < n:
            
            # pressing RETURN ends the trial
                if theseKeys[i] == 'return' and len(inputText) >= 20:
                    continueRoutine = False
                    break
            
            # lose the final character
                elif theseKeys[i] == 'backspace':
                    inputText = inputText[:-1]  
                    i = i + 1
            
                elif theseKeys[i] == 'space':
                    inputText += ' '
                    i = i + 1
            
                elif theseKeys[i] == 'period':
                    inputText += '.'
                    i = i + 1
            
                elif theseKeys[i] == 'comma':
                    inputText += ','
                    i = i + 1
            
                elif theseKeys[i] == 'question':
                    inputText += '?'
                    i = i + 1
            
                elif theseKeys[i] == 'doublequote':
                    inputText += '"'
                    i = i + 1
            
                elif theseKeys[i] == 'minus':
                    inputText += u'ß'
                    i = i + 1
            
                elif theseKeys[i] == 'bracketleft':
                    inputText += u'ü'
                    i = i + 1
            
                elif theseKeys[i] == 'semicolon':
                    inputText += u'ö'
                    i = i + 1
            
                elif theseKeys[i] == 'apostrophe':
                    inputText += u'ä'
                    i = i + 1
            
                elif theseKeys[i] in ['lshift', 'rshift']:
                    shift_flag = True
                    i = i + 1
            
                else:
                    if len(theseKeys[i]) == 1:
                        # we only have 1 char so should be a normal key, 
                        # otherwise it might be 'ctrl' or similar so ignore it
                        if shift_flag:
                            inputText += chr( ord(theseKeys[i]) - ord(' '))
                            shift_flag = False
                        else:
                            inputText += theseKeys[i]
            
                    i = i + 1
            
            
            
            # *box* updates
            if t >= 0.0 and box.status == NOT_STARTED:
                # keep track of start time/frame for later
                box.tStart = t
                box.frameNStart = frameN  # exact frame index
                box.setAutoDraw(True)
            
            # *awareness_type_1_question* updates
            if t >= 0.0 and awareness_type_1_question.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_1_question.tStart = t
                awareness_type_1_question.frameNStart = frameN  # exact frame index
                awareness_type_1_question.setAutoDraw(True)
            
            # *awareness_type_1_show_response* updates
            if t >= 0.0 and awareness_type_1_show_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_1_show_response.tStart = t
                awareness_type_1_show_response.frameNStart = frameN  # exact frame index
                awareness_type_1_show_response.setAutoDraw(True)
            if awareness_type_1_show_response.status == STARTED:  # only update if drawing
                awareness_type_1_show_response.setText((inputText), log=False)
            
            # *awareness_1_response* updates
            if t >= 0.0 and awareness_1_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_1_response.tStart = t
                awareness_1_response.frameNStart = frameN  # exact frame index
                awareness_1_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(awareness_1_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if awareness_1_response.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    awareness_1_response.keys.extend(theseKeys)  # storing all keys
                    awareness_1_response.rt.append(awareness_1_response.clock.getTime())
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in awareness_type_1_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "awareness_type_1_trial"-------
        for thisComponent in awareness_type_1_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store the final text string into the results file
        thisExp.addData('inputText', inputText)
        inputText=""
        # check responses
        if awareness_1_response.keys in ['', [], None]:  # No response was made
            awareness_1_response.keys=None
        awareness_1_trials_loop.addData('awareness_1_response.keys',awareness_1_response.keys)
        if awareness_1_response.keys != None:  # we had a response
            awareness_1_trials_loop.addData('awareness_1_response.rt', awareness_1_response.rt)
        # the Routine "awareness_type_1_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'awareness_1_trials_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    awareness_2a_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/awareness_2a.xlsx'),
        seed=None, name='awareness_2a_trials_loop')
    thisExp.addLoop(awareness_2a_trials_loop)  # add the loop to the experiment
    thisAwareness_2a_trials_loop = awareness_2a_trials_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAwareness_2a_trials_loop.rgb)
    if thisAwareness_2a_trials_loop != None:
        for paramName in thisAwareness_2a_trials_loop:
            exec('{} = thisAwareness_2a_trials_loop[paramName]'.format(paramName))
    
    for thisAwareness_2a_trials_loop in awareness_2a_trials_loop:
        currentLoop = awareness_2a_trials_loop
        # abbreviate parameter names if possible (e.g. rgb = thisAwareness_2a_trials_loop.rgb)
        if thisAwareness_2a_trials_loop != None:
            for paramName in thisAwareness_2a_trials_loop:
                exec('{} = thisAwareness_2a_trials_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "awareness_type_2a_trial"-------
        t = 0
        awareness_type_2a_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(0.3, '1'), (0.6, 'return')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # write this value to disk
        thisExp.addData('condition', condition)
        awareness_type_2a_rating.reset()
        awareness_type_2a_text.setText(awareness_2a_question_text)
        # keep track of which components have finished
        awareness_type_2a_trialComponents = [awareness_type_2a_rating, awareness_type_2a_text]
        for thisComponent in awareness_type_2a_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "awareness_type_2a_trial"-------
        while continueRoutine:
            # get current time
            t = awareness_type_2a_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *awareness_type_2a_rating* updates
            if t >= 0.0 and awareness_type_2a_rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_2a_rating.tStart = t
                awareness_type_2a_rating.frameNStart = frameN  # exact frame index
                awareness_type_2a_rating.setAutoDraw(True)
            continueRoutine &= awareness_type_2a_rating.noResponse  # a response ends the trial
            
            # *awareness_type_2a_text* updates
            if t >= 0.0 and awareness_type_2a_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_2a_text.tStart = t
                awareness_type_2a_text.frameNStart = frameN  # exact frame index
                awareness_type_2a_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in awareness_type_2a_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "awareness_type_2a_trial"-------
        for thisComponent in awareness_type_2a_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # store data for awareness_2a_trials_loop (TrialHandler)
        awareness_2a_trials_loop.addData('awareness_type_2a_rating.response', awareness_type_2a_rating.getRating())
        awareness_2a_trials_loop.addData('awareness_type_2a_rating.rt', awareness_type_2a_rating.getRT())
        # the Routine "awareness_type_2a_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'awareness_2a_trials_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    awareness_2b_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/awareness_2b.xlsx'),
        seed=None, name='awareness_2b_trials_loop')
    thisExp.addLoop(awareness_2b_trials_loop)  # add the loop to the experiment
    thisAwareness_2b_trials_loop = awareness_2b_trials_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAwareness_2b_trials_loop.rgb)
    if thisAwareness_2b_trials_loop != None:
        for paramName in thisAwareness_2b_trials_loop:
            exec('{} = thisAwareness_2b_trials_loop[paramName]'.format(paramName))
    
    for thisAwareness_2b_trials_loop in awareness_2b_trials_loop:
        currentLoop = awareness_2b_trials_loop
        # abbreviate parameter names if possible (e.g. rgb = thisAwareness_2b_trials_loop.rgb)
        if thisAwareness_2b_trials_loop != None:
            for paramName in thisAwareness_2b_trials_loop:
                exec('{} = thisAwareness_2b_trials_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "awareness_type_2b_trial"-------
        t = 0
        awareness_type_2b_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(0.3, '1'), (0.6, 'return')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # write this value to disk
        thisExp.addData('condition', condition)
        awareness_type_2b_rating.reset()
        awareness_type_2b_text.setText(awareness_2b_question_text)
        # keep track of which components have finished
        awareness_type_2b_trialComponents = [awareness_type_2b_rating, awareness_type_2b_text]
        for thisComponent in awareness_type_2b_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "awareness_type_2b_trial"-------
        while continueRoutine:
            # get current time
            t = awareness_type_2b_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *awareness_type_2b_rating* updates
            if t >= 0.0 and awareness_type_2b_rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_2b_rating.tStart = t
                awareness_type_2b_rating.frameNStart = frameN  # exact frame index
                awareness_type_2b_rating.setAutoDraw(True)
            continueRoutine &= awareness_type_2b_rating.noResponse  # a response ends the trial
            
            # *awareness_type_2b_text* updates
            if t >= 0.0 and awareness_type_2b_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_2b_text.tStart = t
                awareness_type_2b_text.frameNStart = frameN  # exact frame index
                awareness_type_2b_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in awareness_type_2b_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "awareness_type_2b_trial"-------
        for thisComponent in awareness_type_2b_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # store data for awareness_2b_trials_loop (TrialHandler)
        awareness_2b_trials_loop.addData('awareness_type_2b_rating.response', awareness_type_2b_rating.getRating())
        awareness_2b_trials_loop.addData('awareness_type_2b_rating.rt', awareness_type_2b_rating.getRT())
        # the Routine "awareness_type_2b_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'awareness_2b_trials_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    awareness_2c_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/awareness_2c.xlsx'),
        seed=None, name='awareness_2c_trials_loop')
    thisExp.addLoop(awareness_2c_trials_loop)  # add the loop to the experiment
    thisAwareness_2c_trials_loop = awareness_2c_trials_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAwareness_2c_trials_loop.rgb)
    if thisAwareness_2c_trials_loop != None:
        for paramName in thisAwareness_2c_trials_loop:
            exec('{} = thisAwareness_2c_trials_loop[paramName]'.format(paramName))
    
    for thisAwareness_2c_trials_loop in awareness_2c_trials_loop:
        currentLoop = awareness_2c_trials_loop
        # abbreviate parameter names if possible (e.g. rgb = thisAwareness_2c_trials_loop.rgb)
        if thisAwareness_2c_trials_loop != None:
            for paramName in thisAwareness_2c_trials_loop:
                exec('{} = thisAwareness_2c_trials_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "awareness_type_2c_trial"-------
        t = 0
        awareness_type_2c_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(0.3, '1'), (0.6, 'return')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # write this value to disk
        thisExp.addData('condition', condition)
        awareness_type_2c_rating.reset()
        awareness_type_2c_text.setText(awareness_2_question_text)
        # keep track of which components have finished
        awareness_type_2c_trialComponents = [awareness_type_2c_rating, awareness_type_2c_text]
        for thisComponent in awareness_type_2c_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "awareness_type_2c_trial"-------
        while continueRoutine:
            # get current time
            t = awareness_type_2c_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *awareness_type_2c_rating* updates
            if t >= 0.0 and awareness_type_2c_rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_2c_rating.tStart = t
                awareness_type_2c_rating.frameNStart = frameN  # exact frame index
                awareness_type_2c_rating.setAutoDraw(True)
            continueRoutine &= awareness_type_2c_rating.noResponse  # a response ends the trial
            
            # *awareness_type_2c_text* updates
            if t >= 0.0 and awareness_type_2c_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                awareness_type_2c_text.tStart = t
                awareness_type_2c_text.frameNStart = frameN  # exact frame index
                awareness_type_2c_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in awareness_type_2c_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "awareness_type_2c_trial"-------
        for thisComponent in awareness_type_2c_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # store data for awareness_2c_trials_loop (TrialHandler)
        awareness_2c_trials_loop.addData('awareness_type_2c_rating.response', awareness_type_2c_rating.getRating())
        awareness_2c_trials_loop.addData('awareness_type_2c_rating.rt', awareness_type_2c_rating.getRT())
        # the Routine "awareness_type_2c_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'awareness_2c_trials_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    end_message_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('text/instructions.xlsx', selection='10:11'),
        seed=None, name='end_message_loop')
    thisExp.addLoop(end_message_loop)  # add the loop to the experiment
    thisEnd_message_loop = end_message_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnd_message_loop.rgb)
    if thisEnd_message_loop != None:
        for paramName in thisEnd_message_loop:
            exec('{} = thisEnd_message_loop[paramName]'.format(paramName))
    
    for thisEnd_message_loop in end_message_loop:
        currentLoop = end_message_loop
        # abbreviate parameter names if possible (e.g. rgb = thisEnd_message_loop.rgb)
        if thisEnd_message_loop != None:
            for paramName in thisEnd_message_loop:
                exec('{} = thisEnd_message_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # simulate responses using ResponseEmulator, for testing
        if monkey:
            simulated_responses = [(2, 'space')]
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        instructions_response = event.BuilderKeyResponse()
        text_instructions.setText(instructions_text)
        # keep track of which components have finished
        instructionsComponents = [instructions_response, text_instructions]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *instructions_response* updates
            if t >= 0.0 and instructions_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructions_response.tStart = t
                instructions_response.frameNStart = frameN  # exact frame index
                instructions_response.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if instructions_response.status == STARTED:
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
    # completed 1 repeats of 'end_message_loop'
    
# completed 1 repeats of 'record_data_collection_site_variable'
















# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
