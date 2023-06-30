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

3854207 675

speech:

Hello, my name is William Saimo and I will be doing a presentation on the danger factors of breast cancer. That is, the factors that can lead to a negative prognosis in someone who has breast cancer

The reason I chose this dataset to look into is because women in the military are more likely to develop breast cancer than those outside the military, as showin in this study.

This data was obtained from the 2017 November update of the SEER Program of the NCI, which provides information on population-based cancer statistics. The dataset involved female patients with breast cancer diagnosed in 2006-2010. There was a lot of data that I had to look through and I discarded information that was either negatively influencing my data models, or information that didn't have much to with it.

Through my investigations I tested the data in a few different data models and found that it fit this graph the best. You don't need to know the technical details about this graph, just know that because it's curved upwards the way it is, that means

At the end of my findings, I came up with this graph. Again, you don't need to know the technical details, just know that the further a datapoint is from the dotted purple line, the more significant it is to our model. They are components of a Logistic Regression, which answers the question of what the odds are someone will live or die if they have breast cancer. And so, I looked further into the most significant data points.

N Stage refers to how many lymph nodes have cancer cells in them and the following number describes the severity. I did a test on this number and came up with the results that the chances that this is random is close to zero and also statistically significant. That's data speak to let you know that this is a very strong predictor.

Progesterone status refers to whether or not there were progesterone receptors in the cancer cells. Interestingly, the inclusion of these receptors mean that the cancer actually grows more slowly that if they weren't there. However, cancer with these receptors are also much more likely to come back even after successful treatment. This data point was about as statistically significant as N Stage N3

Age refers to how old someone is when they get the diagnosis. Even though it is about as far away from the dotted line as progesterone status, it is much less statistically significant. That is, although age is still a strong indicator, it's not as strong as the other two

From this, we can conclude that with the information of whether or not cancer has infiltrated the lymph nodes and whether or not there are progesterone receptors in that cancer, we can accurately predict whether or not a prognosis will be fatal. Things to look at next for me are things that increase risk factors for people with breast cancer. Like whether or not there is a genetic component or if there are lifestyle decisions that lead to higher rates of breast cancer.

If you have any questions, please let me know