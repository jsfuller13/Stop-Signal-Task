#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 01, 2019, at 14:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '3.2.3'
expName = 'SST b1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Jordan\\Documents\\Experiment Building\\3. Stop Signal Task\\SST b1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
key_resp = keyboard.Keyboard()
cont_text = visual.TextStim(win=win, name='cont_text',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "B1_Trials"
B1_TrialsClock = core.Clock()
B1_stim_txt = visual.TextStim(win=win, name='B1_stim_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
B1_resp = keyboard.Keyboard()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Thank_You"
Thank_YouClock = core.Clock()
thanks_txt = visual.TextStim(win=win, name='thanks_txt',
    text='Good work!\n\nYou have finished this task. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
thanks_resp = keyboard.Keyboard()
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
B1_instr = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SST_Instr.xlsx', selection='0:1'),
    seed=None, name='B1_instr')
thisExp.addLoop(B1_instr)  # add the loop to the experiment
thisB1_instr = B1_instr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB1_instr.rgb)
if thisB1_instr != None:
    for paramName in thisB1_instr:
        exec('{} = thisB1_instr[paramName]'.format(paramName))

for thisB1_instr in B1_instr:
    currentLoop = B1_instr
    # abbreviate parameter names if possible (e.g. rgb = thisB1_instr.rgb)
    if thisB1_instr != None:
        for paramName in thisB1_instr:
            exec('{} = thisB1_instr[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "B1_Instr"-------
    # update component parameters for each repeat
    instr_text.setText(instr_txt)
    key_resp.keys = []
    key_resp.rt = []
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
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    B1_InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "B1_Instr"-------
    while continueRoutine:
        # get current time
        t = B1_InstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=B1_InstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_text* updates
        if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_text.frameNStart = frameN  # exact frame index
            instr_text.tStart = t  # local t and not account for scr refresh
            instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
            instr_text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *cont_text* updates
        if cont_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_text.frameNStart = frameN  # exact frame index
            cont_text.tStart = t  # local t and not account for scr refresh
            cont_text.tStartRefresh = tThisFlipGlobal  # on global time
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
# completed 1 repeats of 'B1_instr'


# set up handler to look after randomisation of conditions etc
B1_trials = data.TrialHandler(nReps=24, method='random', 
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
    
    # ------Prepare to start Routine "B1_Trials"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    B1_stim_txt.setText(B1_stim)
    B1_resp.keys = []
    B1_resp.rt = []
    # keep track of which components have finished
    B1_TrialsComponents = [B1_stim_txt, B1_resp, fixation]
    for thisComponent in B1_TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    B1_TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "B1_Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = B1_TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=B1_TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B1_stim_txt* updates
        if B1_stim_txt.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            B1_stim_txt.frameNStart = frameN  # exact frame index
            B1_stim_txt.tStart = t  # local t and not account for scr refresh
            B1_stim_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B1_stim_txt, 'tStartRefresh')  # time at next scr refresh
            B1_stim_txt.setAutoDraw(True)
        if B1_stim_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B1_stim_txt.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                B1_stim_txt.tStop = t  # not accounting for scr refresh
                B1_stim_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B1_stim_txt, 'tStopRefresh')  # time at next scr refresh
                B1_stim_txt.setAutoDraw(False)
        
        # *B1_resp* updates
        waitOnFlip = False
        if B1_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            B1_resp.frameNStart = frameN  # exact frame index
            B1_resp.tStart = t  # local t and not account for scr refresh
            B1_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B1_resp, 'tStartRefresh')  # time at next scr refresh
            B1_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(B1_resp.clock.reset)  # t=0 on next screen flip
        if B1_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B1_resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                B1_resp.tStop = t  # not accounting for scr refresh
                B1_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B1_resp, 'tStopRefresh')  # time at next scr refresh
                B1_resp.status = FINISHED
        if B1_resp.status == STARTED and not waitOnFlip:
            theseKeys = B1_resp.getKeys(keyList=['fj'], waitRelease=False)
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
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
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
    thisExp.nextEntry()
    
# completed 24 repeats of 'B1_trials'


# ------Prepare to start Routine "Thank_You"-------
# update component parameters for each repeat
thanks_resp.keys = []
thanks_resp.rt = []
# keep track of which components have finished
Thank_YouComponents = [thanks_txt, thanks_resp, thanks_cont_text]
for thisComponent in Thank_YouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Thank_YouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Thank_You"-------
while continueRoutine:
    # get current time
    t = Thank_YouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Thank_YouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_txt* updates
    if thanks_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_txt.frameNStart = frameN  # exact frame index
        thanks_txt.tStart = t  # local t and not account for scr refresh
        thanks_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_txt, 'tStartRefresh')  # time at next scr refresh
        thanks_txt.setAutoDraw(True)
    
    # *thanks_resp* updates
    waitOnFlip = False
    if thanks_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_resp.frameNStart = frameN  # exact frame index
        thanks_resp.tStart = t  # local t and not account for scr refresh
        thanks_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_resp, 'tStartRefresh')  # time at next scr refresh
        thanks_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(thanks_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if thanks_resp.status == STARTED and not waitOnFlip:
        theseKeys = thanks_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *thanks_cont_text* updates
    if thanks_cont_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_cont_text.frameNStart = frameN  # exact frame index
        thanks_cont_text.tStart = t  # local t and not account for scr refresh
        thanks_cont_text.tStartRefresh = tThisFlipGlobal  # on global time
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
