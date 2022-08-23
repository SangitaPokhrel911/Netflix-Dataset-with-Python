#!/usr/bin/env python
# coding: utf-8

# #  This dataset has information about Netflix TV shows and Movies available till 2021.
# 

# In[2]:


#importing the libraries and dataset
import pandas as pd
data=pd.read_csv("Netflix Dataset.csv")


# In[3]:


data


# # Some information about the dataset

# 1.head()

# In[4]:


#show top 5 records of the dataset
data.head()


# 2. tail

# In[5]:


data.tail()


# 3.shape

# In[6]:


data.shape


# So in this dataset, there are total 7789 number of rows and 11 columns.

# **4.size**

# In[7]:


#to show the total number of values(elements)
data.size


# **5. columns**

# In[8]:


#to show all the columns name
data.columns


# **6. dtypes**

# In[9]:


#to show the datatype of each column
data.dtypes


# **8. info**

# In[10]:


#to show indexes, columns, datatypes of each columns, memory at once.
data.info()


# # Task 1: Check the duplicate values and then remove if there is any

# In[11]:


data[data.duplicated()]


# In[12]:


#remove the duplicate datas
data.drop_duplicates()


# In[13]:


#remove the duplicate rows permanently
data.drop_duplicates(inplace=True)


# In[14]:


#we can see now that all the duplicates data are deleted
data[data.duplicated()]


# In[15]:


data.shape


# So now, 2 rows are removed. 
# 

# # Task 2: Check for the null values and show with heat map

# In[16]:


# to show where the null value is present
data.isnull()


# In[17]:


#count the null values in each column
data.isnull().sum()


# **Seaborn library**

# In[18]:


#import seaborn library
import seaborn as sns


# In[19]:


#heatmap to show null values count
sns.heatmap(data.isnull())


# # Information about particular element from dataset

# **Q1. Show id and director of 'House of Cards'**

# **isin()**

# In[20]:


data.head()


# In[21]:


data[data['Title'].isin(['House of Cards'])]


# **str.contains()**

# In[22]:


#we can do by the str.contains() also
data[data['Title'].str.contains('House of Cards')]


# **Q2.Show the bar graph of year where the highest number of TV shows and Movies were released**

# In[23]:


data.dtypes


# **to_datetime**

# In[24]:



data['R_date']= pd.to_datetime(data['Release_Date'])


# In[25]:


data.head(2)


# In[26]:


data.dtypes


# **dt.year.value_counts()**

# In[27]:


#counts the occurance of all the individuals Years in date column
data['R_date'].dt.year.value_counts()


# **Bar Graph**

# In[28]:


data['R_date'].dt.year.value_counts().plot(kind='bar', title='Date vs Number of Movies')


# **Q3. Count the Movie name and Tv shows from the dataset and show in bar graph**
# 

# **groupby()**

# In[29]:


data.head(2)


# In[30]:


#grouping all the unique items from the single column and show their count
data.groupby('Category').Category.count()


# **countplot()**

# In[31]:


#to show the count of all unique values of any column in the form of bar graph
sns.countplot(data['Category'])


# **Q4. Show all the movies that were released in the year 2020**

# **Create new column**

# In[32]:


data.head(2)


# In[33]:


data['Year']= data['R_date'].dt.year


# In[34]:


data.head(1)


# **Filtering**

# In[35]:


data[(data['Category']== 'Movie') & (data['Year']==2020)]


# **Q5. Show only the Titles of all TV shows that were released in UK only.**

# **Filtering**

# In[36]:


data.head(1)


# In[37]:


data[(data['Category']== 'TV Show') & (data['Country']=='United Kingdom')]


# In[38]:


data[(data['Category']== 'TV Show') & (data['Country']=='United Kingdom')]['Title']


# **Q6. Show Top 10 Directors who had the highest number of TV Shows and Movies in Netflix.**

# **value_counts()**
# 

# In[39]:


data.head(1)


# In[42]:


data['Director'].value_counts().head(10)


# **Q7. Show all Records where 'Category is Movie and Type is Comedies' or 'Country is United Kingdom'**

# **Filtering(And, OR Operators)**

# In[43]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies')]


# In[44]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# **Q8. How many movies/shows Tom Cruise was cast?**

# In[45]:


data.head(2)


# In[46]:


#filtering
data['Cast'] == 'Tom Cruise'


# In[47]:


data[data['Cast']=='Tom Cruise']


# In[48]:


#str.contains()
data[data['Cast'].str.contains('Tom Cruise')]


# In[50]:


#Since there are null values in the dataset so lets remove the null vlaues

data_new = data.dropna()


# In[51]:


data_new.head(2)


# In[53]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# **Q9. Maximum duration of a Movie/Show on Netflix?**

# In[54]:


data.head(1)


# In[55]:


#data['Duration'].unique()
data.Duration.unique()


# In[61]:


data.Duration.dtypes


# In[63]:


#str.split()
data[['Minutes', 'Unit']]= data['Duration'].str.split(' ', expand = True)


# In[64]:


data.head(3)


# In[68]:


#max()

data['Minutes'].max()


# In[69]:


#min()
data['Minutes'].min()


# **Q10. Top 6 countries which had the highest no of TV Shows?**

# In[70]:


data_tvshow = data[data['Category']=='TV Show']


# In[72]:


data_tvshow.head(2)


# In[74]:


data_tvshow['Country'].value_counts()


# In[76]:


data_tvshow['Country'].value_counts().head(6)


# **Q11. Sort the dataset by Year**

# In[77]:


data.sort_values(by = 'Year')


# In[78]:


data.sort_values(by = 'Year', ascending = False).head(4)


# In[ ]:




