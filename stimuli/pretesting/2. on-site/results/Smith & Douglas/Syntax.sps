* Encoding: UTF-8.
* Encoding: .
*First I have to recode all the ratings of each charecter because Qualtrics simply labels the Likert scales output at 1-9, an ddoes not use the labels as actual values. Below are the positive to negative ratings.
DATASET ACTIVATE DataSet1.
RECODE berg1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO berg_feel.
RECODE carb1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO carb_feel.
RECODE cosmo1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO cosmo_feel.
RECODE cran1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO cran_feel.
RECODE fril1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO fril_feel.
RECODE gole1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO gole_feel.
RECODE grub1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO grub_feel.
RECODE gour1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO gour_feel.
RECODE zor1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO zor_feel.
RECODE jang1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO jang_feel.
RECODE kric1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO kric_feel.
RECODE wimp1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO wimp_feel.
RECODE swad1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO swad_feel.
RECODE slig1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO slig_feel.
RECODE shel1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO shel_feel.
RECODE scra1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO scra_feel.
RECODE scat1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO scat_feel.
RECODE phan1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO phan_feel.
RECODE palp1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO palp_feel.
RECODE mage1 (1=-4) (2=-3) (3=-2) (4=-1) (5=0) (6=1) (7=2) (8=3) (9=4) INTO mage_feel.
EXECUTE.
*Now I am recoding the familiarity varaible so that it can match the data values of the actual Likert scale and be directly comparable to other studies in the replication project. 
RECODE berg2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO berg_famil.
RECODE carb2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO carb_famil.
RECODE cosmo2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO cosmo_famil.
RECODE cran2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO cran_famil.
RECODE fril2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO fril_famil.
RECODE gole2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO gole_famil.
RECODE grub2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO grub_famil.
RECODE gour2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO gour_famil.
RECODE zor2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO zor_famil.
RECODE jang2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO jang_famil.
RECODE kric2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO kric_famil.
RECODE wimp2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO wimp_famil.
RECODE swad2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO swad_famil.
RECODE slig2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO slig_famil.
RECODE shel2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO shel_famil.
RECODE scra2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO scra_famil.
RECODE scat2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO scat_famil.
RECODE phan2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO phan_famil.
RECODE palp2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO palp_famil.
RECODE mage2 (1=0) (2=1) (3=2) (4=3) (5=4) (6=5) (7=6) (8=7) (9=8) INTO mage_famil.
EXECUTE.

*Below I am running descriptives to make sure all the data was recoded correctly and that all data is within specified ranges. I am also ussing these values to calcuate the Cohen's D below.
DESCRIPTIVES VARIABLES=berg_feel carb_feel cosmo_feel cran_feel fril_feel gole_feel grub_feel 
    gour_feel zor_feel jang_feel kric_feel wimp_feel swad_feel slig_feel shel_feel scra_feel scat_feel 
    phan_feel palp_feel mage_feel berg_famil carb_famil cosmo_famil cran_famil fril_famil gole_famil 
    grub_famil gour_famil zor_famil jang_famil kric_famil wimp_famil swad_famil slig_famil shel_famil 
    scra_famil scat_famil phan_famil palp_famil mage_famil
  /STATISTICS=MEAN STDDEV MIN MAX.

*The table below shows my work for calculating the Cohen’s D for each character’s familiarity and positivity to negativity (i.e., feel) rating.*We used the following formula: Cohen’s d = (Mean - Mu) / SD. 
*Because we are trying to test the sample’s difference from 0 on both the familiarity and feeling ratings the Mu is 0 in all calculations. Thus, Cohen’s D is simply mean/SD. This infromation is also in the excel sheet.
*		Mean	Std. Deviation	Cohen's D diff from zero	.
*	berg_feel	-0.0429	1.70622	-0.025118209	.
*	carb_feel	0.9710	1.87060	0.519092301	.
*	cosmo_feel	1.2714	1.71879	0.739722388	.
*	cran_feel	-0.1014	2.50966	-0.040423556	.
*	fril_feel	0.5571	1.97547	0.282030434	.
*	gole_feel	0.5000	1.88626	0.265075019	.
*	grub_feel	-0.5797	1.86615	-0.310644648	.
*	gour_feel	-0.6957	2.43325	-0.285893991	.
*	zor_feel	0.1449	2.25751	0.064198068	.
*	jang_feel	0.5714	1.66439	0.343326606	.
*	kric_feel	1.2029	1.80343	0.66700753	.
*	wimp_feel	-1.1884	1.80094	-0.659880012	.
*	swad_feel	-0.1549	1.99032	-0.077841596	.
*	slig_feel	1.3478	1.93137	0.697861147	.
*	shel_feel	0.0429	1.95185	0.0220	.
*	scra_feel	0.1571	1.96074	0.080144542	.
*	scat_feel	-0.5571	1.81488	-0.306986086	.
*	phan_feel	-0.6143	2.54406	-0.241458527	.
*	palp_feel	0.6000	2.22893	0.26918781	.
*	mage_feel	-0.0580	2.07140	-0.027986362	.
*	berg_famil	0.9286	2.01675	0.460429207	.
*	carb_famil	1.0580	2.34448	0.451260271	.
*	cosmo_famil	0.9286	2.05942	0.450890306	.
*	cran_famil	1.5652	2.69246	0.58133278	.
*	fril_famil	1.0571	2.21252	0.477800687	.
*	gole_famil	1.0000	2.18692	0.457264594	.
*	grub_famil	1.0290	2.15551	0.477375375	.
*	gour_famil	1.0725	2.32833	0.460614094	.
*	zor_famil	1.6087	2.77180	0.580379819	.
*	jang_famil	1.0571	2.15948	0.489535832	.
*	kric_famil	1.4493	2.72535	0.531775739	.
*	wimp_famil	0.9420	2.05715	0.457928196	.
*	swad_famil	1.1714	2.21308	0.52932051	.
*	slig_famil	1.1159	2.31705	0.481622261	.
*	shel_famil	1.1714	2.30922	0.507282838	.
*	scra_famil	1.4286	2.68960	0.531146195	.
*	scat_famil	1.0857	2.15852	0.502989892	.
*	phan_famil	1.1286	2.39517	0.471185796	.
*	palp_famil	1.2571	2.47706	0.507514441	.
*	mage_famil	1.1304	2.22891	0.50716979	.


