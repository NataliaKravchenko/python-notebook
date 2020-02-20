#!/usr/bin/env python
# coding: utf-8

# In[4]:


#BASIC # 2 Create your first array with the elements [1,22.4,5,35,4,6.7,3,8,40] and print it. Experiment what the following
#functions do: ndim, shape, size and dtype.

import numpy as np


# In[5]:


my_array=np.array([1,22.4,5,35,4,6.7,3,8,40])
print(my_array)


# In[7]:


my_array.ndim


# In[8]:


my_array.shape


# In[9]:


my_array.size


# In[10]:


my_array.dtype


# In[11]:


#BASIC #3 Create your first matrix with the elements [['a', 'b'],['c', 'd'],[3, 3]] and print it. Experiment what the
#following functions do: ndim, shape, size and dtype
import pandas as pd


# In[12]:


data=[['a', 'b'],['c', 'd'],[3, 3]]


# In[13]:


df=pd.DataFrame(data)
print(df)


# In[14]:


df.ndim


# In[15]:


df.shape


# In[16]:


df.size


# In[18]:


df.dtype


# In[19]:


#BASIC # 4 Create numpy 1 dimension array using each of the functions arange and rand
new_array=np.arange(start=1, stop=10, step=2)
print(new_array)


# In[21]:


random_array=np.random.rand(5)
print(random_array)


# In[22]:


#BASIC # 5 Create numpy 2 dimensions matrix using each of the functions zeros and rand
my_matrix=np.zeros((3,2))
print(my_matrix)


# In[24]:


random_matrix=np.random.rand(2,2)
print(random_matrix)


# In[35]:


#BASICS # 6 Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix
a = np.empty([1, 20])
a.fill(7)
print(a)


# In[37]:


np.reshape(a, (4,5))


# In[38]:


#BASICS # 6 another way
new_a=np.empty([4,5])
for i in range(4):
    for j in range(5):
        new_a[i][j]=7
print(new_a)


# In[40]:


#BASIC # 7 Create a 6 x 6 matrix with all numbers up to 36
my_matrix=list(range(36))
print(my_matrix)


# In[49]:


reshaped=np.reshape(my_matrix,(6,6))
print(reshaped)


# In[50]:


df=pd.DataFrame(reshaped)
print(df)


# In[54]:


print(df[0:1])


# In[56]:


df[0].iloc[0]


# In[61]:


df.iloc[[-2,-1],:]


# In[62]:


df.iloc[[2,3],[2,3]]


# In[66]:


#Repeat for each column
total=df[0].sum()
print(total)


# In[77]:


# I tried to calculate sum of each column at once, but the result is wierd. Why so?
df.sum(axis=0)


# In[82]:


#ADVANCED # 2 Explore the dataset using functions like to_string(), columns, index, dtypes, shape, info() and describe()
pd=pd.read_csv(r'C:\Users\Nat\Downloads\insurance.csv')
print(pd)


# In[83]:


# to_string(), columns, index, dtypes, shape, info() and describe()
pd.to_string()


# In[84]:


pd.columns


# In[85]:


pd.columns


# In[86]:


pd.index


# In[87]:


pd.dtypes


# In[88]:


pd.shape


# In[89]:


pd.info()


# In[90]:


pd.describe()


# In[91]:


#ADVANCED # 3 Print only the column age
pd["age"]


# In[93]:


#ADVANCED # 4 Print only the columns age,children and charges
pd[["age","children","charges"]]


# In[108]:


#ADVANCED # 5 Print only the first 5 lines and only the columns age,children and charges
pd.iloc[[0,1,2,3,4],[0,3,6]]


# In[118]:


#ADVANCED # 6 What is the average, minimum and maximum charges ?
pd["charges"].mean()


# In[119]:


pd["charges"].min()


# In[120]:


pd["charges"].max()


# In[121]:


# ADVANCED # 7 What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
#Answer: 52 years old, nonsmoker
selection=pd["charges"]==10797.3362


# In[125]:


# ADVANCED # 8 What is the age of the person who paid the maximum charge?
#Answer:54
max_charge=pd['charges'].max()
print(max_charge)


# In[128]:


pd[pd['charges']==63770.42801]


# In[135]:


#ADVANCED # 9 How many insured people do we have for each region?
# Answer: for southwest:325, for southeast:364, for northwest:325, for northeast:324
pd.region.unique()


# In[138]:


# We can change the name of the region inside the selection
pd[pd["region"]=="northeast"]


# In[139]:


#ADVANCED # 10 How many insured people are children?
pd["children"].sum()


# In[142]:


#ADVANCED # 11 What do you expect to be the correlation between charges and age, bmi and children?
#Answer:Between charges and age there should be a correlation. I also expect that there should be a corelation between
#children and bmi.


# In[141]:


#ADVANCED # 12 Using the method corr(), check if your assumptions were correct.
#Answer:Between charges and age there is the strongest correlation in the whole matrix. There is almost no correlation
#children and bmi.

pd.corr()


# In[ ]:




