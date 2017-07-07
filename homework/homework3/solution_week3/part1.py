nlist = [1, [2, [3, [4, 5]]], [6, [7, [8, [9]], 10]]]

# Part 1a
def print_nlist(nlist, indentation = 1):
    for element in nlist:
        if type(element) == list:
            print_nlist(element, indentation + 4)
        else:
            print("{0}{1}".format(indentation * ".", element))

print_nlist(nlist)

# Part 1b

def map_nlist(nlist, fun):
    res = []
    for element in nlist:
        if type(element) == list:
            res.append(map_nlist(element, fun))
        else:
            res.append(fun(element))
    return res
mapped = map_nlist(nlist, lambda a: a*2)
print(nlist)
print(mapped)

# Part 1c
def combine_nlist(nlist, init, fun):

    res = init
    for element in nlist:
        if type(element) == list:
            res = fun(res, combine_nlist(element,init, fun))
        else:
            res = fun(res, element)
    return res

combined = combine_nlist(nlist, 0, lambda a,b: a+b)
print(combined)

# Part 1d
def flatten(nlist):
    return combine_nlist(nlist, [], lambda x,y: x+ (y if type(y)==list else [y]))

print(flatten(nlist))
