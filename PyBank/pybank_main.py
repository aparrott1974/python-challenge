
# coding: utf-8

# In[1]:


# our task is to create a Python script that analyzes the records to calculate each of the following:


# In[2]:


# Import Dependencies
import pandas as pd
import os


# In[3]:


# check my Resouces file
#!ls Resources/


# In[4]:


# Create reference to CSV file
csv_path = "Resources/budget_data_2.csv"


# In[5]:


# Import the CSV into a pandas DataFrame
budget_data_df = pd.read_csv(csv_path)    #, low_memory=False)

# take a look at the head to see if it looks right
# budget_data_df.head()
# first column is Date with a month and year, second column is Revenue as integer


# In[6]:


# The total number of months included in the dataset

mo_cnt = budget_data_df["Date"].count()
print("Total Months: " + str(mo_cnt))


# In[7]:


# The total amount of revenue gained over the entire period

rev_sum = budget_data_df["Revenue"].sum()
print("Total Revenue: $" + str(int(rev_sum)))


# In[8]:


# The average change in revenue between months over the entire period

mo_chg = budget_data_df.set_index('Date').diff()
avg_chg = mo_chg.mean()
print("Average Change: $" + str(int(avg_chg)))


# In[9]:


# The greatest increase in revenue (date and amount) over the entire period

max_rev = budget_data_df["Revenue"].max()
max_rev_row = budget_data_df.loc[budget_data_df["Revenue"] == max_rev,:]
print("Greatest Increase in Revenue: " + max_rev_row.iloc[0]['Date'] + " $(" + str(max_rev) + ")")


# In[10]:


# The greatest decrease in revenue (date and amount) over the entire period

min_rev = budget_data_df["Revenue"].min()
min_rev_row = budget_data_df.loc[budget_data_df["Revenue"] == min_rev,:]

print("Greatest Decrease in Revenue: " + min_rev_row.iloc[0]['Date'] + " $(" + str(min_rev)+ ")")


# In[12]:


#jupyter nbconvert --to script 'pybank_main.ipynb'

