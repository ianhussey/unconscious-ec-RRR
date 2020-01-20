rm(list = ls())

# install.packages("BayesFactor")

library(plyr)

######Read Data#######

setwd("./")
data_file = "data_pretest_Tuebingen.csv"

data = read.table(
  file=data_file, encoding="UTF-8",
  header = FALSE, sep = "\t", quote = "\"",
  dec = ".", row.names = "CASE",
  col.names = c(
    "CASE","SERIAL","REF","QUESTNNR","MODE","STARTED","VP01_01","PR01_01","PR02_01",
    "PR03_01","PR04_01","PR05_01","PR06_01","PR07_01","PR08_01","PR09_01","PR10_01",
    "PR11_01","PR12_01","PR13_01","PR14_01","PR15_01","PR16_01","PR17_01","PR18_01",
    "PR19_01","PR20_01","FR01_01","FR02_01","FR03_01","FR04_01","FR05_01","FR06_01",
    "FR07_01","FR08_01","FR09_01","FR10_01","FR11_01","FR12_01","FR13_01","FR14_01",
    "FR15_01","FR16_01","FR17_01","FR18_01","FR19_01","FR20_01","SD01_01","SD02",
    "SV01_01","SV01_02","SV01_03","TIME001","TIME002","TIME003","TIME004","TIME005",
    "TIME_SUM","MAILSENT","LASTDATA","FINISHED","Q_VIEWER","LASTPAGE","MAXPAGE",
    "MISSING","MISSREL","TIME_RSI","DEG_TIME"
  ),
  as.is = TRUE,
  colClasses = c(
    CASE="numeric", SERIAL="character", REF="character", QUESTNNR="character",
    MODE="character", STARTED="POSIXct", VP01_01="character", PR01_01="numeric",
    PR02_01="numeric", PR03_01="numeric", PR04_01="numeric", PR05_01="numeric",
    PR06_01="numeric", PR07_01="numeric", PR08_01="numeric", PR09_01="numeric",
    PR10_01="numeric", PR11_01="numeric", PR12_01="numeric", PR13_01="numeric",
    PR14_01="numeric", PR15_01="numeric", PR16_01="numeric", PR17_01="numeric",
    PR18_01="numeric", PR19_01="numeric", PR20_01="numeric", FR01_01="numeric",
    FR02_01="numeric", FR03_01="numeric", FR04_01="numeric", FR05_01="numeric",
    FR06_01="numeric", FR07_01="numeric", FR08_01="numeric", FR09_01="numeric",
    FR10_01="numeric", FR11_01="numeric", FR12_01="numeric", FR13_01="numeric",
    FR14_01="numeric", FR15_01="numeric", FR16_01="numeric", FR17_01="numeric",
    FR18_01="numeric", FR19_01="numeric", FR20_01="numeric", SD01_01="numeric",
    SD02="numeric", SV01_01="character", SV01_02="character",
    SV01_03="character", TIME001="integer", TIME002="integer",
    TIME003="integer", TIME004="integer", TIME005="integer", TIME_SUM="integer",
    MAILSENT="POSIXct", LASTDATA="POSIXct", FINISHED="logical",
    Q_VIEWER="logical", LASTPAGE="numeric", MAXPAGE="numeric",
    MISSING="numeric", MISSREL="numeric", TIME_RSI="numeric", DEG_TIME="numeric"
  ),
  skip = 1,
  check.names = TRUE, fill = TRUE,
  strip.white = FALSE, blank.lines.skip = TRUE,
  comment.char = "",
  na.strings = ""
)

rm(data_file)

attr(data, "project") = "RRR_surv_pre"
attr(data, "description") = "RRR_surv_Pretest"
attr(data, "date") = "2019-10-24 10:56:10"
attr(data, "server") = "https://www.soscisurvey.de"

