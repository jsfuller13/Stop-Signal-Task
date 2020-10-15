#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on January 02, 2020, at 10:12
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'SST 1-2-20'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='C:\\Users\\Jordan\\Documents\\Experiment Building\\3. Stop Signal Task\\SST 1-2-20_lastrun.py',
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
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='Built_In_Display', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "B1_Instr"
B1_InstrClock = core.Clock()
instr_text = visual.TextStim(win=win, name='instr_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cont_text = visual.TextStim(win=win, name='cont_text',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fix_cue_text = visual.TextStim(win=win, name='fix_cue_text',
    text='F = Animal  J = Not Animal',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "B1_Trials"
B1_TrialsClock = core.Clock()
B1_stim_txt = visual.TextStim(win=win, name='B1_stim_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
B1_trial_cue_text = visual.TextStim(win=win, name='B1_trial_cue_text',
    text='F = Animal  J = Not Animal',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "B2_Instr"
B2_InstrClock = core.Clock()
B2_instr_txt = visual.TextStim(win=win, name='B2_instr_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
B2_cont_txt = visual.TextStim(win=win, name='B2_cont_txt',
    text='default text',
    font='Arial',
    pos=(0, -0.40), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fix_cue_text = visual.TextStim(win=win, name='fix_cue_text',
    text='F = Animal  J = Not Animal',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "B2_Trials"
B2_TrialsClock = core.Clock()
B2_stim_text = visual.TextStim(win=win, name='B2_stim_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
signal = sound.Sound('A', secs=0.1, stereo=True)
signal.setVolume(1.0)
B2_trial_cue_text = visual.TextStim(win=win, name='B2_trial_cue_text',
    text='F = Animal  J = Not Animal',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Thank_You"
Thank_YouClock = core.Clock()
thanks_txt = visual.TextStim(win=win, name='thanks_txt',
    text='Good work!\n\nYou have finished this task. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
thanks_cont_text = visual.TextStim(win=win, name='thanks_cont_text',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
b1_instuctions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SST_Instr.xlsx'),
    seed=None, name='b1_instuctions')
thisExp.addLoop(b1_instuctions)  # add the loop to the experiment
thisB1_instuction = b1_instuctions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB1_instuction.rgb)
if thisB1_instuction != None:
    for paramName in thisB1_instuction:
        exec('{} = thisB1_instuction[paramName]'.format(paramName))

for thisB1_instuction in b1_instuctions:
    currentLoop = b1_instuctions
    # abbreviate parameter names if possible (e.g. rgb = thisB1_instuction.rgb)
    if thisB1_instuction != None:
        for paramName in thisB1_instuction:
            exec('{} = thisB1_instuction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "B1_Instr"-------
    t = 0
    B1_InstrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instr_text.setText(instr_txt)
    key_resp = keyboard.Keyboard()
    cont_text.setText(cont_txt)
    # keep track of which components have finished
    B1_InstrComponents = [instr_text, key_resp, cont_text]
    for thisComponent in B1_InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "B1_Instr"-------
    while continueRoutine:
        # get current time
        t = B1_InstrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_text* updates
        if t >= 0.0 and instr_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr_text.tStart = t  # not accounting for scr refresh
            instr_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
            instr_text.setAutoDraw(True)
        
        # *key_resp* updates
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *cont_text* updates
        if t >= 0.0 and cont_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            cont_text.tStart = t  # not accounting for scr refresh
            cont_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(cont_text, 'tStartRefresh')  # time at next scr refresh
            cont_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B1_InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B1_Instr"-------
    for thisComponent in B1_InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "B1_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'b1_instuctions'


# set up handler to look after randomisation of conditions etc
B1_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SST_B1.xlsx'),
    seed=None, name='B1_trials')
thisExp.addLoop(B1_trials)  # add the loop to the experiment
thisB1_trial = B1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB1_trial.rgb)
if thisB1_trial != None:
    for paramName in thisB1_trial:
        exec('{} = thisB1_trial[paramName]'.format(paramName))

for thisB1_trial in B1_trials:
    currentLoop = B1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisB1_trial.rgb)
    if thisB1_trial != None:
        for paramName in thisB1_trial:
            exec('{} = thisB1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_cross, fix_cue_text]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 1.0 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t  # not accounting for scr refresh
            fixation_cross.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        frameRemains = 1.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation_cross.tStop = t  # not accounting for scr refresh
            fixation_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(False)
        
        # *fix_cue_text* updates
        if t >= 0.0 and fix_cue_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cue_text.tStart = t  # not accounting for scr refresh
            fix_cue_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cue_text, 'tStartRefresh')  # time at next scr refresh
            fix_cue_text.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix_cue_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fix_cue_text.tStop = t  # not accounting for scr refresh
            fix_cue_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cue_text, 'tStopRefresh')  # time at next scr refresh
            fix_cue_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "B1_Trials"-------
    t = 0
    B1_TrialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    B1_stim_txt.setText(B1_stim)
    B1_resp = keyboard.Keyboard()
    if B1_trials.thisN == 0:
        RT_list = []
    # keep track of which components have finished
    B1_TrialsComponents = [B1_stim_txt, B1_resp, B1_trial_cue_text]
    for thisComponent in B1_TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "B1_Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = B1_TrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B1_stim_txt* updates
        if t >= 0 and B1_stim_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            B1_stim_txt.tStart = t  # not accounting for scr refresh
            B1_stim_txt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B1_stim_txt, 'tStartRefresh')  # time at next scr refresh
            B1_stim_txt.setAutoDraw(True)
        frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if B1_stim_txt.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            B1_stim_txt.tStop = t  # not accounting for scr refresh
            B1_stim_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(B1_stim_txt, 'tStopRefresh')  # time at next scr refresh
            B1_stim_txt.setAutoDraw(False)
        
        # *B1_resp* updates
        if t >= 0 and B1_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            B1_resp.tStart = t  # not accounting for scr refresh
            B1_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B1_resp, 'tStartRefresh')  # time at next scr refresh
            B1_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(B1_resp.clock.reset)  # t=0 on next screen flip
        frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if B1_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            B1_resp.tStop = t  # not accounting for scr refresh
            B1_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(B1_resp, 'tStopRefresh')  # time at next scr refresh
            B1_resp.status = FINISHED
        if B1_resp.status == STARTED:
            theseKeys = B1_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                B1_resp.keys = theseKeys.name  # just the last key pressed
                B1_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (B1_resp.keys == str(B1_correct)) or (B1_resp.keys == B1_correct):
                    B1_resp.corr = 1
                else:
                    B1_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *B1_trial_cue_text* updates
        if t >= 0.0 and B1_trial_cue_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            B1_trial_cue_text.tStart = t  # not accounting for scr refresh
            B1_trial_cue_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B1_trial_cue_text, 'tStartRefresh')  # time at next scr refresh
            B1_trial_cue_text.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if B1_trial_cue_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            B1_trial_cue_text.tStop = t  # not accounting for scr refresh
            B1_trial_cue_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(B1_trial_cue_text, 'tStopRefresh')  # time at next scr refresh
            B1_trial_cue_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B1_TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B1_Trials"-------
    for thisComponent in B1_TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if B1_resp.keys in ['', [], None]:  # No response was made
        B1_resp.keys = None
        # was no response the correct answer?!
        if str(B1_correct).lower() == 'none':
           B1_resp.corr = 1;  # correct non-response
        else:
           B1_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for B1_trials (TrialHandler)
    B1_trials.addData('B1_resp.keys',B1_resp.keys)
    B1_trials.addData('B1_resp.corr', B1_resp.corr)
    if B1_resp.keys != None:  # we had a response
        B1_trials.addData('B1_resp.rt', B1_resp.rt)
    RT_list.append(B1_resp.rt)
    thisExp.addData('RT_list', RT_list)
    thisExp.nextEntry()
    
# completed 1 repeats of 'B1_trials'


# set up handler to look after randomisation of conditions etc
B2_instr = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('B2_instr.xlsx'),
    seed=None, name='B2_instr')
thisExp.addLoop(B2_instr)  # add the loop to the experiment
thisB2_instr = B2_instr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB2_instr.rgb)
if thisB2_instr != None:
    for paramName in thisB2_instr:
        exec('{} = thisB2_instr[paramName]'.format(paramName))

