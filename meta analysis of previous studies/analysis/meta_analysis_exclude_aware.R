#meta anlysis surveliance task - excluding awere participants
library(metafor)
library(MAd)
#read the file:
all <- read.csv("C:\\Users\\tmoranyo\\Documents\\LipLab\\projects\\RRR_fazio&olson2001\\meta-analysis\\meta-analysis_exclude_awere.csv")

#first aggragate when needed Hedge's g:
all.agg <- agg(
  id = compid, es = g, var = var.g, cor = 0.5,
  method = "BHHR", data = all
)

#random effect
require(weightr)
weightfunct(effect=all.agg$es, all.agg$var)


#funell plot
meta.RE <- rma(es, var, method="REML", data=all.agg)
meta.RE.egger <- rma(es, var, mods=sqrt(var), method="REML", data=all.agg)
par(mar=c(5,5,2,2))
plot(x="", y="", type="n",
     xlab="Effect size (Hedges' g)", ylab="Standard error",
     cex.lab=1.5, xlim=c(-1,1.5), ylim=c(0.5, 0),
     frame.plot=FALSE)
polygon(c(-1.96*.49, 0, 1.96*.49), y = c(.49, 0, .49),
        col=rgb(.85, .85, .85), border=NA, lwd=1)
polygon(c(-1.96*.49+meta.RE$b, meta.RE$b, 1.96*.49+meta.RE$b), y = c(.49, 0, .49),
        col=rgb(.85, .85, .85, .01), border="black", lwd=1, lty=2)
lines(c(meta.RE$b,meta.RE$b), c(.49,0), lty=2)
points(all.agg$es, sqrt(all.agg$var),
       pch=19, col=rgb(.70,.30,.30,.65), cex=2, lwd=1.2)
se = seq(0,.49,.01)
y = matrix(NA,length(se))
for (i in 1:length(y)){y[i] = meta.RE.egger$beta[1] + meta.RE.egger$beta[2]*se[i]}
lines(x=y, y=se, typ='l', lty=1, col="red", lwd=2)
