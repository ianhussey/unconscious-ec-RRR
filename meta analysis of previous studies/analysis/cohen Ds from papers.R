#computing Cohen d
library(powerAnalysis)

#Olson & Fazio 2001 - study 2, explicit 
ES.t.one(t = 1.92, n = 50)#0.27
#Olson & Fazio 2001 - study 2, IAT 
ES.t.one(t = 2.59, n = 50)#0.37
#Olson & Fazio 2002 
ES.t.one(t = 2.28, n = 51)#0.32
#Jones, Fazio, & Olson (2009) - study 1
ES.t.one(m = 0.64, sd = 4.5, n = 28, mu=0)#0.14
#Jones, Fazio, & Olson (2009) - study 2 - high
ES.t.one(t = 2.09, n = 53)#0.28
#Jones, Fazio, & Olson (2009) - study 2 - low
ES.t.one(t = -0.91, n = 54)#0.12
#Jones, Fazio, & Olson (2009) - study 3 - high
ES.t.one(t = 2.03, n = 57)#0.27
#Jones, Fazio, & Olson (2009) - study 4 - high
ES.t.one(t = 1.8, n = 50)#0.25
#Jones, Fazio, & Olson (2009) - study 5 - high
ES.t.one(t = 2.01, n = 59)#0.26
#Olson, Kendrick & Fazio (2009) - 1a - EC
ES.t.one(m = 0.30, sd = 1.07, n = 43, mu=0)#0.28
#Olson, Kendrick & Fazio (2009) - 1b - EC
ES.t.one(m = 0.40, sd = 1.07, n = 39, mu=0)#0.37
#Kendrick & Olson (2012) - study 1 - "intuative"
ES.t.one(t = 3.41, n = 28)#0.65
#Kendrick & Olson (2012) - study 2 - "expert"
ES.t.one(t = 2.92, n = 69)#0.35
#Bar-Anan et al (2010) study 1
ES.t.one(t = 1.83, n = 413)#0.09
#Bar-Anan et al (2010) study 2
ES.t.one(t = 1, n = 487)#0.04
#Luethi, Meier, & Sandi (2009) - control participants
ES.t.one(t = -1.3, n = 12)#-0.39
ES.t.one(m = -0.75, sd = 2, n = 12, mu=0)#0.37
#Luethi, Meier, & Sandi (2009) - stressed participants
ES.t.one(t = 2.17, n = 13)#0.62
ES.t.one(m = 1.15, sd = 1.9, n = 13, mu=0)#0.60
#Stahl & Heycke (2016)
ES.t.one(t = 5.03, n = 58)#0.66


library(BayesFactor)



