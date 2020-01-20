#!/usr/bin/env python
# coding: utf-8

# In[30]:


script01 = input("Enter the first script name: ")
script02 = input("Enter the second script name: ")
output = input("Enter output file name: ")

def counter_py(script01, script02, output):
    with open(script01, "r") as f1:
        char1 = f1.read()
        char1 = "".join(char1.split())
        len1 = len(char1)
        f1.close()
        
    with open(script02, "r") as f2:
        char2 = f2.read()
        char2 = "".join(char2.split())
        len2 = len(char2)
        f2.close()
        
    with open(output, "w") as txt:
        txt.write("There are " + str(len1) + " characters in the first script.\n")
        txt.write("There are " + str(len2) + " characters in the second script.\n")
        txt.close()
        
counter_py(script01, script02, output)

