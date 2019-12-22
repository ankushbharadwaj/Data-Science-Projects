#start off by reading in the tables
post_df <- read.csv('/Users/ankushbharadwaj/Desktop/quora_data_challenge/t1_user_active_min.csv')
variant_df <- read.csv('/Users/ankushbharadwaj/Desktop/quora_data_challenge/t2_user_variant.csv')
pre_df <- read.csv('/Users/ankushbharadwaj/Desktop/quora_data_challenge/t3_user_active_min_pre.csv')
user_df <- read.csv('/Users/ankushbharadwaj/Desktop/quora_data_challenge/t4_user_attributes.csv')

####################################################################################

#page 2
#one assumption of t-test is that the data is normally distributed
#verify that option 1 is normally distributed

#option 1, unit of analysis: Total minutes per user in each group 
#going to first generate relevant dataframe by adding a column to the variant dataframe that indicates how many active minutes each user logged on the app over all days after the experiment started
#create empty column 'total_active_mins'
variant_df['total_active_mins'] <- rep_len(0, nrow(variant_df))
#for loop through variant_df and add the total active minutes associated with each uid
for (i in variant_df$uid)
  variant_df$total_active_mins[i+1] <- sum(post_df[post_df$uid==i,]$active_mins)
#split up the variant_df into an experimental sample and a control sample
exp_grp_op1 <- variant_df[variant_df$variant_number==1,]
ctrl_grp_op1 <- variant_df[variant_df$variant_number==0,]

#produce a Q-Q plot for the experimental sample dataset
qqnorm(exp_grp_op1$total_active_mins, main="QQ plot exp_grp_op1")
qqline(exp_grp_op1$total_active_mins)

#produce a Q-Q plot for the control sample dataset
qqnorm(ctrl_grp_op1$total_active_mins, main="QQ plot ctrl_grp_op1")
qqline(ctrl_grp_op1$total_active_mins)

#calculate the R squared value for the experimental sample dataset
qn_exp1=qqnorm(exp_grp_op1$total_active_mins, plot.it=FALSE)
rsq_exp_op1 <- cor(qn_exp1$x,qn_exp1$y)
#value calculated = .1426549

#calculate the R squared value for the control sample dataset
qn_ctrl1=qqnorm(ctrl_grp_op1$total_active_mins, plot.it=FALSE)
rsq_ctrl_op1 <- cor(qn_ctrl1$x,qn_ctrl1$y)
#value calculated = .1838523

#let's use the Anderson-Darling test for normality as well
library(nortest)
#conduct A-D test on experimental sample dataset
ad.test(exp_grp_op1$total_active_mins)
#p-value < 2.2e-16
#conduct A-D test on experimental sample dataset
ad.test(ctrl_grp_op1$total_active_mins)
#p-value < 2.2e-16

#this option produces two samples that are clearly not normally distributed

####################################################################################

#page 3
#unit of analysis: total minutes per user per day in each group
#let's first create the relevant dataframe
#essentially going to add variant_number column to the dataframe that has active minutes each user has logged each day on the app
new_df_op2 <- post_df
#generate empty column in our new dataframe
new_df_op2['variant_number'] <- rep_len(2,nrow(new_df_op2))

#for loop to populate the variant_number column
for (i in unique(new_df_op2$uid))
  new_df_op2[new_df_op2$uid==i,]$variant_number <- variant_df[variant_df$uid==i,]$variant_number

#subset this new dataframe into an experimental group and a control group
exp_grp_op2 <- new_df_op2[new_df_op2$variant_number==1,]
ctrl_grp_op2 <- new_df_op2[new_df_op2$variant_number==0,]

#write these two new dataframes into the computer so they can be read into Python for continued analysis
write.csv(exp_grp_op2,"/Users/ankushbharadwaj/Desktop/exp_grp_op2.csv")
write.csv(ctrl_grp_op2,"/Users/ankushbharadwaj/Desktop/ctrl_grp_op2.csv")

####################################################################################

#page 4

#so for this one, the approach is going to be that we are going to use table 3 to get a new dataframe
#this new dataframe will have active minutes each day for users who will be placed into the experimental group once the experiment has started

#we get the uid of all the individuals who will be placed into the experimental sample
exp_variant_df <- variant_df[variant_df$variant_number==1,]
uid_exp_people <- exp_variant_df$uid

#going to use dplyr
library(dplyr)

#filter the dataframe that has usage minutes of all users before the experiment started such that the new dataframe only has data about users who will be placed in the experimental sample
pre_df <- pre_df %>% filter(uid %in% uid_exp_people)

#rename this new dataframe to the new control group
#reuse previously developed dataframe for the experimental group
ctrl_df_pg4 <- pre_df
exp_df_pg4 <- exp_grp_op2

#write these dataframes out so that they can be read into Python for continued analysis
write.csv(ctrl_df_pg4, "/Users/ankushbharadwaj/Desktop/ctrl_df_pg4.csv")
write.csv(exp_df_pg4, "/Users/ankushbharadwaj/Desktop/exp_df_pg4.csv")

####################################################################################

#page 5

#so we're going to be adding onto the dataframe that has all the users' active minutes each day
#first create 'gender' and 'user_type' columns
new_df_op2['gender'] <- rep_len('0', nrow(new_df_op2))
new_df_op2['user_type'] <- rep_len('0', nrow(new_df_op2))

#now, iterate through this dataframe and populate the gender and user_type columns
for (i in c(1:nrow(new_df_op2))) {
  new_df_op2$gender[i] <- user_df[user_df$uid==new_df_op2$uid[i],]$gender
  new_df_op2$user_type[i] <- user_df[user_df$uid==new_df_op2$uid[i],]$user_type
}
#integer values mean the following
#female = 1, male = 2, unknown = 3
#contributor = 1, new_user = 2, non_reader = 3, reader = 4

#subset this dataframe into a control group and an experimental group
ctrl_df_pg5 <- new_df_op2[new_df_op2$variant_number==0,]
exp_df_pg5 <- new_df_op2[new_df_op2$variant_number==1,]

#write out the dataframe into a csv so that they can be read into Python for continued analysis
write.csv(ctrl_df_pg5, "/Users/ankushbharadwaj/Desktop/ctrl_df_pg5.csv")
write.csv(exp_df_pg5, "/Users/ankushbharadwaj/Desktop/exp_df_pg5.csv")


