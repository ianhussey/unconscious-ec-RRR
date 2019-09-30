if (!require(ROI)) {install.packages("ROI"); require(ROI)}
if (!require(ROI.plugin.glpk)) {install.packages("ROI.plugin.glpk"); require(ROI.plugin.glpk)}

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
myData <- read.csv("Olson & Fazio (2001) replication Cornell pretest.csv")

# Descriptives
write.csv(cbind(apply(myData[, grepl("Valence", colnames(myData))], 2, mean),
                apply(myData[, grepl("Valence", colnames(myData))], 2, sd),
                apply(myData[, grepl("Familiar", colnames(myData))], 2, mean),
                apply(myData[, grepl("Familiar", colnames(myData))], 2, sd)), "Descriptives.csv")

# Identify 9 stimuli closest to 0 on the liking scale

sort(abs(apply(myData[, grepl("Valence", colnames(myData))], 2, mean)))[1:9]
sort(round(apply(myData[, grepl("Valence", colnames(myData))], 2, function(x) 1/extractBF(ttestBF(x))$bf), 4), decreasing = TRUE)[1:9]

# Are they below 4 on familiarity scale?

neutralVal <- names(sort(abs(apply(myData[, grepl("Valence", colnames(myData))], 2, mean)))[1:9])
neutralFam <- sub("Valence", "Familiar", neutralVal)

apply(myData[, colnames(myData) %in% neutralFam], 2, function(x) t.test(x, mu = 4))

# Find stimuli with smallest valence mean deviation from 0 AND lowest familiarity
n <- length(neutralVal)
W <- 2
v <- apply(myData[, colnames(myData) %in% neutralFam], 2, mean)
w <- rep(1, 9)
a <- apply(myData[, colnames(myData) %in% neutralVal], 2, mean)
A <- 0

constraints <- rbind(L_constraint(w, "==", W), L_constraint(abs(A-a), "<=", 0.25))

model <- OP(objective = v, 
            constraints = constraints,
            bounds = V_bound(li = 1:n, lb = rep.int(0, n), ui = 1:n, ub = rep.int(1, n)), 
            types = rep.int("B", n), 
            maximum = FALSE)
model

res <- ROI_solve(model, "glpk", verbose = TRUE)
res
ROI::solution(res)

t.test(myData$frillishValence)
1/ttestBF(myData$frillishValence)

t.test(myData$magearnaValence)
1/ttestBF(myData$magearnaValence)

t.test(myData$frillishValence, myData$magearnaValence, paired = TRUE)
1/ttestBF(myData$frillishValence, myData$magearnaValence, paired = TRUE)

t.test(myData$frillishFamiliar, mu = 4)
ttestBF(myData$frillishFamiliar, mu = 4)

t.test(myData$magearnaFamiliar, mu = 4)
ttestBF(myData$magearnaFamiliar, mu = 4)

t.test(myData$frillishFamiliar, myData$magearnaFamiliar, paired = TRUE)
1/ttestBF(myData$frillishFamiliar, myData$magearnaFamiliar, paired = TRUE)


# Larger set
n <- sum(grepl("Valence", colnames(myData)))
W <- 9
v <- apply(myData[, grepl("Familiar", colnames(myData))], 2, mean)
w <- rep(1, 18)
a <- apply(myData[, grepl("Valence", colnames(myData))], 2, mean)
A <- 0

constraints <- rbind(L_constraint(w, "==", W), L_constraint(abs(A-a), "<=", 2.1))

model <- OP(objective = v, 
            constraints = constraints,
            bounds = V_bound(li = 1:n, lb = rep.int(0, n), ui = 1:n, ub = rep.int(1, n)), 
            types = rep.int("B", n), 
            maximum = FALSE)
model

res <- ROI_solve(model, "glpk", verbose = TRUE)
res
ROI::solution(res)

apply(myData[, grepl("Valence", colnames(myData))], 2, mean)[names(apply(myData[, grepl("Valence", colnames(myData))], 2, mean)) %in% sub("Familiar", "Valence", names(ROI::solution(res)[as.logical(ROI::solution(res))]))]
apply(myData[, grepl("Valence", colnames(myData))], 2, sd)[names(apply(myData[, grepl("Valence", colnames(myData))], 2, sd)) %in% sub("Familiar", "Valence", names(ROI::solution(res)[as.logical(ROI::solution(res))]))]
apply(myData[, grepl("Familiar", colnames(myData))], 2, mean)[names(apply(myData[, grepl("Familiar", colnames(myData))], 2, mean)) %in% names(ROI::solution(res)[as.logical(ROI::solution(res))])]
apply(myData[, grepl("Familiar", colnames(myData))], 2, sd)[names(apply(myData[, grepl("Familiar", colnames(myData))], 2, sd)) %in% names(ROI::solution(res)[as.logical(ROI::solution(res))])]
