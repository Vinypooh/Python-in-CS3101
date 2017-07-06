###############################################
# COMS3101.001 - Python - Homework 1
#
# Please fill in your solutions for part 2 to 4 
# below. 

##############################################################################
# Part 2
# For each line in the following interactive Python interpreter session, write
# a short justification for the output, clearly indicating which objects are
# in memory and which variables refer to them (ignore garbage collection for
# this exercise)
# Add your explanations as a new comment after each line. 

#>>> y,x = [1], [1]

## Two objects: y->Object1: [1]    x->Object2: [1]

#>>> x is y
#False

## y and x refer to two different objects.

#>>> x = y

## Two objects: nothing-> Object1: [1]  x,y -> Object2: [1]
## Eventually garbage collection will remove Object1, but this problem
## assumes that objects are never collected. 

#x is y
#True

##x and y refer to the same object

#>>> y = y + x

## Three objects:  Object1: [1]    x-> Object2:[1]    y->Object3: [1,1]

#>>> x.append(y)

## Three objects:      Object1: [1]   
##                 x-> Object2:[1,Object3] = Object2:[1,[1,1]
##                 y->Object3: [1,1]

#y.append(24)

## Three objects:      Object1: [1]   
##                 x-> Object2:[1,Object3] = Object2:[1,[1,1,24]
##                 y-> Object3 : [1,1,24]

#>>> x == y
#False

##obviously no equal 

##############################################################################
# Part 3 - Lists and for-Loops
#
# Use two nested for loops to compute the value 
# of expressions of the form 
# (a[1]+...+a[m])*(b[1]+...+b[m]).
# 
# Assume that a and b are arbitrary sequences of numbers.
# For instance, for a = [1, 2, 4] and b = [2, 3] the result would be 35.

a = [1, 2, 4]
b = [2, 3]
#Your code starts here
result = 0
for x in a:
    for y in b:
        result += x * y
#Your code ends here


##############################################################################
# Part 4 - Loops, Strings, and Indices
#
# Given a string s create a second string s2 that is a copy of s but without 
# characters that have an identical element next to them.
#
# For instance the, string
# s = ’abbcaabcaa’
# should produce the answer ’acbc ’.
#
# Pay attention to the first and last element.
# 
# Instead of iterating over elements of s, you should iterate over
# indices of a (use range). This should work for arbitrary sequences of
# arbitary length. You can refer to a specific character in a string 
# using the index operation s[index]. The index of the first character is 0.
# In the above example s[0] equals ’a’ and s[3] equals ’c’.
s = 'abbcaabcaa'
#Your code starts here
result = ''
for i in range(len(s)):
    if (i==len(s) or s[i]!=s[i+1]) and (i==0 or s[i]!=s[i-1]):
        result += s[i]

# List comprehension solution: 

char_list = [s[i] for i in range(len(s)) if not ((i==0 or s[i-1] != s[i]) and (i==len(s) or s[i+1] == s[i]))]
result = "".join(char_list)
#Your code ends here