# Variable und Value Labels
data$SD02 = factor(data$SD02, levels=c("1","2","3","-9"), labels=c("weiblich","männlich","divers","[NA] nicht beantwortet"), ordered=FALSE)
attr(data$PR01_01,"1") = "sehr negativ"
attr(data$PR01_01,"5") = "neutral"
attr(data$PR01_01,"9") = "sehr positiv"
attr(data$PR02_01,"1") = "sehr negativ"
attr(data$PR02_01,"5") = "neutral"
attr(data$PR02_01,"9") = "sehr positiv"
attr(data$PR03_01,"1") = "sehr negativ"
attr(data$PR03_01,"5") = "neutral"
attr(data$PR03_01,"9") = "sehr positiv"
attr(data$PR04_01,"1") = "sehr negativ"
attr(data$PR04_01,"5") = "neutral"
attr(data$PR04_01,"9") = "sehr positiv"
attr(data$PR05_01,"1") = "sehr negativ"
attr(data$PR05_01,"5") = "neutral"
attr(data$PR05_01,"9") = "sehr positiv"
attr(data$PR06_01,"1") = "sehr negativ"
attr(data$PR06_01,"5") = "neutral"
attr(data$PR06_01,"9") = "sehr positiv"
attr(data$PR07_01,"1") = "sehr negativ"
attr(data$PR07_01,"5") = "neutral"
attr(data$PR07_01,"9") = "sehr positiv"
attr(data$PR08_01,"1") = "sehr negativ"
attr(data$PR08_01,"5") = "neutral"
attr(data$PR08_01,"9") = "sehr positiv"
attr(data$PR09_01,"1") = "sehr negativ"
attr(data$PR09_01,"5") = "neutral"
attr(data$PR09_01,"9") = "sehr positiv"
attr(data$PR10_01,"1") = "sehr negativ"
attr(data$PR10_01,"5") = "neutral"
attr(data$PR10_01,"9") = "sehr positiv"
attr(data$PR11_01,"1") = "sehr negativ"
attr(data$PR11_01,"5") = "neutral"
attr(data$PR11_01,"9") = "sehr positiv"
attr(data$PR12_01,"1") = "sehr negativ"
attr(data$PR12_01,"5") = "neutral"
attr(data$PR12_01,"9") = "sehr positiv"
attr(data$PR13_01,"1") = "sehr negativ"
attr(data$PR13_01,"5") = "neutral"
attr(data$PR13_01,"9") = "sehr positiv"
attr(data$PR14_01,"1") = "sehr negativ"
attr(data$PR14_01,"5") = "neutral"
attr(data$PR14_01,"9") = "sehr positiv"
attr(data$PR15_01,"1") = "sehr negativ"
attr(data$PR15_01,"5") = "neutral"
attr(data$PR15_01,"9") = "sehr positiv"
attr(data$PR16_01,"1") = "sehr negativ"
attr(data$PR16_01,"5") = "neutral"
attr(data$PR16_01,"9") = "sehr positiv"
attr(data$PR17_01,"1") = "sehr negativ"
attr(data$PR17_01,"5") = "neutral"
attr(data$PR17_01,"9") = "sehr positiv"
attr(data$PR18_01,"1") = "sehr negativ"
attr(data$PR18_01,"5") = "neutral"
attr(data$PR18_01,"9") = "sehr positiv"
attr(data$PR19_01,"1") = "sehr negativ"
attr(data$PR19_01,"5") = "neutral"
attr(data$PR19_01,"9") = "sehr positiv"
attr(data$PR20_01,"1") = "sehr negativ"
attr(data$PR20_01,"5") = "neutral"
attr(data$PR20_01,"9") = "sehr positiv"
attr(data$FR01_01,"1") = "gar nicht vertraut"
attr(data$FR01_01,"8") = "sehr vertraut"
attr(data$FR02_01,"1") = "gar nicht vertraut"
attr(data$FR02_01,"8") = "sehr vertraut"
attr(data$FR03_01,"1") = "gar nicht vertraut"
attr(data$FR03_01,"8") = "sehr vertraut"
attr(data$FR04_01,"1") = "gar nicht vertraut"
attr(data$FR04_01,"8") = "sehr vertraut"
attr(data$FR05_01,"1") = "gar nicht vertraut"
attr(data$FR05_01,"8") = "sehr vertraut"
attr(data$FR06_01,"1") = "gar nicht vertraut"
attr(data$FR06_01,"8") = "sehr vertraut"
attr(data$FR07_01,"1") = "gar nicht vertraut"
attr(data$FR07_01,"8") = "sehr vertraut"
attr(data$FR08_01,"1") = "gar nicht vertraut"
attr(data$FR08_01,"8") = "sehr vertraut"
attr(data$FR09_01,"1") = "gar nicht vertraut"
attr(data$FR09_01,"8") = "sehr vertraut"
attr(data$FR10_01,"1") = "gar nicht vertraut"
attr(data$FR10_01,"8") = "sehr vertraut"
attr(data$FR11_01,"1") = "gar nicht vertraut"
attr(data$FR11_01,"8") = "sehr vertraut"
attr(data$FR12_01,"1") = "gar nicht vertraut"
attr(data$FR12_01,"8") = "sehr vertraut"
attr(data$FR13_01,"1") = "gar nicht vertraut"
attr(data$FR13_01,"8") = "sehr vertraut"
attr(data$FR14_01,"1") = "gar nicht vertraut"
attr(data$FR14_01,"8") = "sehr vertraut"
attr(data$FR15_01,"1") = "gar nicht vertraut"
attr(data$FR15_01,"8") = "sehr vertraut"
attr(data$FR16_01,"1") = "gar nicht vertraut"
attr(data$FR16_01,"8") = "sehr vertraut"
attr(data$FR17_01,"1") = "gar nicht vertraut"
attr(data$FR17_01,"8") = "sehr vertraut"
attr(data$FR18_01,"1") = "gar nicht vertraut"
attr(data$FR18_01,"8") = "sehr vertraut"
attr(data$FR19_01,"1") = "gar nicht vertraut"
attr(data$FR19_01,"8") = "sehr vertraut"
attr(data$FR20_01,"1") = "gar nicht vertraut"
attr(data$FR20_01,"8") = "sehr vertraut"
attr(data$FINISHED,"F") = "abgebrochen"
attr(data$FINISHED,"T") = "ausgefüllt"
attr(data$Q_VIEWER,"F") = "Teilnehmer"
attr(data$Q_VIEWER,"T") = "Durchklicker"
comment(data$SERIAL) = "Seriennummer (sofern verwendet)"
comment(data$REF) = "Referenz (sofern im Link angegeben)"
comment(data$QUESTNNR) = "Fragebogen, der im Interview verwendet wurde"
comment(data$MODE) = "Interview-Modus"
comment(data$STARTED) = "Zeitpunkt zu dem das Interview begonnen hat (Europe/Berlin)"
comment(data$VP01_01) = "VPNr: VPNr"
comment(data$PR01_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR02_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR03_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR04_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR05_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR06_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR07_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR08_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR09_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR10_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR11_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR12_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR13_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR14_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR15_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR16_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR17_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR18_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR19_01) = "PR: [Keine Beschreibung] 01"
comment(data$PR20_01) = "PR: [Keine Beschreibung] 01"
comment(data$FR01_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR02_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR03_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR04_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR05_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR06_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR07_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR08_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR09_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR10_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR11_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR12_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR13_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR14_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR15_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR16_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR17_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR18_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR19_01) = "FR: [Keine Beschreibung] 01"
comment(data$FR20_01) = "FR: [Keine Beschreibung] 01"
comment(data$SD01_01) = "Alter (direkt): Ich bin   ... Jahre alt."
comment(data$SD02) = "Geschlecht"
comment(data$SV01_01) = "Save: $Images"
comment(data$SV01_02) = "Save: $PleasureRating"
comment(data$SV01_03) = "Save: $FamiliarityRating"
comment(data$TIME001) = "Verweildauer Seite 1"
comment(data$TIME002) = "Verweildauer Seite 2"
comment(data$TIME003) = "Verweildauer Seite 3"
comment(data$TIME004) = "Verweildauer Seite 4"
comment(data$TIME005) = "Verweildauer Seite 5"
comment(data$TIME_SUM) = "Verweildauer gesamt (ohne Ausreißer)"
comment(data$MAILSENT) = "Versandzeitpunkt der Einladungsmail (nur für nicht-anonyme Adressaten)"
comment(data$LASTDATA) = "Zeitpunkt als der Datensatz das letzte mal geändert wurde"
comment(data$FINISHED) = "Wurde die Befragung abgeschlossen (letzte Seite erreicht)?"
comment(data$Q_VIEWER) = "Hat der Teilnehmer den Fragebogen nur angesehen, ohne die Pflichtfragen zu beantworten?"
comment(data$LASTPAGE) = "Seite, die der Teilnehmer zuletzt bearbeitet hat"
comment(data$MAXPAGE) = "Letzte Seite, die im Fragebogen bearbeitet wurde"
comment(data$MISSING) = "Anteil fehlender Antworten in Prozent"
comment(data$MISSREL) = "Anteil fehlender Antworten (gewichtet nach Relevanz)"
comment(data$TIME_RSI) = "Maluspunkte für schnelles Ausfüllen"
comment(data$DEG_TIME) = "Maluspunkte für schnelles Ausfüllen"



# Assure that the comments are retained in subsets
as.data.frame.avector = as.data.frame.vector
`[.avector` <- function(x,i,...) {
  r <- NextMethod("[")
  mostattributes(r) <- attributes(x)
  r
}
data_tmp = data.frame(
  lapply(data, function(x) {
    structure( x, class = c("avector", class(x) ) )
  } )
)
mostattributes(data_tmp) = attributes(data)
data = data_tmp
rm(data_tmp)


#####RESHAPE######

data$VP01_01 <- as.numeric(data$VP01_01)


# Split lists

VPN <- length(data$VP01_01)
VPNr <- 0
Age <- 0
Alter <- 0
Sex <- 0
Geschlecht <- 0
SplitedPicNames <- 0
PicNames <- 0
SplitedPRating <- 0
PRating <- 0
SplitedFRating <- 0
FRating <- 0


for(i in seq(VPN)){

  VPNr[i] <- list(rep(data[i,]$VP01_01,20))
  VPNrFrame <- unlist(VPNr, use.names=F)

  Age[i] <- list(rep(data[i,]$SD01_01,20))
  Alter <- unlist(Age, use.names=F)

  Sex[i] <- list(rep(data[i,]$SD02,20))
  Geschlecht <- unlist(Sex, use.names=F)

  SplitedPicNames[i] <- strsplit(data[i,]$SV01_01, ",", fixed = TRUE)
  PicNames <- unlist(SplitedPicNames, use.names=T)

  SplitedPRating[i] <- strsplit(data[i,]$SV01_02, ",", fixed = TRUE)
  PRating <- unlist(SplitedPRating, use.names=T)

  SplitedFRating[i] <- strsplit(data[i,]$SV01_03, ",", fixed = TRUE)
  FRating <- unlist(SplitedFRating, use.names=T)
}


