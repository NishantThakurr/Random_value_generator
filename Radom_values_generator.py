#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Modified linear congruence method
#Proof with matplot lib

import matplotlib.pyplot as plt


no_of_random_numbers = int(input("How many random numbers would you like to generate?\nInput : "))
 

def random_values_generator():
    seed = 2
    multiplier = 12
    increment = 7
    modulus = 999
    lst=[]
    lstx=[]
    num = seed
    for i in range(no_of_random_numbers):
        rmd = (multiplier * num + increment) % modulus
        random_no = float(rmd/100)
        if random_no in lst:
            rmd=int(rmd*4.5)
            multiplier +=1
            increment +=1
        lst.append(random_no)
        lstx.append(i)
        num= rmd
    print(f"List of {no_of_random_numbers} random numbers :\n")
    print(lst)
    print("Scatter Plot :\n")
    plt.scatter(lstx,lst)
    plt.show()
   
    
    
    
random_values_generator()

