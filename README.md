# Breast_Cancer_Study

This dataset of breast cancer patients was obtained from the 2017 November update of the SEER Program of the NCI, which provides information on population-based cancer statistics. The dataset involved female patients with infiltrating duct and lobular carcinoma breast cancer (SEER primary cites recode NOS histology codes 8522/3) diagnosed in 2006-2010. Patients with unknown tumour size, examined regional LNs, positive regional LNs, and patients whose survival months were less than 1 month were excluded; thus, 4024 patients were ultimately included.

data
Age - age of the person the data is being collected on
Race - race of the person, other includes pacific islander and other more specific races
Marital Status - Married, Divorced, Single, Widow
T Stage - the stage of the tumor size
N Stage - involvement of lymph nodes (larger stage means more lymph nodes)
6th Stage - classification system used by AJ CC 6th edition, a breast cancer research guide. hard to explain, will probably drop
Differentiate - how much the cancer cells looks like the normal cells that they were derived from
Grade - how fast the cancer grows
Stage - whether the cancer has stayed within the region where it originated or has spread to other parts of the body, like the lungs or stomach
Tumor Size - expressed in cubic ml
Estrogen Status - whether or not the cancer has estrogen receptors
Progesterone Status - whether or not the cancer has progesterone receptors
Regional Node Examined - which specific lymph node the cells were tested from. Will probably drop. Not explained well.
Regional Node Positive - will probably drop for same reason above
Survival Months - about how long the person is expected to survive. Dropped as it is a predictor and we are using the dataframe for other predictions. May skew results
Status - whether the person has since died

After parsing through the data, I did a quick AUC test to see if the data was significant and got a result of around .75
Since this is a fairly good indicator of moving forward, I standardized the data and did a logistic regression to get the coefficients. They were all fairly small with the highest at around .45

After I did some hypothesis tests on the 3 largest, I came up with the following data.

Stage N3: (statistic=-10.981203765477005, pvalue=5.378710704967063e-26)
Progesterone: (statistic=9.35138388753239, pvalue=9.918443501831385e-20)
Age: (statistic=-3.322896024862656, pvalue=0.0009309078378221079)
