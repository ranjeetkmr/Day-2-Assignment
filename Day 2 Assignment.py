#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Day 2 Assignment
# Question 1 :- find the value of the following question, where x=5
# . (2x+5/x^2+5x+6)
# . (x^2+5x+6/2x+5)
# . (2x-3)(x-9)
x=int(input("Enter the number:"))
y=(2*x+5/x**2+5*x+6)
print("Result is :",y)
y=(x**2+5*x+6/2*x+5)
print("Result is :",y)
y=(2*x-3)*(x-9)
print("Result is :",y)




# In[ ]:


#Create a username and password login file using nested while loop.
print('Enter correct username and password combo to continue')
count =0
while count<5:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password =='India' and username =='India':
        print("welcome\n Successfully Login")
           
    else:
            print('Invalid your Username/Password! ')
            count+1


# In[ ]:





# In[ ]:





# In[ ]:




