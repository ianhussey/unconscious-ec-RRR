#The data's folder (directory)


#read the evaluation file 
eval <- read.csv("C:\\Users\\tmoranyo\\Documents\\LipLab\\projects\\RRR_fazio&olson2001\\replication_procedure\\pretest_pokemon_UGent\\results\\pretest.csv")
#read the demo file
demo <-read.csv("C:\\Users\\tmoranyo\\Documents\\LipLab\\projects\\RRR_fazio&olson2001\\replication_procedure\\pretest_pokemon_UGent\\results\\demographics.csv")
#merge
allok <- full_join(eval, demo, by = c("subject"))

#demo (N =88)
mean(allok$age_response, na.rm=T) #21.52
sd(allok$age_response, na.rm=T) #3.90
table(allok$sex_response) # 73 female (82%)


creatures = select(allok, contains("response"))
#sparte liking and exciting ratings
like = select(creatures, contains("liking"))
fami = select(creatures, contains("familiar"))
#liking
write.csv(like,file=paste("C:\\Users\\tmoranyo\\Documents\\LipLab\\projects\\RRR_fazio&olson2001\\replication_procedure\\pretest_pokemon_UGent\\results", "like.csv", sep="\\"))
write.csv(fami,file=paste("C:\\Users\\tmoranyo\\Documents\\LipLab\\projects\\RRR_fazio&olson2001\\replication_procedure\\pretest_pokemon_UGent\\results", "fami.csv", sep="\\"))

#OUTPUT OF MEANS stds liking
like_out  = c()
for (i in 1:dim(like)[2]){
  like_out$name[i] = strsplit(paste(colnames(like)[i]), "_")[[1]]
  like_out$mean_liking[i] = mean(like[,i], na.rm=T)
  like_out$sd_liking[i] = sd(like[,i], na.rm=T)
  like_out$like_d.es[i] = cohensD(like[,i], mu=0 )  
  like_out$n[i] = sum(!is.na(like[,i]))
  
}
like_out  = as.data.frame(like_out)

#familiar

fami_out  = c()
for (i in 1:dim(fami)[2]){
  fami_out$name[i] = strsplit(paste(colnames(fami)[i]), "_")[[1]]
  fami_out$mean_fami[i] = mean(fami[,i], na.rm=T)
  fami_out$sd_fami[i] = sd(fami[,i], na.rm=T)
  fami_out$fmi_d.es[i] = cohensD(like[,i], mu=0)    
  fami_out$n[i] = sum(!is.na(fami[,i]))
  
}
fami_out  = as.data.frame(fami_out)

all_cretures = cbind(like_out,fami_out)
write.csv(all_cretures,file=paste("C:\\Users\\tmoranyo\\Documents\\LipLab\\projects\\RRR_fazio&olson2001\\replication_procedure\\pretest_pokemon_UGent\\results", "all_cretures2.csv", sep="\\"))

#test potential stimuli

#Magearna
t.test(like$Magearna_Liking_response, mu=0)
cohensD(like$Magearna_Liking_response, mu=0)
ttestBF(x = like$Magearna_Liking_response, mu = 0)
#t(87) = -0.05, p = 0.959, d =0.05, BF10 = 0.117 
t.test(fami$Magearna_familiar_response, mu=4)
cohensD(fami$Magearna_familiar_response, mu=4)
ttestBF(x = fami$Magearna_familiar_response, mu = 4)
#t(87) = -30.58, p < 0.001, d =3.26, BF10 > 1000

#Zorua
t.test(like$Zorua_Liking_response, mu=0)
cohensD(like$Zorua_Liking_response, mu=0)
ttestBF(x = like$Zorua_Liking_response, mu = 0)
#t(87) = 0.09, p = 0.922, d =0.01, BF10 = 0.118
t.test(fami$Zorua_familiar_response, mu=4)
cohensD(fami$Zorua_familiar_response, mu=4)
ttestBF(x = fami$Zorua_familiar_response, mu = 4)
#t(87) = -16.25, p < 0.001, d =1.73, BF10 > 1000

#Jangmo
t.test(like$Jangmo_Liking_response, mu=0)
cohensD(like$Jangmo_Liking_response, mu=0)
ttestBF(x = like$Jangmo_Liking_response, mu = 0)
#t(87) = 0.17, p = 0.858, d =0.01, BF10 = 0.119
t.test(fami$Jangmo_familiar_response, mu=4)
cohensD(fami$Jangmo_familiar_response, mu=4)
ttestBF(x = fami$Jangmo_familiar_response, mu = 4)
#t(87) = -39.66, p < 0.001, d =4.22, BF10 > 1000

