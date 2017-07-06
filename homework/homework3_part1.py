#Homework3
#using functional programming knowledge
#two parts total
##########################################################

#part1: Functional Programming

#test list
nlist = [1, [2, [3, [4, 5]]], [6, [7, [8, [9]], 10]]]
s = 'the quick red fox jumps over the lazy brown dog'

#Printing Nested Lists:
#this function can only process list type as isn't a good example for polymorphism.
def print_nlist(nlist: 'list', count = 1): 
    sepimg = '.'
    for ea_node in nlist:
        n = count   #reset count to default value of that layer
        if type(ea_node) is list:   #not for polymorphism
            n += 4
            print_nlist(ea_node, n) #pass parameter among nested function
        else:
            print("%s%s" % (sepimg * n, ea_node))

#Mapping Nested Lists:
def map_nlist(nlist: 'list', fun):
    count = 0
    for ea_node in nlist:
        if isinstance(ea_node, list):
            map_nlist(ea_node, fun)
        else:
            nlist[count] = fun(ea_node)     #perform in-place change
        count += 1
    return nlist

#Combining Nested Lists:
def combine_nlist(nlist, init = 0, combiner):
    res = init
    for ea_node in nlist:
        if isinstance(ea_node, list):
            res = combine_nlist(ea_node, res, combiner)
        else:
            res = combiner(res, ea_node)
    return res

#Flattening Nested Lists:
def flatten_nlist(nlist):
    return combine_nlist(nlist, [], lambda x,y: x + [y])

#part2: Generator
def ngrams(n: 'the length of sequence s', s: 'a list of words'):
    if len(s) < n:
        yield s
    while len(s) >= n:
        yield s[:n]
        s = s[1:]

if __name__ == '__main__':
    from copy import deepcopy as dcp
    print_nlist(nlist)
    cnlist = dcp(nlist)
    print(map_nlist(cnlist, lambda x: x*2))
    print(nlist)
    print(combine_nlist(nlist, lambda x,y: x + y))
    print(flatten_nlist(nlist))
    for x in ngrams(5, s.split(' ')):
        print(x)
