#!/usr/bin/env python
# coding: utf-8

# <h3> Mock Interview Python Screening test </h3>
# 

# In[2]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
dataframe = pd.read_csv("adult_census_data.csv")


# In[ ]:





# <b> Q1. After importing the adult_census_data.csv file, please filter this to include only the following criteria: </b>
# <p>
# 
# <li> State-Gov</li>
# <li> Bachelors </li>
# <li> Never-Married </li>
# <li> Adm-Clerical </li> 
# <li> Not-in-familiy </li>
# <li> White </li>
# <li> Male </li> 
# <li> United States </li>
# <li> <=50K </li> 
# 
# <b> Feel free to any method to complete this tasks. However, we recommend you use either list filtering [], or .loc to complete this task.</b>

# <b> Put your code below </b>

# In[17]:


filtered_data = dataframe.loc[
    (dataframe[' State-gov'] == 'State-Gov') &
    (dataframe[' Bachelors'] == 'Bachelors') &
    (dataframe[' Never-married'] == 'Never-Married') &
    (dataframe[' Adm-clerical'] == 'Adm-Clerical') &
    (dataframe[' Not-in-family'] == 'Not-in-family') &
    (dataframe[' White'] == 'White') &
    (dataframe[' Male'] == 'Male') &
    (dataframe[' United-States'] == 'United States') &
    (dataframe[' <=50K'] == '<=50K')
]
print(filtered_data)


# <b> Currently, the dataframe you are using has the following column names: </b>
# 
# [' State-gov', ' Bachelors', ' Never-married',
#        ' Adm-clerical', ' Not-in-family', ' White', ' Male', ' United-States', ' <=50K']
#        
#      
# <b> Q2. Please re-name all the newly filtered columns in the pandas DataFrame to the following: </b>
# 
# Employment Type, Degree Status, Marriage-Status, Job-Role, Family-Role, Ethnicity, Gender, Country, Earnings
# 
# E.g. State-Gov becomes Employment Type, Bachelors becomes Degree Status, etc.

# <b> Put your code below </b>

# In[22]:


filtered_data = dataframe.loc[
    (dataframe[' State-gov'] == 'Employment_Type') &
    (dataframe[' Bachelors'] == 'Degree_Status') &
    (dataframe[' Never-married'] == 'Marriage-Status') &
    (dataframe[' Adm-clerical'] == 'Job-Role') &
    (dataframe[' Not-in-family'] == 'Family-Role') &
    (dataframe[' White'] == 'Ethnicity') &
    (dataframe[' Male'] == 'Gender') &
    (dataframe[' United-States'] == 'Country') &
    (dataframe[' <=50K'] == 'Earnings')
]
print(filtered_data)


# <b> Q3. The Job Role Columns holds the job information for each individual in this census snapshot. Using this column, create a Bar Chart that shows the count of 'Unique' Jobs per Job Group in the "Job-Role" Column in ascending order, as per the provided image below </b>
# 

# <b> Put your code below </b>

# In[20]:


job_counts = dataframe[' Adm-clerical'].value_counts().sort_values()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
job_counts.plot(kind='barh', color='skyblue')
plt.xlabel('Count')
plt.title('Count of Unique Jobs per Job Group')
plt.show()


# <b> Q4. Please create two bar plots as per below that show:
#     
#     1) The number of individuals who have a High School Graduate Diploma AND earn <=50K in the United States
#     2) The number of individuals who have a High School Graduate Diploma AND earn >50K in the United States 
# 
# Please note you will be looking specifically at the *Job Role* column

# <b> Put Your Code Below </b>

# In[26]:



high_school_graduates = dataframe[(dataframe[' Adm-clerical'] == 'High School Grad') & (dataframe[' United-States'] == 'United-States')]

count_earning_lessthan_50k = high_school_graduates[high_school_graduates[' <=50K'] == ' <=50K'].shape[0]

count_earning_morethan_50k = high_school_graduates[high_school_graduates[' <=50K'] == ' >50K'].shape[0]

print("High School Graduates earning <=50K in the United States:", count_earning_lessthan_50k)
print("High School Graduates earning >50K in the United States:", count_earning_morethan_50k)


# In[ ]:





# 
# 

# <H2> Challenge Question </H2>
# 
# <b> Q5. Which Job Role has the highest <i> proportion </i> of individuals who earn >50K? </b>

# <b> Put your code below </b>

# In[ ]:




