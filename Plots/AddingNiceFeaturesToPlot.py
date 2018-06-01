
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[26]:


plt.style.available


# In[33]:


#Adding Nice Customization to the Lines
plt.style.use('fivethirtyeight')
x = [0, 1, 2, 3, 4, 5, 6]
y = [21, 2, 4, 19, 5, 8, 16]

plt.plot(x, y, color = 'blue', linestyle = 'solid', linewidth = 2, marker = 'x', markerfacecolor = 'red', markersize = 6)


# In[34]:


# setting x axis range
plt.xlim(-5, 10)
#setting y axis range
plt.ylim(0, 25)


# In[35]:


plt.show()


# In[36]:


plt.close()

