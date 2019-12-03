# Title: CS selection 
# Team: Université catholique de Louvain

rm(list=ls()) # clear out the environment

if (!require("pacman")) install.packages("pacman")
p_load(data.table, BayesFactor,
       install = TRUE, update = getOption("pac_update"), character.only = FALSE) # Install, update and load packages if necessary

css = read.csv("css.csv", header = TRUE, sep = ";") # import raw data
css[,2:41] <- sapply(css[,2:41],as.numeric) # set DVs as numeric

average <- function(x){
        return(mean(x, na.rm = TRUE))
} # create function to extract mean

BF <- function(x){
        y = ttestBF(x[!is.na(x)])
        return(extractBF(y)$bf)
} # create function to extract BF01

df <- data.table(cs = sapply(strsplit(colnames(css[,2:41]), "_"), "[", 1),
                 dimension = sapply(strsplit(colnames(css[,2:41]), "_"), "[", 2),
                 average = sapply(css[,2:41], average),
                 bf = sapply(css[,2:41], BF)) # create data.table with means and BF01 for each CS and both dimensions
df[dimension %in% c("familiari","familiarit"), dimension := "familiarity"] # correct typos
df[cs %in% "begmite", cs := "bergmite"] # correct typos

## Selection step1: Based on effect size and Bayes-Factor analyses on the above ratings, select the 9 characters that are rated closest to 0 (neutral) on the liking scale.

df[, abs_average := abs(average), 1:nrow(df)] # absolute value of values 
df[,rank_mean:=rank(abs_average,ties.method="first"),by=dimension] # rank average values
df[,rank_bf:=rank(bf,ties.method="first"),by=dimension] # rank BF01 values
df[,rank_tot := rank_mean + rank_bf] # combine rank of means and BF01s
df[,rank_unique:=rank(rank_tot,ties.method="first"),by=dimension] # unique rank by stimulus and dimension
df[dimension %in% "liking" & rank_unique < 10, step1 := "1"] # Step 1 selection: select the 9 less valent CSs
df <- data.table(full_join(df[,-10], df[dimension %in% "liking" & step1  %in% "1", cs, step1])) # Step 1 selection 

## Selection step2: Then, make sure that they are not rated as somewhat familiar (i.e., that they rated significantly below 4 on the familiarity scale). 

pval <- function(x){
        return(t.test(x, mu = 4)$p.value)
} # function to extract p-value from ttest against 4
df$p <- sapply(css[,2:41], pval) # apply function to all CSs
df[dimension %in% "familiarity" & step1 %in% "1", p] < .05 & df[dimension %in% "familiarity" & step1 %in% "1", average] < 4 # Step 2 check: OK

## Selection step3: Thereafter, please identify, which two of the nine characters are most neutral and least familiar. 

df[cs %in% c("wimpod", "grubbin"), step1 := "NA"] # exclude wimpod and grubbin
s3 <- dcast(df[,c("cs","dimension","rank_unique")], cs ~ dimension, value.var="rank_unique") # select only relevant columns
s3[, rank_familiarity := 21 - familiarity] # compute a rank of familiarity with higher value meaning higher familiarity
s3[, rank_tot := liking + rank_familiarity] # create a combined index of liking and familiarity with higher value meaning more valenced and more familiar
s3[rank_tot %in% sort(s3[,rank_tot])[1:2], step3 := "1"] # select the two CSs the less valenced and less familiar

## Step4: Finally, verify with t-test and Bayes-Factor analysis that the liking scores and familiarity scores of the two selected CSs do not differ from one another. 

s4_liking <- data.table(css$gourgeist_liking_1,css$zorua_liking_1) # select liking data for the selected CSs
s4_liking <- s4_liking[complete.cases(s4_liking)] # remove NAs

t.test(s4_liking$V1, s4_liking$V2, paired = TRUE) # Non-significant
ttestBF(s4_liking$V1, s4_liking$V2, paired = TRUE) # BF01 ~ 3

s4_familiarity <- data.table(css$gourgeist_familiarit_1,css$zorua_familiarity_1) # select familiarity data for the selected CSs
s4_familiarity <- s4_familiarity[complete.cases(s4_familiarity)] # remove NAs

t.test(s4_familiarity$V1, s4_familiarity$V2, paired = TRUE) # Significant
ttestBF(s4_familiarity$V1, s4_familiarity$V2, paired = TRUE) # BF10 ~ 8

## Step5: re-selection of the next two less valent and less familiar CSs: jangmo & frillish

s5_liking <- data.table(css$jangmo_liking_1,css$frillish_liking_1) # select liking data for the selected CSs
s5_liking <- s5_liking[complete.cases(s5_liking)] # remove NAs

t.test(s5_liking$V1, s5_liking$V2, paired = TRUE) # Non-significant
ttestBF(s5_liking$V1, s5_liking$V2, paired = TRUE) # BF01 ~ 6

s5_familiarity <- data.table(css$jangmo_familiarity_1,css$frillish_familiarity_1) # select familiarity data for the selected CSs
s5_familiarity <- s5_familiarity[complete.cases(s5_familiarity)] # remove NAs

t.test(s5_familiarity$V1, s5_familiarity$V2, paired = TRUE) # Non-significant
ttestBF(s5_familiarity$V1, s5_familiarity$V2, paired = TRUE) # BF01 ~ 3

## The selected CSs are: Jangmo and Frillish
