
# coding: utf-8

# In[20]:


infile = open("ORDER", "r")


# In[21]:


order = infile.readlines()


# In[32]:


for o in order:
    o.strip()
    script_import = '.import "/dpool/swalkow2/mysql-2019-03-01/'+ o + '.csv" ghtorrent.' + o
    get_ipython().system(' script_import')
