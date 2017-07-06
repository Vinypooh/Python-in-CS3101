#Part 2
s = "the quick red fox jumps over the lazy brown dog"

def ngrams(n, s): 
    for i in range(len(s)-n+1):
        yield s[i:i+n]

for element in ngrams(3, s.split()):
    print(element)

