
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[80]:


# Let’s first define labels
projects = ['spychat', 'twitterAPI', 'instabot', 'Clarifai']

# Now Let’s see their contribution(the area which they’ll cover in Pie Chart)
area = [10, 7, 2, 13]

# Setting colors for each label
myColors = ['r', 'm', 'g', 'b']

# Plotting Pie Chart
plt.pie(area, labels = projects, colors = myColors, startangle = 90, shadow = True, explode = (0, 0, 0.1, 0), radius = 1.2, autopct = '%1.1f%%')


# In[81]:


plt.legend()
plt.show()


# In[82]:


plt.close()

