
# coding: utf-8

# <h1>iPhone6 Barometer Precision</h1>

# In[3]:

get_ipython().magic(u'matplotlib inline')


# In[4]:

import numpy as np
import matplotlib.pyplot as plt


# In[5]:

x = np.loadtxt('zerodata.txt')
print len(x)


# In[6]:

rms = np.sqrt(x.var())
mean = x.mean()
rmstxt = 'rms = %.1f cm' % rms
meantxt = 'mean = %.1f cm' % mean
print rmstxt
print meantxt


# In[7]:

fig = plt.figure()
ax = plt.subplot(111)
plt.hist(x);
plt.xlabel('$\Delta h$ (cm)', fontsize='x-large')
plt.xlim(-40,40)
plt.text(0.65, 0.9, rmstxt, transform=ax.transAxes, fontsize='x-large')
plt.text(0.65, 0.8, meantxt, transform=ax.transAxes, fontsize='x-large')
fig.savefig('barometer_deltah.png')


# In[8]:

print np.sqrt(x.var())
print x.mean()


# In[ ]:




# In[ ]:



