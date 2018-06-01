
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[77]:


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [12, 4, 50, 27, 20, 18, 9, 21, 37, 5]

# plotting points as a scatter plot
plt.scatter(x, y, label= "stars", color = "m", marker = "*", s = 30)


# In[78]:


plt.show()


# In[79]:


plt.close()