for thisB2_instr in B2_instr:
    currentLoop = B2_instr
    # abbreviate parameter names if possible (e.g. rgb = thisB2_instr.rgb)
    if thisB2_instr != None:
        for paramName in thisB2_instr:
            exec('{} = thisB2_instr[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "B2_Instr"-------
    t = 0
    B2_InstrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    B2_instr_txt.setText(instr_txt)
    B2_instr_resp = keyboard.Keyboard()
    B2_cont_txt.setText(cont_txt)
    # keep track of which components have finished
    B2_InstrComponents = [B2_instr_txt, B2_instr_resp, B2_cont_txt]
    for thisComponent in B2_InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "B2_Instr"-------
    while continueRoutine:
        # get current time
        t = B2_InstrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B2_instr_txt* updates
        if t >= 0.0 and B2_instr_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            B2_instr_txt.tStart = t  # not accounting for scr refresh
            B2_instr_txt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B2_instr_txt, 'tStartRefresh')  # time at next scr refresh
            B2_instr_txt.setAutoDraw(True)
        
        # *B2_instr_resp* updates
        if t >= 0.0 and B2_instr_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            B2_instr_resp.tStart = t  # not accounting for scr refresh
            B2_instr_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B2_instr_resp, 'tStartRefresh')  # time at next scr refresh
            B2_instr_resp.status = STARTED
            # keyboard checking is just starting
            B2_instr_resp.clearEvents(eventType='keyboard')
        if B2_instr_resp.status == STARTED:
            theseKeys = B2_instr_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *B2_cont_txt* updates
        if t >= 0.0 and B2_cont_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            B2_cont_txt.tStart = t  # not accounting for scr refresh
            B2_cont_txt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B2_cont_txt, 'tStartRefresh')  # time at next scr refresh
            B2_cont_txt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B2_InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B2_Instr"-------
    for thisComponent in B2_InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "B2_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'B2_instr'


# set up handler to look after randomisation of conditions etc
B2_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SST_B2.xlsx'),
    seed=None, name='B2_trials')
thisExp.addLoop(B2_trials)  # add the loop to the experiment
thisB2_trial = B2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB2_trial.rgb)
if thisB2_trial != None:
    for paramName in thisB2_trial:
        exec('{} = thisB2_trial[paramName]'.format(paramName))

for thisB2_trial in B2_trials:
    currentLoop = B2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisB2_trial.rgb)
    if thisB2_trial != None:
        for paramName in thisB2_trial:
            exec('{} = thisB2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_cross, fix_cue_text]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 1.0 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t  # not accounting for scr refresh
            fixation_cross.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        frameRemains = 1.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation_cross.tStop = t  # not accounting for scr refresh
            fixation_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(False)
        
        # *fix_cue_text* updates
        if t >= 0.0 and fix_cue_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cue_text.tStart = t  # not accounting for scr refresh
            fix_cue_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cue_text, 'tStartRefresh')  # time at next scr refresh
            fix_cue_text.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix_cue_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fix_cue_text.tStop = t  # not accounting for scr refresh
            fix_cue_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cue_text, 'tStopRefresh')  # time at next scr refresh
            fix_cue_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "B2_Trials"-------
    t = 0
    B2_TrialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    B2_stim_text.setText(B2_stim
)
    B2_resp = keyboard.Keyboard()
    signal.setSound('A', secs=0.1)
    signal.setVolume(sig_volume, log=False)
    # keep track of which components have finished
    B2_TrialsComponents = [B2_stim_text, B2_resp, signal, B2_trial_cue_text]
    for thisComponent in B2_TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "B2_Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = B2_TrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B2_stim_text* updates
        if t >= 0 and B2_stim_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            B2_stim_text.tStart = t  # not accounting for scr refresh
            B2_stim_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B2_stim_text, 'tStartRefresh')  # time at next scr refresh
            B2_stim_text.setAutoDraw(True)
        frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if B2_stim_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            B2_stim_text.tStop = t  # not accounting for scr refresh
            B2_stim_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(B2_stim_text, 'tStopRefresh')  # time at next scr refresh
            B2_stim_text.setAutoDraw(False)
        
        # *B2_resp* updates
        if t >= 0 and B2_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            B2_resp.tStart = t  # not accounting for scr refresh
            B2_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B2_resp, 'tStartRefresh')  # time at next scr refresh
            B2_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(B2_resp.clock.reset)  # t=0 on next screen flip
            B2_resp.clearEvents(eventType='keyboard')
        frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if B2_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            B2_resp.tStop = t  # not accounting for scr refresh
            B2_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(B2_resp, 'tStopRefresh')  # time at next scr refresh
            B2_resp.status = FINISHED
        if B2_resp.status == STARTED:
            theseKeys = B2_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                B2_resp.keys = theseKeys.name  # just the last key pressed
                B2_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (B2_resp.keys == str(B2_correct)) or (B2_resp.keys == B2_correct):
                    B2_resp.corr = 1
                else:
                    B2_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop signal
        if t >= 0 and signal.status == NOT_STARTED:
            # keep track of start time/frame for later
            signal.tStart = t  # not accounting for scr refresh
            signal.frameNStart = frameN  # exact frame index
            win.timeOnFlip(signal, 'tStartRefresh')  # time at next scr refresh
            signal.play()  # start the sound (it finishes automatically)
        frameRemains = 0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if signal.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            signal.tStop = t  # not accounting for scr refresh
            signal.frameNStop = frameN  # exact frame index
            win.timeOnFlip(signal, 'tStopRefresh')  # time at next scr refresh
            if 0.1 > 0.5:  # don't force-stop brief sounds
                signal.stop()
        
        # *B2_trial_cue_text* updates
        if t >= 0.0 and B2_trial_cue_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            B2_trial_cue_text.tStart = t  # not accounting for scr refresh
            B2_trial_cue_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B2_trial_cue_text, 'tStartRefresh')  # time at next scr refresh
            B2_trial_cue_text.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if B2_trial_cue_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            B2_trial_cue_text.tStop = t  # not accounting for scr refresh
            B2_trial_cue_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(B2_trial_cue_text, 'tStopRefresh')  # time at next scr refresh
            B2_trial_cue_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B2_TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B2_Trials"-------
    for thisComponent in B2_TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if B2_resp.keys in ['', [], None]:  # No response was made
        B2_resp.keys = None
        # was no response the correct answer?!
        if str(B2_correct).lower() == 'none':
           B2_resp.corr = 1;  # correct non-response
        else:
           B2_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for B2_trials (TrialHandler)
    B2_trials.addData('B2_resp.keys',B2_resp.keys)
    B2_trials.addData('B2_resp.corr', B2_resp.corr)
    if B2_resp.keys != None:  # we had a response
        B2_trials.addData('B2_resp.rt', B2_resp.rt)
    signal.stop()  # ensure sound has stopped at end of routine
    B2_trials.addData('signal.started', signal.tStart)
    B2_trials.addData('signal.stopped', signal.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'B2_trials'


# ------Prepare to start Routine "Thank_You"-------
t = 0
Thank_YouClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
thanks_resp = keyboard.Keyboard()
# keep track of which components have finished
Thank_YouComponents = [thanks_txt, thanks_resp, thanks_cont_text]
for thisComponent in Thank_YouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thank_You"-------
while continueRoutine:
    # get current time
    t = Thank_YouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_txt* updates
    if t >= 0.0 and thanks_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_txt.tStart = t  # not accounting for scr refresh
        thanks_txt.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanks_txt, 'tStartRefresh')  # time at next scr refresh
        thanks_txt.setAutoDraw(True)
    
    # *thanks_resp* updates
    if t >= 0.0 and thanks_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_resp.tStart = t  # not accounting for scr refresh
        thanks_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanks_resp, 'tStartRefresh')  # time at next scr refresh
        thanks_resp.status = STARTED
        # keyboard checking is just starting
        thanks_resp.clearEvents(eventType='keyboard')
    if thanks_resp.status == STARTED:
        theseKeys = thanks_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *thanks_cont_text* updates
    if t >= 0.0 and thanks_cont_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_cont_text.tStart = t  # not accounting for scr refresh
        thanks_cont_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanks_cont_text, 'tStartRefresh')  # time at next scr refresh
        thanks_cont_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_YouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_You"-------
for thisComponent in Thank_YouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thank_You" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
