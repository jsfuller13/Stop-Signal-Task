/******************* 
 * Sst 1-2-20 Test *
 *******************/

import { PsychoJS } from 'https://pavlovia.org/lib/core-3.2.js';
import * as core from 'https://pavlovia.org/lib/core-3.2.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data-3.2.js';
import { Scheduler } from 'https://pavlovia.org/lib/util-3.2.js';
import * as util from 'https://pavlovia.org/lib/util-3.2.js';
import * as visual from 'https://pavlovia.org/lib/visual-3.2.js';
import { Sound } from 'https://pavlovia.org/lib/sound-3.2.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'SST 1-2-20';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const b1_instuctionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(b1_instuctionsLoopBegin, b1_instuctionsLoopScheduler);
flowScheduler.add(b1_instuctionsLoopScheduler);
flowScheduler.add(b1_instuctionsLoopEnd);
const B1_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(B1_trialsLoopBegin, B1_trialsLoopScheduler);
flowScheduler.add(B1_trialsLoopScheduler);
flowScheduler.add(B1_trialsLoopEnd);
const B2_instrLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(B2_instrLoopBegin, B2_instrLoopScheduler);
flowScheduler.add(B2_instrLoopScheduler);
flowScheduler.add(B2_instrLoopEnd);
const B2_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(B2_trialsLoopBegin, B2_trialsLoopScheduler);
flowScheduler.add(B2_trialsLoopScheduler);
flowScheduler.add(B2_trialsLoopEnd);
flowScheduler.add(Thank_YouRoutineBegin);
flowScheduler.add(Thank_YouRoutineEachFrame);
flowScheduler.add(Thank_YouRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var B1_InstrClock;
var instr_text;
var key_resp;
var cont_text;
var fixationClock;
var fixation_cross;
var fix_cue_text;
var B1_TrialsClock;
var B1_stim_txt;
var B1_resp;
var B1_trial_cue_text;
var B2_InstrClock;
var B2_instr_txt;
var B2_instr_resp;
var B2_cont_txt;
var B2_TrialsClock;
var B2_stim_text;
var B2_resp;
var signal;
var B2_trial_cue_text;
var Thank_YouClock;
var thanks_txt;
var thanks_resp;
var thanks_cont_text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "B1_Instr"
  B1_InstrClock = new util.Clock();
  instr_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  cont_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'cont_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_cross',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  fix_cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cue_text',
    text: 'F = Animal  J = Not Animal',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "B1_Trials"
  B1_TrialsClock = new util.Clock();
  B1_stim_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'B1_stim_txt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  B1_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  B1_trial_cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'B1_trial_cue_text',
    text: 'F = Animal  J = Not Animal',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "B2_Instr"
  B2_InstrClock = new util.Clock();
  B2_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'B2_instr_txt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  B2_instr_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  B2_cont_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'B2_cont_txt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_cross',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  fix_cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cue_text',
    text: 'F = Animal  J = Not Animal',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "B2_Trials"
  B2_TrialsClock = new util.Clock();
  B2_stim_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'B2_stim_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  B2_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  signal = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.1,
    });
  signal.setVolume(1.0);
  B2_trial_cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'B2_trial_cue_text',
    text: 'F = Animal  J = Not Animal',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Thank_You"
  Thank_YouClock = new util.Clock();
  thanks_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks_txt',
    text: 'Good work!\n\nYou have finished this task. ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  thanks_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  thanks_cont_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks_cont_text',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var b1_instuctions;
var currentLoop;
function b1_instuctionsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  b1_instuctions = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SST_Instr.xlsx',
    seed: undefined, name: 'b1_instuctions'});
  psychoJS.experiment.addLoop(b1_instuctions); // add the loop to the experiment
  currentLoop = b1_instuctions;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB1_instuction of b1_instuctions) {
    thisScheduler.add(importConditions(b1_instuctions));
    thisScheduler.add(B1_InstrRoutineBegin);
    thisScheduler.add(B1_InstrRoutineEachFrame);
    thisScheduler.add(B1_InstrRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function b1_instuctionsLoopEnd() {
  psychoJS.experiment.removeLoop(b1_instuctions);

  return Scheduler.Event.NEXT;
}

var B1_trials;
function B1_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B1_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SST_B1.xlsx',
    seed: undefined, name: 'B1_trials'});
  psychoJS.experiment.addLoop(B1_trials); // add the loop to the experiment
  currentLoop = B1_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB1_trial of B1_trials) {
    thisScheduler.add(importConditions(B1_trials));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(B1_TrialsRoutineBegin);
    thisScheduler.add(B1_TrialsRoutineEachFrame);
    thisScheduler.add(B1_TrialsRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function B1_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(B1_trials);

  return Scheduler.Event.NEXT;
}

var B2_instr;
function B2_instrLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B2_instr = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'B2_instr.xlsx',
    seed: undefined, name: 'B2_instr'});
  psychoJS.experiment.addLoop(B2_instr); // add the loop to the experiment
  currentLoop = B2_instr;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB2_instr of B2_instr) {
    thisScheduler.add(importConditions(B2_instr));
    thisScheduler.add(B2_InstrRoutineBegin);
    thisScheduler.add(B2_InstrRoutineEachFrame);
    thisScheduler.add(B2_InstrRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function B2_instrLoopEnd() {
  psychoJS.experiment.removeLoop(B2_instr);

  return Scheduler.Event.NEXT;
}

var B2_trials;
function B2_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B2_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SST_B2.xlsx',
    seed: undefined, name: 'B2_trials'});
  psychoJS.experiment.addLoop(B2_trials); // add the loop to the experiment
  currentLoop = B2_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB2_trial of B2_trials) {
    thisScheduler.add(importConditions(B2_trials));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(B2_TrialsRoutineBegin);
    thisScheduler.add(B2_TrialsRoutineEachFrame);
    thisScheduler.add(B2_TrialsRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function B2_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(B2_trials);

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var B1_InstrComponents;
function B1_InstrRoutineBegin() {
  //------Prepare to start Routine 'B1_Instr'-------
  t = 0;
  B1_InstrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instr_text.setText(instr_txt);
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  cont_text.setText(cont_txt);
  // keep track of which components have finished
  B1_InstrComponents = [];
  B1_InstrComponents.push(instr_text);
  B1_InstrComponents.push(key_resp);
  B1_InstrComponents.push(cont_text);
  
  for (const thisComponent of B1_InstrComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function B1_InstrRoutineEachFrame() {
  //------Loop for each frame of Routine 'B1_Instr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = B1_InstrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_text* updates
  if (t >= 0.0 && instr_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_text.tStart = t;  // (not accounting for frame time here)
    instr_text.frameNStart = frameN;  // exact frame index
    instr_text.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *cont_text* updates
  if (t >= 0.0 && cont_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cont_text.tStart = t;  // (not accounting for frame time here)
    cont_text.frameNStart = frameN;  // exact frame index
    cont_text.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of B1_InstrComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function B1_InstrRoutineEnd() {
  //------Ending Routine 'B1_Instr'-------
  for (const thisComponent of B1_InstrComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "B1_Instr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var fixationComponents;
function fixationRoutineBegin() {
  //------Prepare to start Routine 'fixation'-------
  t = 0;
  fixationClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  fixationComponents = [];
  fixationComponents.push(fixation_cross);
  fixationComponents.push(fix_cue_text);
  
  for (const thisComponent of fixationComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function fixationRoutineEachFrame() {
  //------Loop for each frame of Routine 'fixation'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = fixationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *fixation_cross* updates
  if (t >= 1.0 && fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fixation_cross.tStart = t;  // (not accounting for frame time here)
    fixation_cross.frameNStart = frameN;  // exact frame index
    fixation_cross.setAutoDraw(true);
  }

  frameRemains = 1.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    fixation_cross.setAutoDraw(false);
  }
  
  // *fix_cue_text* updates
  if (t >= 0.0 && fix_cue_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fix_cue_text.tStart = t;  // (not accounting for frame time here)
    fix_cue_text.frameNStart = frameN;  // exact frame index
    fix_cue_text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (fix_cue_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    fix_cue_text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of fixationComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function fixationRoutineEnd() {
  //------Ending Routine 'fixation'-------
  for (const thisComponent of fixationComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var B1_TrialsComponents;
function B1_TrialsRoutineBegin() {
  //------Prepare to start Routine 'B1_Trials'-------
  t = 0;
  B1_TrialsClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  B1_stim_txt.setText(B1_stim);
  B1_resp.keys = undefined;
  B1_resp.rt = undefined;
  // keep track of which components have finished
  B1_TrialsComponents = [];
  B1_TrialsComponents.push(B1_stim_txt);
  B1_TrialsComponents.push(B1_resp);
  B1_TrialsComponents.push(B1_trial_cue_text);
  
  for (const thisComponent of B1_TrialsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function B1_TrialsRoutineEachFrame() {
  //------Loop for each frame of Routine 'B1_Trials'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = B1_TrialsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *B1_stim_txt* updates
  if (t >= 0 && B1_stim_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B1_stim_txt.tStart = t;  // (not accounting for frame time here)
    B1_stim_txt.frameNStart = frameN;  // exact frame index
    B1_stim_txt.setAutoDraw(true);
  }

  frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B1_stim_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B1_stim_txt.setAutoDraw(false);
  }
  
  // *B1_resp* updates
  if (t >= 0 && B1_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B1_resp.tStart = t;  // (not accounting for frame time here)
    B1_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { B1_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { B1_resp.start(); }); // start on screen flip
  }

  frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B1_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B1_resp.status = PsychoJS.Status.FINISHED;
  }

  if (B1_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = B1_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      B1_resp.keys = theseKeys[0].name;  // just the last key pressed
      B1_resp.rt = theseKeys[0].rt;
      // was this 'correct'?
      if (B1_resp.keys === B1_correct) {
          B1_resp.corr = 1;
      } else {
          B1_resp.corr = 0;
      }
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *B1_trial_cue_text* updates
  if (t >= 0.0 && B1_trial_cue_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B1_trial_cue_text.tStart = t;  // (not accounting for frame time here)
    B1_trial_cue_text.frameNStart = frameN;  // exact frame index
    B1_trial_cue_text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B1_trial_cue_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B1_trial_cue_text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of B1_TrialsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function B1_TrialsRoutineEnd() {
  //------Ending Routine 'B1_Trials'-------
  for (const thisComponent of B1_TrialsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // was no response the correct answer?!
  if (B1_resp.keys === undefined) {
    if (['None','none',undefined].includes(B1_correct)) {
       B1_resp.corr = 1  // correct non-response
    } else {
       B1_resp.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('B1_resp.keys', B1_resp.keys);
  psychoJS.experiment.addData('B1_resp.corr', B1_resp.corr);
  if (typeof B1_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('B1_resp.rt', B1_resp.rt);
      routineTimer.reset();
      }
  
  B1_resp.stop();
  return Scheduler.Event.NEXT;
}

var B2_InstrComponents;
function B2_InstrRoutineBegin() {
  //------Prepare to start Routine 'B2_Instr'-------
  t = 0;
  B2_InstrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  B2_instr_txt.setText(instr_txt);
  B2_instr_resp.keys = undefined;
  B2_instr_resp.rt = undefined;
  B2_cont_txt.setText(cont_txt);
  // keep track of which components have finished
  B2_InstrComponents = [];
  B2_InstrComponents.push(B2_instr_txt);
  B2_InstrComponents.push(B2_instr_resp);
  B2_InstrComponents.push(B2_cont_txt);
  
  for (const thisComponent of B2_InstrComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function B2_InstrRoutineEachFrame() {
  //------Loop for each frame of Routine 'B2_Instr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = B2_InstrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *B2_instr_txt* updates
  if (t >= 0.0 && B2_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B2_instr_txt.tStart = t;  // (not accounting for frame time here)
    B2_instr_txt.frameNStart = frameN;  // exact frame index
    B2_instr_txt.setAutoDraw(true);
  }

  
  // *B2_instr_resp* updates
  if (t >= 0.0 && B2_instr_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B2_instr_resp.tStart = t;  // (not accounting for frame time here)
    B2_instr_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { B2_instr_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { B2_instr_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { B2_instr_resp.clearEvents(); });
  }

  if (B2_instr_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = B2_instr_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *B2_cont_txt* updates
  if (t >= 0.0 && B2_cont_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B2_cont_txt.tStart = t;  // (not accounting for frame time here)
    B2_cont_txt.frameNStart = frameN;  // exact frame index
    B2_cont_txt.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of B2_InstrComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function B2_InstrRoutineEnd() {
  //------Ending Routine 'B2_Instr'-------
  for (const thisComponent of B2_InstrComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "B2_Instr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var B2_TrialsComponents;
function B2_TrialsRoutineBegin() {
  //------Prepare to start Routine 'B2_Trials'-------
  t = 0;
  B2_TrialsClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  B2_stim_text.setText(B2_stim);
  B2_resp.keys = undefined;
  B2_resp.rt = undefined;
  signal.secs=0.1;
  signal.setVolume(sig_volume);
  // keep track of which components have finished
  B2_TrialsComponents = [];
  B2_TrialsComponents.push(B2_stim_text);
  B2_TrialsComponents.push(B2_resp);
  B2_TrialsComponents.push(signal);
  B2_TrialsComponents.push(B2_trial_cue_text);
  
  for (const thisComponent of B2_TrialsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function B2_TrialsRoutineEachFrame() {
  //------Loop for each frame of Routine 'B2_Trials'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = B2_TrialsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *B2_stim_text* updates
  if (t >= 0 && B2_stim_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B2_stim_text.tStart = t;  // (not accounting for frame time here)
    B2_stim_text.frameNStart = frameN;  // exact frame index
    B2_stim_text.setAutoDraw(true);
  }

  frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B2_stim_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B2_stim_text.setAutoDraw(false);
  }
  
  // *B2_resp* updates
  if (t >= 0 && B2_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B2_resp.tStart = t;  // (not accounting for frame time here)
    B2_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { B2_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { B2_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { B2_resp.clearEvents(); });
  }

  frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B2_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B2_resp.status = PsychoJS.Status.FINISHED;
  }

  if (B2_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = B2_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      B2_resp.keys = theseKeys[0].name;  // just the last key pressed
      B2_resp.rt = theseKeys[0].rt;
      // was this 'correct'?
      if (B2_resp.keys === B2_correct) {
          B2_resp.corr = 1;
      } else {
          B2_resp.corr = 0;
      }
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // start/stop signal
  if (t >= 0 && signal.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    signal.tStart = t;  // (not accounting for frame time here)
    signal.frameNStart = frameN;  // exact frame index
    signal.play();  // start the sound (it finishes automatically)
    signal.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (signal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (0.1 > 0.5) {  signal.stop();  // stop the sound (if longer than duration)
      signal.status = PsychoJS.Status.FINISHED;
    }
  }
  
  // *B2_trial_cue_text* updates
  if (t >= 0.0 && B2_trial_cue_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B2_trial_cue_text.tStart = t;  // (not accounting for frame time here)
    B2_trial_cue_text.frameNStart = frameN;  // exact frame index
    B2_trial_cue_text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B2_trial_cue_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B2_trial_cue_text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of B2_TrialsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function B2_TrialsRoutineEnd() {
  //------Ending Routine 'B2_Trials'-------
  for (const thisComponent of B2_TrialsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // was no response the correct answer?!
  if (B2_resp.keys === undefined) {
    if (['None','none',undefined].includes(B2_correct)) {
       B2_resp.corr = 1  // correct non-response
    } else {
       B2_resp.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('B2_resp.keys', B2_resp.keys);
  psychoJS.experiment.addData('B2_resp.corr', B2_resp.corr);
  if (typeof B2_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('B2_resp.rt', B2_resp.rt);
      routineTimer.reset();
      }
  
  B2_resp.stop();
  signal.stop();  // ensure sound has stopped at end of routine
  return Scheduler.Event.NEXT;
}

var Thank_YouComponents;
function Thank_YouRoutineBegin() {
  //------Prepare to start Routine 'Thank_You'-------
  t = 0;
  Thank_YouClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  thanks_resp.keys = undefined;
  thanks_resp.rt = undefined;
  // keep track of which components have finished
  Thank_YouComponents = [];
  Thank_YouComponents.push(thanks_txt);
  Thank_YouComponents.push(thanks_resp);
  Thank_YouComponents.push(thanks_cont_text);
  
  for (const thisComponent of Thank_YouComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Thank_YouRoutineEachFrame() {
  //------Loop for each frame of Routine 'Thank_You'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Thank_YouClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *thanks_txt* updates
  if (t >= 0.0 && thanks_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    thanks_txt.tStart = t;  // (not accounting for frame time here)
    thanks_txt.frameNStart = frameN;  // exact frame index
    thanks_txt.setAutoDraw(true);
  }

  
  // *thanks_resp* updates
  if (t >= 0.0 && thanks_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    thanks_resp.tStart = t;  // (not accounting for frame time here)
    thanks_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { thanks_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { thanks_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { thanks_resp.clearEvents(); });
  }

  if (thanks_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = thanks_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *thanks_cont_text* updates
  if (t >= 0.0 && thanks_cont_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    thanks_cont_text.tStart = t;  // (not accounting for frame time here)
    thanks_cont_text.frameNStart = frameN;  // exact frame index
    thanks_cont_text.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of Thank_YouComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Thank_YouRoutineEnd() {
  //------Ending Routine 'Thank_You'-------
  for (const thisComponent of Thank_YouComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "Thank_You" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
