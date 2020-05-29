# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:04:06 2019

@author: ramagurr
"""


#%%
#Write a function when given two lists will return a single sorted list.
def sort(a,b):
    c=a+b
    r=len(c)
    for i in range(r):
        for j in range(i+1,r):
            if c[i]>c[j]:
                t=c[i]
                c[i]=c[j]
                c[j]=t
    return c
print(sort([1,6,3],[5,2,2]))


#%%

#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
def revstring(mystr):
    s=[]
    a=''
    for i in mystr:
        s.append(i)
    for i in range(len(s)):
        a=a+s.pop()
    return a
print(revstring("senorita"))

#%%
#return yes if you find atleast a pair of elements in input array whose reminder is 3 else no
def reminder(arr):
    yes=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]%arr[j]==3:
                 yes=+1
                 break
    if yes>=1:
        print('yes')
    else: print('No')
    
print(reminder([1,13,5,11,4]))

     
#%%
#Count the number of occurences and its index of a letter in a string
def count_str(istr,l):
    count=0
    ind=0
    i=[]
    for c in istr:
        if l==c:
            count=count+1
            i.append(ind)
        ind+=1
    return count,i
print(count_str('apple','p'))
    
#%%
#Check if the integer is a pallindrome
def pallindrome(x):
    a=str(x)
    l=[]
    rl=''
    for i in a:
        l.append(i)
    for i in range(len(a)):
        rl=rl+l.pop()
    if rl==a:
        return True
    else: return False
print(pallindrome('-121'))

#Program without converting the integer to string
print(list('str'))


#%%
#check if the string has all unique characters

#%%
#given two strings, check if one is the permutation of the other
def perm(s1,s2):
    a=list(s1)
    b=list(s2)
    a.sort()
    b.sort()
    if a==b:
        return True
    else : return False
    
#print(perm('The cow is monk','The monk is cow'))
#print(perm('drive','drv'))
        
#Without sort function
def is_perm(s1,s2):
    s1=s1.replace(' ','')
    s2=s2.replace(' ','')
    if len(s1) != len(s2): return False
    for c in s1:
        if c in s2:
            s2=s2.replace(c,'')
    return len(s2)==0
    
print(is_perm('drive','driv  e'))

#%%
#Check if string is a pallindrome
import string
def pallind(s):
    s=s.lower()
    s=s.translate(string.punctuation)
    s=s.replace(" ","")
    return s== s[::-1]
print(pallind('racecar'))

#%%
#pivot a dataframe
import pandas as pd
df = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                       'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'baz': [1, 2, 3, 4, 5, 6]})
df.pivot(index='foo', columns='bar', values='baz')

#%%
#Write a iterative and recursive function that implements the factorial of a number.

def fact_it(n):
    ans=1
    while (n>=1):
        ans=ans*n
        n=n-1
    return ans
print(fact_it(5))

def fact_rec(n):
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n-1)
print(fact_rec(5))

#%%
"""
Given a positive integer, N, print all the integers from 1 to N.
For multiples of 3 print "Fizz" instead of the number and for multiples of 5
print "Buzz". For numbers which are multiples of 3 and 5, print "FizzBuzz".
"""

def fizzbuzz(n):
    for i in range (1,n+1):
        if (i%3==0 and i%5==0):
            print("Fizzbuzz")
        elif (i%3==0):
            print("Fizz")
        elif (i%5==0):
            print("buzz")
        else:
            print(i)
fizzbuzz(15)

#%%
"""
Anagram:
Given two strings, check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, only the order 
of characters can be different. For example, “act” and “tac” are anagram of each other.


input_str_1 = "practice makes perfect"
input_str_2 = "perfect makes practice"