*Below I am using the One Sample Normal Bayesian option to estimate the Bayes Factor. I also copied this infromation into the Excel doc.
DATASET ACTIVATE DataSet1.
BAYES ONESAMPLE
  /MISSING SCOPE=ANALYSIS
  /CRITERIA CILEVEL=95 METHOD=AGL TOL=0.000001 MAXITER=2000
  /INFERENCE DISTRIBUTION=NORMAL VARIABLES=berg_feel carb_feel cosmo_feel cran_feel fril_feel 
    gole_feel grub_feel gour_feel zor_feel jang_feel kric_feel wimp_feel swad_feel slig_feel shel_feel 
    scra_feel scat_feel phan_feel palp_feel mage_feel berg_famil carb_famil cosmo_famil cran_famil 
    fril_famil gole_famil grub_famil gour_famil zor_famil jang_famil kric_famil wimp_famil swad_famil 
    slig_famil shel_famil scra_famil scat_famil phan_famil palp_famil mage_famil ANALYSIS=BAYESFACTOR
  /PRIOR VARDIST=DIFFUSE MEANDIST=DIFFUSE
  /DATA VARIABLES= berg_feel carb_feel cosmo_feel cran_feel fril_feel gole_feel grub_feel gour_feel 
    zor_feel jang_feel kric_feel wimp_feel swad_feel slig_feel shel_feel scra_feel scat_feel phan_feel 
    palp_feel mage_feel berg_famil carb_famil cosmo_famil cran_famil fril_famil gole_famil grub_famil 
    gour_famil zor_famil jang_famil kric_famil wimp_famil swad_famil slig_famil shel_famil scra_famil 
    scat_famil phan_famil palp_famil mage_famil NULLVALUE=0.

*In the excel sheet I have highlighted the 9 characters with the smallest Cohen’s D and largest Bayes Factor.Both of these metrics were in agreement, concerning which character’s liking ratings differed the least from 0.
 *The 9 chosen characters are: Shelmet, Bergmite, Magearna, Cranidos, Zorua, Swadloon, Scraggy, Phantump, and Golett. 



*Below I ran one sample t-test to make each character selected above is significantly lower than 4 in familiarity (somewhat familiar). 
T-TEST
  /TESTVAL=4
  /MISSING=ANALYSIS
  /VARIABLES=shel_famil berg_famil mage_famil cran_famil zor_famil swad_famil scra_famil phan_famil 
    gole_famil
  /CRITERIA=CI(.95).

* Next I selected the two most neutral characters to be selected as CSs (Shelmet and Bergmite). Below I am running paired samples t-tests and Bayes Factor analyses to make sure they do not significantly differ in liking or familiarity.
T-TEST PAIRS=berg_feel berg_famil WITH shel_feel shel_famil (PAIRED)
  /CRITERIA=CI(.9500)
  /MISSING=ANALYSIS.

BAYES RELATED
  /MISSING SCOPE=ANALYSIS
  /CRITERIA CILEVEL=95 METHOD=AGL TOL=0.000001 MAXITER=2000
  /INFERENCE DISTRIBUTION=NORMAL ANALYSIS=BAYESFACTOR
  /PRIOR VARDIST=DIFFUSE MEANDIST=DIFFUSE
  /PAIR VARIABLES=berg_feel shel_feel NULLVALUE=0
  /PAIR VARIABLES=berg_famil shel_famil NULLVALUE=0.