PRating <- as.factor(PRating)

Frame <- data.frame(cbind(VPNrFrame, Alter, Geschlecht, PicNames, PRating, FRating))

levels(Frame$PRating) <-  c("1" = "-4", "2" = "-3", "3" = "-2", "4" = "-1", "5" = "0", "6" = "1", "7" = "2", "8" = "3", "9" = "4")
levels(Frame$FRating) <-  c("1" = "0", "2" = "1", "3" = "2", "4" = "3", "5" = "4", "6" = "5", "7" = "6", "8" = "7")

Frame$PRating <- as.numeric(as.character(Frame$PRating))
Frame$FRating <- as.numeric(as.character(Frame$FRating))

Reshaped <- reshape(Frame, idvar = "VPNrFrame", timevar = "PicNames", direction = "wide")

Reshaped.data <- Reshaped[,-c(6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59,62,63,66,67,70,71,74,75,78,79)]

# Datensatz Zahlenart ver�ndern

PRating <- aggregate(PRating ~ PicNames,Frame,"mean")
PRatingSD <- aggregate(PRating ~ PicNames,Frame,"sd")
FRating <- aggregate(FRating ~ PicNames,Frame,"mean")
FRatingSD <- aggregate(FRating ~ PicNames,Frame,"sd")

Rating <- cbind(PRating, PRatingSD$PRating, FRating$FRating, FRatingSD$FRating)

colnames(Rating) <- c("PicName", "Pleasure", "PleasureSD", "Familiarity", "FamiliaritySD")


# Data.Frames: Frame (enth�lt die Rohdaten) und Rating (aggregierte Mittelwerte und SD f�r die 20 Bilder)
summary(Frame)
summary(Rating)

#####ANALYSES######

# BayesFactors
library("BayesFactor")