input_str_3 = "allergy"
input_str_4 = "allergic"
"""

def anagram(s1,s2):
    s1=s1.replace(" ","")
    s2=s2.replace(" ","")
    s1=''.join(sorted(s1))
    s2=''.join(sorted(s2))
    return s1==s2
print(anagram('aabsd','absda'))

#%%
"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
Example:
nums = [1, 3, 11, 2, 7]
target = 9
return : [3,4]
9 - 1 = 8 -> {8 : 0}
9 - 3 = 6 -> {8 : 0, 6 : 1}
9 - 11 = -2 -> {8 : 0, 6 : 1, -2 : 2}
9 - 2 = 7 -> {8 : 0, 6 : 1, -2 : 2, 7 : 3}
nums[i], i
"""
nums = [1, 3, 11, 2, 7]
target = 9
def two_sum(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = {}
    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return [aux_dict[nums[i]], i]
        else:
            aux_dict[target - nums[i]] = i
print(two_sum(nums, target))

#%%
"""
1.3
URLify: Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string. (Note: If
implementing in Java, please use character array so that you can perform this
operation in place.)
"""

input_test_str = "Mr. John Smith"
input_test_len = len(input_test_str)


#%%
#maximum pairwise program

#%%
# Bubble Sort Algorithm --iterative
"""how j initially goes from the first element in the list to the element immediately 
before the last. During the second iteration, j runs until two items from the last, 
then three items from the last, and so on. At the end of each iteration, the end 
portion of the list will be sorted."""

def bubble_sort(array):
    length=len(array)
    for i in range(length):
        a_s=True
        for j in range(length-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                a_s=False
        if a_s:
            break
    return array

print(bubble_sort([8,2,6,4,5]))
        
#%%
#Merge Sort
"""
"""

def merge_sort(array):
    if len(array)<2:
        return list(array)
    mp=len(array)//2
    return merge(left=merge_sort(array[:mp]),right=merge_sort(array[mp:]))
def merge(left,right):
    result=[]
    l_i= 0
    r_i=0
    while len(result)<len(left)+len(right):
        if left[l_i]<= right[r_i]:
            result.append(left[l_i])
            l_i+=1
        else:
            result.append(right[r_i])
            r_i+=1
        if len(left)==l_i:
            result.extend(right[r_i:])
            break
        if len(right)==r_i:
            result.extend(left[l_i:])
            break
    return result
print(merge_sort([8,2,6,4,5]))

            
#%%
#Binary search-- The list should already be sorted for the binary search

def find_index(array,value):
    left,right=0,len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==value:
            return mid
        if value<array[mid]:
            right=mid-1
        elif value>array[mid]:
            left=mid+1

def contains(array,value):
    return find_index(array,value) is not None  
def find_left(array,value):
    index=find_index(array,value)
    while array[index]==value and index >= 0:
        index-=1
    return index+1
def find_right(array,value):
    index=find_index(array,value)
    while index <len(array) and array[index]==value:
        index+=1
    return index-1
def find_all(array,value):
    l=find_left(array,value)
    r=find_right(array,value)
    return (l,r)

print(find_all([15,15,15],15))

#%%
#Find the longest pallindromic substring
def pallin(string):
    if string[:]==string[::-1] and len(string)>=2:
        return 'Yes'
  
def lps(string):
    l,d=0,len(string)
    while d>=0:
        l=0
        while l+d<=len(string):
            if pallin(string[l:l+d])=='Yes':        
                return string[l:l+d]
            else:
                l+=1
        d-=1       

print(lps(''))   
       
#%%
#Queue
import queue as q
qu=q.Queue()
qu.put(1)
qu.put(2)
qu.put(3)
for i in qu:
    print(i)
    
#%%
"""
Suppose you're given the following table, showing open and close prices as 
well as trading volume for a particular equity.
In python, write code to show the volume weighted average price (VWAP) for a 
rolling 2-day window. The VWAP is calculated as [(Price * Volume) / Volume]. 
In this case, your resultant table would start on 1/3/2019 and roll daily from there.
"""
import pandas as pd
import numpy as np
rng = pd.date_range(start='2019-01-01', periods=15)

df = pd.DataFrame({'Open': abs(np.random.randn(len(rng))),
                  'Close': abs(np.random.randn(len(rng))),
                  'Volume': np.random.randint(500, 3000, len(rng))},
                   index=rng)
df['VWAP']=df['Volume']*df['Close']
df['VWAP']=(df['VWAP'].rolling(3).sum())/df['Volume'].rolling(3).sum()
df

