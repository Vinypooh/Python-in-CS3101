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
#>>> x is y
#False 
#Justification for the output:
#The two lists are in different locations of memory. y is the name for the first one and x is for the second
#one. Though the value of the list is equal, x and y are pointed to different location of memory. So the output is a
#'False'
#
#
#>>> x = y
#x is y
#True
#Justification for the output:
#At this time, y also is also pointed to the second list, as variable x. Actually, y is the alias of variable x. This time
#both of the variables are pointed to the same location of the memory, so the output is a 'True'
#
#
#>>> y = y + x
#>>> x.append(y)
#>>> x == y
#False
#Justification for the output:
#expression of 'y == y + x' creates a new list named y in the memory, whereas x.append(y) add value y 
#to the original list named x. At this time, x and y have the same value of list but are pointed to 
#different location of memory. So the output is a 'False'.
#
#
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

        #ans = 0;
        #for x in a:
        #	for y in b:
        #		ans += int(x) * int(y);
        #print(ans);
    #sum_1 = [ x * y for x in a for  y in b]
    #ans = sum(sum_1)
    #print(ans)
ans = 0
for x in a:
    for y in b:
        ans += x * y
print(ans)
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
for i in range(len(s)): #using indices to access data, like a pointer
    if (i == len(s) - 1 or s[i] != s[i+1]) and (i == 0 or s[i] != s[i-1]):  #using complex logic conditon
        result += s[i]
print(result)

result = [s[i] for i in range(len(s)) if (i == 0 or s[i] != s[i-1])
                                       and (i == len(s) - 1 or s[i] != s[i+1])]
print(''.join(result))

#Your code ends here