#Pleasure
BFP01 <- ttestBF(Reshaped.data$PRating.P01)
BFP01 <- as.data.frame(BFP01)
BFP02 <- ttestBF(Reshaped.data$PRating.P02)
BFP02 <- as.data.frame(BFP02)
BFP03 <- ttestBF(Reshaped.data$PRating.P03)
BFP03 <- as.data.frame(BFP03)
BFP04 <- ttestBF(Reshaped.data$PRating.P04)
BFP04 <- as.data.frame(BFP04)
BFP05 <- ttestBF(Reshaped.data$PRating.P05)
BFP05 <- as.data.frame(BFP05)
BFP06 <- ttestBF(Reshaped.data$PRating.P06)
BFP06 <- as.data.frame(BFP06)
BFP07 <- ttestBF(Reshaped.data$PRating.P07)
BFP07 <- as.data.frame(BFP07)
BFP08 <- ttestBF(Reshaped.data$PRating.P08)
BFP08 <- as.data.frame(BFP08)
BFP09 <- ttestBF(Reshaped.data$PRating.P09)
BFP09 <- as.data.frame(BFP09)
BFP10 <- ttestBF(Reshaped.data$PRating.P10)
BFP10 <- as.data.frame(BFP10)
BFP11 <- ttestBF(Reshaped.data$PRating.P11)
BFP11 <- as.data.frame(BFP11)
BFP12 <- ttestBF(Reshaped.data$PRating.P12)
BFP12 <- as.data.frame(BFP12)
BFP13 <- ttestBF(Reshaped.data$PRating.P13)
BFP13 <- as.data.frame(BFP13)
BFP14 <- ttestBF(Reshaped.data$PRating.P14)
BFP14 <- as.data.frame(BFP14)
BFP15 <- ttestBF(Reshaped.data$PRating.P15)
BFP15 <- as.data.frame(BFP15)
BFP16 <- ttestBF(Reshaped.data$PRating.P16)
BFP16 <- as.data.frame(BFP16)
BFP17 <- ttestBF(Reshaped.data$PRating.P17)
BFP17 <- as.data.frame(BFP17)
BFP18 <- ttestBF(Reshaped.data$PRating.P18)
BFP18 <- as.data.frame(BFP18)
BFP19 <- ttestBF(Reshaped.data$PRating.P19)
BFP19 <- as.data.frame(BFP19)
BFP20 <- ttestBF(Reshaped.data$PRating.P20)
BFP20 <- as.data.frame(BFP20)

BFP <- cbind(c(BFP01$bf, BFP02$bf, BFP03$bf, BFP04$bf, BFP05$bf, BFP06$bf, BFP07$bf, BFP08$bf, BFP09$bf, BFP10$bf, BFP11$bf, BFP12$bf, BFP13$bf, 
               BFP14$bf, BFP15$bf, BFP16$bf, BFP17$bf, BFP18$bf, BFP19$bf, BFP20$bf))


Rating.neu <- cbind(Rating, BFP)

#most neutral: 18, 20, 07, 15, 05, 09, 06, 16, 02

#Familiarity < 4?
#T-Tests
t.test(Reshaped.data$FRating.P18, mu = 4)
t.test(Reshaped.data$FRating.P20, mu = 4)
t.test(Reshaped.data$FRating.P07, mu = 4)
t.test(Reshaped.data$FRating.P15, mu = 4)
t.test(Reshaped.data$FRating.P05, mu = 4)
t.test(Reshaped.data$FRating.P09, mu = 4)
t.test(Reshaped.data$FRating.P06, mu = 4)
t.test(Reshaped.data$FRating.P16, mu = 4)
t.test(Reshaped.data$FRating.P02, mu = 4)
#Bayes Factors
ttestBF(Reshaped.data$FRating.P18, mu = 4)
ttestBF(Reshaped.data$FRating.P20, mu = 4)
ttestBF(Reshaped.data$FRating.P07, mu = 4)
ttestBF(Reshaped.data$FRating.P15, mu = 4)
ttestBF(Reshaped.data$FRating.P05, mu = 4)
ttestBF(Reshaped.data$FRating.P09, mu = 4)
ttestBF(Reshaped.data$FRating.P06, mu = 4)
ttestBF(Reshaped.data$FRating.P16, mu = 4)
ttestBF(Reshaped.data$FRating.P02, mu = 4)


# CSs: 16 Shelmet, 05 Frillish

# T-Tests
t.test(Reshaped.data$PRating.P16, mu = 0)
t.test(Reshaped.data$PRating.P05, mu = 0)

t.test(Reshaped.data$PRating.P16, Reshaped.data$PRating.P05, paired = TRUE)
t.test(Reshaped.data$FRating.P16, Reshaped.data$FRating.P05, paired = TRUE)

# Bayes Faktor
ttestBF(Reshaped.data$PRating.P16, mu = 0)
ttestBF(Reshaped.data$PRating.P05, mu = 0)

ttestBF(Reshaped.data$PRating.P16, Reshaped.data$PRating.P05, paired = TRUE)
ttestBF(Reshaped.data$FRating.P16, Reshaped.data$FRating.P05, paired = TRUE)

# Targets and Fillers: 18 Swadloon, 20 Zorua, 07 Gourgeist, 15 Scraggy, 09 Jangmo, 06 Golett, 02 Carbink