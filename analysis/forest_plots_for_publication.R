# Open and run analysis.Rmd so that the results_1, results_2, results_3, and results_4 objects are present in your environment. 
# Then run this script. 


# Ns
nrow(data_1)
# >[1] 1340

nrow(data_2)
# >[1] 1007

nrow(data_3)
# >[1] 755

nrow(data_4)
# >[1] 1060



setwd("~/git/unconscious-ec-RRR/analysis")

pdf(NULL)
dev.control(displaylist = "enable")

par(mfrow = c(2, 2))

size <- 1

metafor::forest(results_1$fitted_model,
                xlab = substitute(paste("Hedges' ", italic('g'))),
                addcred = TRUE,
                xlim = c(-1.1, 1.6),
                at = c(-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0),
                refline = 0,
                mlab = add_heterogeneity_metrics_to_forest(results_1$fitted_model))
text(-1.1, 14, substitute(paste("(a) Olson & Fazio (2001) exclusions (", italic('n'), " = 1340)")), pos = 4)
text(1.6, 13.97, substitute(paste(italic('g'), " [95% CI]")), pos = 2)


metafor::forest(results_2$fitted_model,
                xlab = substitute(paste("Hedges' ", italic('g'))),
                addcred = TRUE,
                xlim = c(-1.1, 1.6),
                at = c(-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0),
                refline = 0,
                mlab = add_heterogeneity_metrics_to_forest(results_2$fitted_model))
text(-1.1, 14, substitute(paste("(b) Olson & Fazio (2001) modified exclusions (", italic('n'), " = 1007)")), pos = 4)
text(1.6, 13.97, substitute(paste(italic('g'), " [95% CI]")), pos = 2)


metafor::forest(results_3$fitted_model,
                xlab = substitute(paste("Hedges' ", italic('g'))),
                addcred = TRUE,
                xlim = c(-1.1, 1.6),
                at = c(-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0),
                refline = 0,
                mlab = add_heterogeneity_metrics_to_forest(results_3$fitted_model))
text(-1.1, 14, substitute(paste("(c) Bar-Anan et al. (2010) exclusions (", italic('n'), " = 755)")), pos = 4)
text(1.6, 13.97, substitute(paste(italic('g'), " [95% CI]")), pos = 2)


metafor::forest(results_4$fitted_model,
                xlab = substitute(paste("Hedges' ", italic('g'))),
                addcred = TRUE,
                xlim = c(-1.1, 1.6),
                at = c(-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0),
                refline = 0,
                mlab = add_heterogeneity_metrics_to_forest(results_4$fitted_model))
text(-1.1, 14, substitute(paste("(c) Bar-Anan et al. (2010) modified exclusions (", italic('n'), " = 1060)")), pos = 4)
text(1.6, 13.97, substitute(paste(italic('g'), " [95% CI]")), pos = 2)


p1 <- recordPlot()
invisible(dev.off())

# # display the saved plot
# grid::grid.newpage()
# p1

pdf("forest_plots.pdf",
    width = 10, 
    height = 7.5)
p1
dev.off()
