# Instructions for scoring the open-ended responses

## Development notes from Ian to Tal

- Im not sure how to get the sites to score the multiple criteria invovled in confirmatory analysis 1 and exporatory analysis 1's exclusion criteria (e.g., multiple criteria and multiple stimuli, as well as references to agreement between the raters). Who will calculate and integrate each step, etc. This needs documenting. We could capture each subclause (ie the X or Y or Z criteria) for replicability and then process them into a global variable (this would be more replicable), or get them to score the compound critiera themselves. 
- Each site will also need to know which pokemon were used as the CS1 and CS2 in each condition at their site to know if the correct stimuli were used. How to ensure the raters know this correctly? the condition variable is now printed to the csv files at least.
- In either case, there is some admin work to be done in making site specific excel files from the master file that the processing scripts produce, ensuring there are two separate files to be given to the two different reviewers so that they are blinded to one anothers responses, sending them to the sites, then integrating results into a single file for futher processing using the second R script. Tal, will you look after this?

## Awareness questions

Two awareness criteria must be scored from participants' open ended responses across two questions:

1. "Think back to the very first part of the experiment. Did you notice anything out of the ordinary in the way the words and pictures were presented during the surveillance tasks?"
2. "Did you notice anything systematic about how particular words and images appeared together during the surveillance tasks?"

The attached .csv file contains each participant's responses to the two relevant questions. We therefore ask you to have two researchers at your site hand-score responses to these questions using the following criteria. The two researchers should be blinded to one anothers responses - have them fill in two separate copies of the file and then integrate these responses into one file to return to us. 

## Exclusion criteria

Taken from manuscript.

### Confirmatory analysis 1

"As recommended by the original authors, participants will be excluded if both raters agree that participants identified the valence of the USs that were paired with each of the CSs, in at least one of the two questions. If participants identify that one of the CSs was paired with a US of a particular valence, or report that CSs and US were paired during the task (even if they do not mention the specific way in which they were paired), then they will be retained and coded as being ‘contingency unaware’. Likewise, in cases of rater disagreement, participants will also be retained and coded as ‘contingency unaware’ as per the original authors criteria."

### Exploratory analysis 1

The first (exploratory) score will use a more conservative coding of the original authors’ questions. Participants will be coded as ‘aware’ if they express full or partial memory. Specifically, assignment to the ‘aware’ group will occur when both judges agree that the participant identified the valence of the USs that were paired with each of the CSs, or identified that one of the CSs was paired with a US of a particular valence, or reports that CSs and USs were paired during the task (even if they do not mention the specific way in which they were paired), in at least one of the two questions. Assignment to the ‘unaware’ group will occur when both judges indicate that the participant did not report that CSs were systematically paired with USs, or that a CS was paired with a US of a specific valance, in at least one of the two questions. In cases of rater disagreement, a third judge will be recruited and asked to provide their own judgement according to the above criteria. The majority judgement will be adopted. Participants in the ‘aware’ group will be excluded from subsequent analysis.

### Exploratory analysis 2

 The second (exploratory) score will be computed based on Bar-Anan et al.’s (2010) criteria. Here participants will be excluded if they chose the “yes” answer on question 1 of the Bar-Anan et al. measure, and retained if they chose “no”. 

### Exploratory analysis 3

Participants will be excluded if they chose the “yes” answer on question 1 and correctly identify the valence with which each of the two CSs appeared during the task (providing either a *probably* or *certainly* response on questions 2-3). 

## Scoring procedure

1.  Ascertain which pokemon was paired with positive stimuli (CS-pos) and which was paired with negative stimuli (CS-neg) at your site and for this participant (depending on condition).
2. Inspect their written responses across both questions. If the participant identifies that the CS-pos stimulus was paired (e.g., paired, associated, occured alongside with, etc) positive stimuli AND the CS-neg stimulus was paired with negative stimuli, score this participant as TRUE. If they only report one CS stimulus pairing, or report both but fail to note with which valenced stimuli each was specifically paired, or do not report either CS being paired with a valenced stimulus, score them as FALSE. 
3. XXX NEEDS FLESHING OUT - TAL CAN YOU ADD THIS? 



