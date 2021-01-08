#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Day 3 Assignment 
# Question 1. write a python to remove duplicates from a list
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


# In[4]:


# Question 2. write a python program to get the different between the two list
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)


# In[5]:


# Question 3. write a python program to get the frequency of the element in a list
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)


# In[11]:


# Question 4. write a python program to compute the similarity between two lists.
# Sample data:["red","orange","green","blue","white"],["black","yellow","green","blue"]
# Expected Output:Color1-Color2:["white","orange","red"] , Color2-Color1:["black","yellow"]
from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ",list(counter1 - counter2))
print("Color2-Color1: ",list(counter2 - counter1))


# In[12]:


# Question 5. write a python function that takes a list of words and returns the length of longest one
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])


# In[13]:


# Question 6. write a python program to count the occurrences of each word in given sentance.
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))


# In[15]:


# Question 7. write a python program to count and display the vowels of a given text
def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])
vowel('gradeup a programming language based on tutorials');


# In[16]:


# Question 8. write a python script to generate and print a dictionary that contains a number(between 1 and n) in the from(x,x*x)
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 


# In[17]:


# Question 9. write a python program to combine two dictionary adding values for comman keys
# .d1={'a':100,'b':200,'c':300}
# .d2={'a':300,'b':200,'d':400}
# .Sample Output:({'a':400,'b':400,'d':400,'c':300,})

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


# In[18]:


# Question 9. write a python program to print all unique values in a dictionary
# . Sample Data:[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# . Expected Output:Unique Values:{'S005','S002','S007','S001','S009'}

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)


# In[ ]:




