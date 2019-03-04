# Unconscious EC RRR

## Software requirements

1. Download and install PsychoPy version 3.0 on all computes that will be used for data collection.
   - https://github.com/psychopy/psychopy/releases/
2. If you would like to prevents your research assistants from being able to make accidential changes to the experiment's python script while they are collecting data, set the coder to "read only" on computers that will be used for data collection. This can be done as follows:
   1.  Inside psychopy, click file>open>experiment.py
   2. Click settings - ie the icon with the wrench and screwdriver across one another.
   3. Click the "coder" tab.
   4. Check the box next to "read-only".
3. You can contact Ian (ian.hussey@ugent.be) if you have issues with the experiment materials specially. However, I won't be able to take questions about issues with psychopy more generally (eg its installation or running). For these, please contact your department's technical staff or the psychopy forums.

## Materials

You have been sent a copy of the measures that:

1. Uses your localised stimuli and instructions files
2. Contains a unique set of randomised trials files (that is, randomisation of the trials is done ahead of time rather than for each participant at runtime), and
3. Contains customised data collection site file (which encodes information about the data collection site into the data files). 

## Data collection

1. For each experimental session, open `experiment.py` inside PsychoPy.
2. Click the green button to run the study.
3. Enter sequential participant number, age, and gender in the pop up box, and click the button to start. 
   - NB that duplicate participants will likely require both duplicates to be excluded from the analysis, so please ensure that participant code assignment is correct.

## Data processing and analysis

**[add note on the BF optional stopping design here, and how researchers at each site should process and analyse their data using the bundled scripts (to be created) in order to determine when they stop collecting data].**

## Return files

Once you have done the above, please return both all the `csv` files produced by the task to Ian for (ian.hussey@ugent.be) centralised analysis.