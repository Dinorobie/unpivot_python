#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the Pandas library
import pandas as pd
import snowflake.connector as sf
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Import file
csv_path = "/Users/robert/Desktop/calls.csv"
df = pd.read_csv(csv_path)
df.head(10)


# In[3]:


melted_df = pd.melt(df, var_name='Event', value_name='Value')
melted_df


# In[ ]:




