
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[15]:


#Plotting a simple line
x = [1, 2, 3, 4]
y = [4, 7, 10, 13]
plt.plot(x, y)


# In[16]:


plt.xlabel('x label')
plt.ylabel('y label')
plt.title('This is a Simple Line')


# In[17]:


plt.show()


# In[18]:


plt.close()

