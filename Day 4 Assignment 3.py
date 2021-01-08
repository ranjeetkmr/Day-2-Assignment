#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Day 4
# Assignment 3
# Question 1.Write a Python function to find the Max of three numbers.

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))


# In[15]:


# Question 2.Write a Python function that checks whether a passed string is palindrome or not
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True
print(isPalindrome('aza')) 



# In[16]:


# Question 3.Write a Python function that accepts a string and calculate the number of uppercase letters and
#lowercase letters

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# In[17]:


# Question 4 . Write a Python function to sum all the numbers in a list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


# In[19]:


# Question 5.Write a Python function to multiply all the numbers in a list

def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))


# In[20]:


# Question 6.Write a Python function that takes a list and returns a new list with unique elements of the first list

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 


# In[ ]:




