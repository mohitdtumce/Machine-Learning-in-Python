
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[63]:


# setting x-coordinates of bars 
x = [0, 5, 10, 15, 20]

# setting heights of bars
Popularity = [80, 74, 86, 40, 95]

# labels which will appear for bars
Anime = ['Naruto', 'FairyTale', 'DeathNote', 'FutureDiary', 'DeadlySins']

# Plotting barchart
plt.bar(x, Popularity, tick_label = Anime, width = 3, color = 'b')


# In[64]:


plt.xlabel('Anime')
plt.ylabel('Popularity')
plt.title('Anime Vs Popularity Chart')


# In[65]:


plt.show()


# In[66]:


plt.close()