#Shelmet
t.test(like$Shelmet_Liking_response, mu=0)
cohensD(like$Shelmet_Liking_response, mu=0)
ttestBF(x = like$Shelmet_Liking_response, mu = 0)
#t(87) = 0.29, p = 0.767, d =0.03, BF10 = 0.122
t.test(fami$Shelmet_familiar_response, mu=4)
cohensD(fami$Shelmet_familiar_response, mu=4)
ttestBF(x = fami$Shelmet_familiar_response, mu = 4)
#t(87) = -28.59, p < 0.001, d =3.04, BF10 > 1000

#Golett
t.test(like$Golett_Liking_response, mu=0)
cohensD(like$Golett_Liking_response, mu=0)
ttestBF(x = like$Golett_Liking_response, mu = 0)
#t(87) = -0.72, p = 0.472, d =0.07, BF10 = 0.151
t.test(fami$Golett_familiar_response, mu=4)
cohensD(fami$Golett_familiar_response, mu=4)
ttestBF(x = fami$Golett_familiar_response, mu = 4)
#t(87) = -32.38, p < 0.001, d =3.45, BF10 > 1000

#Scatterbug
t.test(like$Scatterbug_Liking_response, mu=0)
cohensD(like$Scatterbug_Liking_response, mu=0)
ttestBF(x = like$Scatterbug_Liking_response, mu = 0)
#t(87) = 0.83, p = 0.407, d =0.08, BF10 = 0.164
t.test(fami$Scatterbug_familiar_response, mu=4)
cohensD(fami$Scatterbug_familiar_response, mu=4)
ttestBF(x = fami$Scatterbug_familiar_response, mu = 4)
#t(87) = -27.38, p < 0.001, d =2.91, BF10 > 1000

#Cranidos
t.test(like$Cranidos_Liking_response, mu=0)
cohensD(like$Cranidos_Liking_response, mu=0)
ttestBF(x = like$Cranidos_Liking_response, mu = 0)
#t(87) = -1.47, p = 0.143, d =0.157, BF10 = 0.334 
t.test(fami$Cranidos_familiar_response, mu=4)
cohensD(fami$Cranidos_familiar_response, mu=4)
ttestBF(x = fami$Cranidos_familiar_response, mu = 4)
#t(87) = -13.97, p < 0.001, d =1.48, BF10 > 1000

#Swadloon
t.test(like$Swadloon_Liking_response, mu=0)
cohensD(like$Swadloon_Liking_response, mu=0)
ttestBF(x = like$Swadloon_Liking_response, mu = 0)
#t(87) = -1.89, p = 0.061, d =0.20, BF10 = 0.646
t.test(fami$Swadloon_familiar_response, mu=4)
cohensD(fami$Swadloon_familiar_response, mu=4)
ttestBF(x = fami$Swadloon_familiar_response, mu = 4)
#t(87) = -22.28, p < 0.001, d =2.37, BF10 > 1000

#Bergmite
t.test(like$Bergmite_Liking_response, mu=0)
cohensD(like$Bergmite_Liking_response, mu=0)
ttestBF(x = like$Bergmite_Liking_response, mu = 0)
#t(87) = 1.96, p = 0.052, d =0.20, BF10 = 0.736
t.test(fami$Bergmite_familiar_response, mu=4)
cohensD(fami$Bergmite_familiar_response, mu=4)
ttestBF(x = fami$Bergmite_familiar_response, mu = 4)
#t(87) = -35.44, p < 0.001, d =3.77, BF10 > 1000



#test diffrence between CSs, starting from the lowers in valence.
#Magearna vs. Zorua
t.test(like$Magearna_Liking_response,like$Zorua_Liking_response, paired=T)#p= .915
ttestBF(x =like$Magearna_Liking_response, y = like$Zorua_Liking_response, paired=T)
#BF10 = 0.118, BF01= 8.47
t.test(fami$Magearna_familiar_response,fami$Zorua_familiar_response, paired=T)#p= .001
ttestBF(x =fami$Magearna_familiar_response, y = fami$Zorua_familiar_response, paired=T)
#BF10 = 17.07, BF01= 0.05

#Magearna vs. Jangmo
#Comparing the two two CSs on likability 
t.test(like$Magearna_Liking_response, like$Jangmo_Liking_response, paired=T)
cohen.d(like$Magearna_Liking_response, like$Jangmo_Liking_response, paired=T)
ttestBF(like$Magearna_Liking_response, like$Jangmo_Liking_response, paired=TRUE)
#t(87) = -0.17, p = 0.862, d =-0.01, BF10 = 0.119

#Comparing the two two CSs on familiarity
t.test(fami$Magearna_familiar_response, fami$Jangmo_familiar_response, paired=T)
cohen.d(fami$Magearna_familiar_response, fami$Jangmo_familiar_response, paired=T)
ttestBF(fami$Magearna_familiar_response, fami$Jangmo_familiar_response, paired=TRUE)
#t(87) = 0.21, p = 0.830, d =0.02, BF10 = 0.120



















#FILLERS






