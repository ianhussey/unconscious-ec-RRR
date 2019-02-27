# Unconscious EC RRR

## Usage instructions

### Software & dependencies

1. Download and install PsychoPy version 3.0.4 on all computes that will be used for data collection.
   1. https://github.com/psychopy/psychopy/releases/tag/3.0.4
   2. In order to prevents research assistants from making accidential changes to the experiment script when collecting data, set the coder to read only on computers that will be used for data collection.
      1.  Inside psychopy, click file>open>experiment.py
      2. Click settings - ie the icon with the wrench and screwdriver across one another.
      3. Click the "coder" tab.
      4. Check the box next to "read-only". 
2. Download and install R on at least one computer
   1. https://cran.r-project.org/mirrors.html
3. Download and install RStudio at least one computer
   1. https://www.rstudio.com/products/rstudio/download/#download
   2. NB All libraries needed by the study's R scripts will self install when the script is run. 

### Localisation

#### Text

In order to change all text used within the experiment to your local language, translate the text in the files `filler_1.xlsx`, `filler_2.xlsx`, `instructions.xlsx`, `instructions_evaluation.xlsx`, and `instructions_surveillance.xlsx`. The PsychoPy script will pull text from these files to be used in the study. Ensure you preserve line breaks etc used in the files so that they are presented correctly on screen. Cells that you should not alter are protected to prevent accidential changes.

#### Stimuli

Stimuli should be pre-rated in a seperate sample from the population you will collect data from. The least familiar and most neutral stimuli should be selected for inclusion in the study. If it isn't possible to pre-rate stimuli, we have provided stimuli that we have pre-rated using an online sample. You should already have discussed this step with Tal when you agreed with her to collect data for this study - if not, please touch base with her. If your data from pre-ratings suggests that different stimuli should be used to those employed here, please contact Tal for advice on how to make these changes in a way that conforms to the precise requests of the original authors.  

### Data collection

1. Open `trials_generator.Rmd` in RStudio. Click the "knit" button to run this script and create a report. This will create a "trials" folder and fill it with files. These are used to determine the randomised order of presentation of the trials within the experiment. Enough for 150 participants are produced, on the basis that the planned max N per site is 150. 
   1. NB this needs to be done only once for each site. The files in the trials folder only need to be generated once to have all you need for the 150 participants. 
2. For each experimental session, open `experiment.py` in PsychoPy. 
3. Click the green button to run the study.
4. Enter sequential participant number, age, and gender in the pop up box, and click the button to start. Counterbalancing between the two conditions (CS1-USpositive and CS1-USnegative) is done randomly within the task, between participants. All other counterbalancing (e.g., of trial-order/stimulus exemplars within blocks) was done ahead of time using the R script. 

## To do

- What counterbalancing options are needed other than CS1-pos vs CS2-pos?





