
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[22]:


#Coordinates of the first line
x1 = [1, 2, 3, 4]
y1 = [5, 8, 11, 14]

#Coordinates of second line
x2 = [1, 2, 3, 4]
y2 = [1, 0, -1, -2]


# In[23]:


#Plotting the lines
plt.plot(x1, y1, label = 'y = 3x + 2')
plt.plot(x2, y2, label = 'y = -x + 2')


# In[24]:


plt.legend()


# In[25]:


plt.show()


# In[18]:


plt.close()

