
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[73]:


marks = [92, 15, 72, 41, 29, 45, 55, 44, 41, 20, 24, 60, 7, 13, 57, 18, 90, 77, 2, 21, 20, 40]
# Now let’s set the ranges and no. of intervals
myrange = (0, 100)
interval = 10

# plotting a histogram
plt.hist(marks, interval, myrange, color = 'green', histtype = 'bar')


# In[74]:


plt.xlabel('Marks')
plt.ylabel('Interval')
plt.title('Interval vs Marks Histogram')


# In[75]:


plt.show()


# In[76]:


plt.close()

