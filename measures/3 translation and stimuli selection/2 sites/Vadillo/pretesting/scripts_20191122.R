# clear workspace and load libraries
rm(list = ls())
require(BayesFactor)

# read and format dataframe
data <- read.csv2("Results.csv", sep=",", header = FALSE)
data <- data.frame(data)
colnames(data) <- c("subj", "item", "eval", "familiar")

# summary of results of each pokemon...
results <- data.frame(item = 1:20,
                      name = c("Bergmite", "Carbink", "Cosmog", "Cranidos", "Frillish",
                               "Golett", "Gourgeist", "Grubbin", "Jangmo", "Kricketot",
                               "Magearna", "Palpitoad", "Phantump", "Scatterbug", "Scraggy",
                               "Shelmet", "Sliggoo", "Swadloon", "Wimpod", "Zorua"),
                      m.eval      = tapply(data$eval, data$item, mean),
                      sd.eval     = tapply(data$eval, data$item, sd),
                      m.familiar  = tapply(data$familiar, data$item, mean),
                      sd.familiar = tapply(data$familiar, data$item, sd))

# t-statistic comparing evaluation ratings and 0 for each pokemon...
results$t.eval <- results$m.eval / (results$sd.eval / sqrt(max(data$subj)))

# effect size (mean evaluation / standard deviation)...
results$d.eval <- results$m.eval / results$sd.eval

# add two-sided Bayes Factors (BF01) for evaluation ratings...
results$bf.01 <- 1 / mapply(ttest.tstat, t=results$t.eval, n1=max(data$subj), simple=TRUE)

# sort rows according to BF01...
results <- results[order(results$bf.01),]

# t-statistic (and p-value) comparing familiarity ratings to 4...
results$t.familiar <- (4 - results$m.familiar) / (results$sd.familiar / sqrt(max(data$subj)))
results$p.familiar <- 2*pt(-abs(results$t.familiar),df=max(data$subj)-1)

# see all results to select the two most neutral stimuli...
results
# based on the data in "results", we selected the two stimuli at the end:
# Scatterbug (item=14) and Gourgeist (item=7)
# because they have the highest BF01 in favour of the null hypothesis for
# evaluation ratings and their familiarity ratings are among the lowest

# check that evaluation ratings do not differ for items 7 and 14
# the t-test is non-significan, p = .79
t.eval <- t.test(x=data$eval[data$item==7],
                 y=data$eval[data$item==14],
                 paired=TRUE)

# check that familiarity ratings do not differ for items 7 and 14...
# the t-test is non-significnat, p = .65
t.familiar <- t.test(x=data$familiar[data$item==7],
                     y=data$familiar[data$item==14],
                    paired=TRUE)

# BFs comparing items 7 and 14 favour the null hypothesis
# for both evaluation and familiarity...
ttest.tstat(t=t.eval$statistic, n1=max(data$subj), simple=TRUE)
ttest.tstat(t=t.familiar$statistic, n1=max(data$subj), simple=TRUE)

# see results again to select fillers...
results
# we select as fillers the valid items that are immediately above
# Scatterburg and Gourgeist in the results data frame:
# Shelmet (16), Phantump (13), Bergmite (1), Golett (6), Magearna (11), Palpitoad (12), Sliggoo (17)
# Grubbin is excluded following the instructions by Tal
# Cranidos is excluded because familiarity is not significantly lower than 4 (p = .286)