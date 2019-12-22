#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:40:13 2019

@author: ankushbharadwaj
"""
#import necessary libraries, add as project continues
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.stats.api as sms
import matplotlib.pyplot as plt
import statistics as statistics

####################################################################################

#PAGE 3
#read in data from tables produced in R
treatment_df = pd.read_csv("/Users/ankushbharadwaj/Desktop/exp_grp_op2.csv")
control_df = pd.read_csv("/Users/ankushbharadwaj/Desktop/ctrl_grp_op2.csv")

#STEP 1: REMOVE OUTLIERS
#going to remove outliers more than 3 standard deviations from mean
#get standard deviation of active minutes per user per day for each group
std_treat = np.std(treatment_df["active_mins"])
std_ctrl = np.std(control_df["active_mins"])

#find out how many values we should see removed by looking at the z-score
sum(abs(stats.zscore(treatment_df["active_mins"])) > 3)
#value output: 30
sum(abs(stats.zscore(control_df["active_mins"])) > 3)
#value output: 142

#call shape before and after removing to confirm how many values removed with z-score above
treatment_df.shape
#remove outliers
treatment_df = treatment_df[treatment_df["active_mins"] <= 3*std_treat+statistics.mean(treatment_df["active_mins"])]
treatment_df = treatment_df[treatment_df["active_mins"] >= -3*std_treat+statistics.mean(treatment_df["active_mins"])]
treatment_df.shape
#calling shape before and after confirms that 30 rows were lost

#repeat removal process for control group
control_df.shape
control_df = control_df[control_df["active_mins"] <= 3*std_ctrl+statistics.mean(control_df["active_mins"])]
control_df = control_df[control_df["active_mins"] >= -3*std_ctrl+statistics.mean(control_df["active_mins"])]
control_df.shape
#calling shape before and after confirms that 142 rows were lost

#STEP 2: CONDUCT T-TEST AND CALCULATE 95% CONFIDENCE INTERVALS

#first establish null hypothesis
#null hypothesis: mean difference of active minutes spent on app by each user on each day between experimental group and control group is 0 

treatment_df["active_mins"].describe()
control_df["active_mins"].describe()
#note that the mean active_mins is higher in the dataframe that has the experimental group than the control group

#conduct t-test
stats.ttest_ind(treatment_df["active_mins"], control_df["active_mins"], equal_var = False)
#output: t-statistic=30.686846737487123 and pvalue<.05)

#now we're going to find the 95% confidene interval
x1 = treatment_df["active_mins"]
x2 = control_df["active_mins"]
#going to use statsmodels
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))

####################################################################################

#PAGE 4
#read in the dataframes wrangled in R
ctrl_df_pg4 = pd.read_csv("/Users/ankushbharadwaj/Desktop/ctrl_df_pg4.csv")
exp_df_pg4 = pd.read_csv("/Users/ankushbharadwaj/Desktop/exp_df_pg4.csv")

#STEP 1: REMOVE OUTLIERS
#going to remove outliers more than 3 standard deviations from mean

#get standard deviation of active minutes per user per day for each group
std_exp = np.std(exp_df_pg4["active_mins"])
std_ctrl = np.std(ctrl_df_pg4["active_mins"])

#find out how many values we should see removed by looking at the z-score
sum(abs(stats.zscore(exp_df_pg4["active_mins"])) > 3)
#value output: 30
sum(abs(stats.zscore(ctrl_df_pg4["active_mins"])) > 3)
#value output: 5

#call shape before and after removing to confirm how many values removed with z-score above
exp_df_pg4.shape
#remove outliers
exp_df_pg4 = exp_df_pg4[exp_df_pg4["active_mins"] <= 3*std_exp+statistics.mean(exp_df_pg4["active_mins"])]
exp_df_pg4 = exp_df_pg4[exp_df_pg4["active_mins"] >= -3*std_exp+statistics.mean(exp_df_pg4["active_mins"])]
exp_df_pg4.shape
#confirm that by comparing the shape before and after, 30 rows were revoved

#repeat removal process for control group
ctrl_df_pg4.shape
#remove outliers
ctrl_df_pg4 = ctrl_df_pg4[ctrl_df_pg4["active_mins"] <= 3*std_ctrl+statistics.mean(ctrl_df_pg4["active_mins"])]
ctrl_df_pg4 = ctrl_df_pg4[ctrl_df_pg4["active_mins"] >= -3*std_ctrl++statistics.mean(ctrl_df_pg4["active_mins"])]
ctrl_df_pg4.shape
#confirm that by comparing the shape before and after, 5 rows were removed

#STEP 2: CONDUCT T-TEST AND CALCULATE 95% CONFIDENCE INTERVALS
#first establish null hypothesis
#null hypothesis: mean difference of active minutes spent on app by each user on each day between experimental group and control group is 0 

ctrl_df_pg4["active_mins"].describe()
exp_df_pg4["active_mins"].describe()
#once again, notice that the experimental dataframe has a higher mean active minutes each user spent on the app per day than the control dataframe

x1_4 = exp_df_pg4["active_mins"]
x2_4 = ctrl_df_pg4["active_mins"]

#conduct t-test
stats.ttest_ind(x1_4, x2_4, equal_var = False)
#output: t-statistic=67.78502009822164 and pvalue<.05)

#now we're going to find the 95% confidene interval
#going to use statsmodels
cm_4 = sms.CompareMeans(sms.DescrStatsW(x1_4), sms.DescrStatsW(x2_4))
print(cm_4.tconfint_diff(usevar='unequal'))

##########################################################################################

#PAGE 5
#read in dataframes wrangled in R
ctrl_df_pg5 = pd.read_csv("/Users/ankushbharadwaj/Desktop/ctrl_df_pg5.csv")
exp_df_pg5 = pd.read_csv("/Users/ankushbharadwaj/Desktop/exp_df_pg5.csv")

#STEP 1: REMOVE OUTLIERS, SAME PROCESS AS PREVIOUSY DONE
#get standard deviation of active minutes per user per day for each group
std_exp_5 = np.std(exp_df_pg5["active_mins"])
std_ctrl_5 = np.std(ctrl_df_pg5["active_mins"])

#find out how many values we should see removed by looking at the z-score
sum(abs(stats.zscore(exp_df_pg5["active_mins"])) > 3)
#output: 30
sum(abs(stats.zscore(ctrl_df_pg5["active_mins"])) > 3)
#output: 142

#call shape before and after removing to confirm how many values removed with z-score above
exp_df_pg5.shape
#remove outliers
exp_df_pg5 = exp_df_pg5[exp_df_pg5["active_mins"] <= 3*std_exp_5+statistics.mean(exp_df_pg5["active_mins"])]
exp_df_pg5 = exp_df_pg5[exp_df_pg5["active_mins"] >= -3*std_exp_5+statistics.mean(exp_df_pg5["active_mins"])]
exp_df_pg5.shape

#repeat removal process for control group
ctrl_df_pg5.shape
#remove outliers
ctrl_df_pg5 = ctrl_df_pg5[ctrl_df_pg5["active_mins"] <= 3*std_ctrl_5+statistics.mean(ctrl_df_pg5["active_mins"])]
ctrl_df_pg5 = ctrl_df_pg5[ctrl_df_pg5["active_mins"] >= -3*std_ctrl_5+statistics.mean(ctrl_df_pg5["active_mins"])]
ctrl_df_pg5.shape

#STEP 2: CALCULATE RATIOS OF EACH GENDER AND EACH USER TYPE IN EACH GROUP
ctrl_df_pg5["gender"].value_counts()
exp_df_pg5["gender"].value_counts()

ctrl_df_pg5["user_type"].value_counts()
exp_df_pg5["user_type"].value_counts()

#calculating ratios of each gender in control group
male_ratio_ctrl = sum(ctrl_df_pg5["gender"]==2)/ctrl_df_pg5.shape[0]
female_ratio_ctrl = sum(ctrl_df_pg5["gender"]==1)/ctrl_df_pg5.shape[0]
unknown_ratio_ctrl = sum(ctrl_df_pg5["gender"]==3)/ctrl_df_pg5.shape[0]
gender_ctrl_ratio = (male_ratio_ctrl, female_ratio_ctrl, unknown_ratio_ctrl)

#calcuating ratios of each gender in experimental group
male_ratio_exp = sum(exp_df_pg5["gender"]==2)/exp_df_pg5.shape[0]
female_ratio_exp = sum(exp_df_pg5["gender"]==1)/exp_df_pg5.shape[0]
unknown_ratio_exp = sum(exp_df_pg5["gender"]==3)/exp_df_pg5.shape[0]
gender_exp_ratio = (male_ratio_exp, female_ratio_exp, unknown_ratio_exp)

#calculating ratios of each user type in control group
contributor_ratio_ctrl = sum(ctrl_df_pg5["user_type"]==1)/ctrl_df_pg5.shape[0]
newuser_ratio_ctrl = sum(ctrl_df_pg5["user_type"]==2)/ctrl_df_pg5.shape[0]
nonreader_ratio_ctrl = sum(ctrl_df_pg5["user_type"]==3)/ctrl_df_pg5.shape[0]
reader_ratio_ctrl = sum(ctrl_df_pg5["user_type"]==4)/ctrl_df_pg5.shape[0]
usertype_ctrl_ratio = (contributor_ratio_ctrl,newuser_ratio_ctrl,nonreader_ratio_ctrl,reader_ratio_ctrl)

#calculating ratios of each user type in experimental group
contributor_ratio_exp = sum(exp_df_pg5["user_type"]==1)/exp_df_pg5.shape[0]
newuser_ratio_exp = sum(exp_df_pg5["user_type"]==2)/exp_df_pg5.shape[0]
nonreader_ratio_exp = sum(exp_df_pg5["user_type"]==3)/exp_df_pg5.shape[0]
reader_ratio_exp = sum(exp_df_pg5["user_type"]==4)/exp_df_pg5.shape[0]
usertype_exp_ratio = (contributor_ratio_exp,newuser_ratio_exp,nonreader_ratio_exp,reader_ratio_exp)

#STEP 3: SET UP SOME PLOTS
#going to use bar charts to compare ratios of genders and user types in each group

#set up plot for gender
fig, ax = plt.subplots()
index = np.arange(3)
bar_width = 0.35
opacity = 0.8

#bar plot for gender ratios in control group
rects1 = plt.bar(index, gender_ctrl_ratio, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Control Group')

#bar plot for gender ratios in experimental group
rects2 = plt.bar(index + bar_width, gender_exp_ratio, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Experimental Group')

#execute plot
plt.xlabel('Gender')
plt.ylabel('Proportion')
plt.title('Proportion of Gender in Groups')
plt.xticks(index + bar_width/2, ('Male', 'Female', 'Unknown'))
plt.legend()
plt.tight_layout()
plt.show()

#set up plot for user tyope
fig, ax = plt.subplots()
index = np.arange(4)
bar_width = 0.35
opacity = 0.8

#bar plot for user type ratios in control group
rects1 = plt.bar(index, usertype_ctrl_ratio, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Control Group')

#bar plot for user type ratios in experimental group
rects2 = plt.bar(index + bar_width, usertype_exp_ratio, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Experimental Group')

#execute plot
plt.xlabel('User Type')
plt.ylabel('Proportion')
plt.title('Proportion of User Type in Groups')
plt.xticks(index + bar_width/2, ('Contributor', 'New User', 'Non-reader', 'Reader'))
plt.legend()
plt.tight_layout()
plt.show()

#STEP 4: CONDUCT T TEST AND CALCULATE 95% CONFIDENCE INTERVAL

#t-test and CI for GENDER
#subset control and experimental sample data for males only
male_ctrl_df = ctrl_df_pg5[ctrl_df_pg5["gender"]==2]
male_exp_df = exp_df_pg5[exp_df_pg5["gender"]==2]

x1 = male_ctrl_df["active_mins"]
x2 = male_exp_df["active_mins"]

x1.describe()
x2.describe()
#mean active minutes noted to be greater in the experimental sample

stats.ttest_ind(x1, x2, equal_var = False)
#output: t-statistic=-20.836860473108892, pvalue<.05

#now we're going to find the 95% confidence interval
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))
#output: (-4.167924612661975, -3.4512418598873427)

#subset control and experimental sample data for females only
female_ctrl_df = ctrl_df_pg5[ctrl_df_pg5["gender"]==1]
female_exp_df = exp_df_pg5[exp_df_pg5["gender"]==1]

x1 = female_ctrl_df["active_mins"]
x2 = female_exp_df["active_mins"]

x1.describe()
x2.describe()
#mean active minutes noted to be greater in the experimental sample

stats.ttest_ind(x1, x2, equal_var = False)
#output: t-statistic=-17.052753645677395, pvalue<.05

#now we're going to find the 95% confidence interval
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))
#output: (-4.674910956248812, -3.7110472378534602)

#subset control and experimental sample data for unknown genders only
unknown_ctrl_df = ctrl_df_pg5[ctrl_df_pg5["gender"]==3]
unknown_exp_df = exp_df_pg5[exp_df_pg5["gender"]==3]

x1 = unknown_ctrl_df["active_mins"]
x2 = unknown_exp_df["active_mins"]

x1.describe()
x2.describe()
#mean active minutes noted to be greater in the experimental sample

stats.ttest_ind(x1, x2, equal_var = False)
#output: t-statistic=-18.041531844898703, pvalue<.05

#now we're going to find the 95% confidence interval
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))
#output: (-6.884559362142111, -5.535265614125654)

#t-test and CI for USER TYPE
#subset control and experimental sample data for contributors only
contributor_ctrl_df = ctrl_df_pg5[ctrl_df_pg5["user_type"]==1]
contributor_exp_df = exp_df_pg5[exp_df_pg5["user_type"]==1]

x1 = contributor_ctrl_df["active_mins"]
x2 = contributor_exp_df["active_mins"]

x1.describe()
x2.describe()
#sample mean higher in experimental sample

stats.ttest_ind(x1, x2, equal_var = False)
#output: t-statistic=-13.362249564731702, pvalue<.05

#now we're going to find the 95% confidence interval
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))
#output: (-25.811923581725303, -19.207468491632078)

#subset control and experimental sample data for new users only
newuser_ctrl_df = ctrl_df_pg5[ctrl_df_pg5["user_type"]==2]
newuser_exp_df = exp_df_pg5[exp_df_pg5["user_type"]==2]

x1 = newuser_ctrl_df["active_mins"]
x2 = newuser_exp_df["active_mins"]

x1.describe()
x2.describe()
#sample mean higher in experimental sample

stats.ttest_ind(x1, x2, equal_var = False)
#output: t-statistic=-11.95004871846676, pvalue<.05

#now we're going to find the 95% confidence interval
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))
#output: (-4.555460036233804, -3.27148648619829)

#subset control and experimental sample data for non-readers only
nonreader_ctrl_df = ctrl_df_pg5[ctrl_df_pg5["user_type"]==3]
nonreader_exp_df = exp_df_pg5[exp_df_pg5["user_type"]==3]

x1 = nonreader_ctrl_df["active_mins"]
x2 = nonreader_exp_df["active_mins"]

x1.describe()
x2.describe()
#sample mean higher in experimental sample

stats.ttest_ind(x1, x2, equal_var = False)
#output: t-statistic=-59.007782898664104, pvalue<.05

#now we're going to find the 95% confidecne interval
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))
#output: (-4.390409365475092, -4.108124999207799)

##subset control and experimental sample data for readers only
reader_ctrl_df = ctrl_df_pg5[ctrl_df_pg5["user_type"]==4]
reader_exp_df = exp_df_pg5[exp_df_pg5["user_type"]==4]

x1 = reader_ctrl_df["active_mins"]
x2 = reader_exp_df["active_mins"]

x1.describe()
x2.describe()
#sample mean higher in experimental sample

stats.ttest_ind(x1, x2, equal_var = False)
#output: t-statistic=-42.357846901213954, pvalue<.05

#now we're going to find the 95% confidence interval
cm = sms.CompareMeans(sms.DescrStatsW(x1), sms.DescrStatsW(x2))
print(cm.tconfint_diff(usevar='unequal'))
#(-13.322081885421905, -12.143718222299317)

##########################################################################################






