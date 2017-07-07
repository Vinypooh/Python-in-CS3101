#Part3
#Functions, Files, and String Processing
##########################################

def indexByziptown(filename) -> (dict, dict):   # -> in function header depicts the type of return varibles
    ''' This is a very good example of how python works on dict'''  
    fo = open(filename, 'r', encoding = 'ISO-8859-1')   #be careful of the encoding issue
    zip_dict, town_dict = {}, {}
    for market in fo:
        far = market.split('\t')
        far = tuple(far)   #make farms information in tuple
        if zip_dict.get(far[4]): zip_dict[far[4]].append(far)
        else: zip_dict[far[4]] = [far]
        if town_dict.get(far[3].lower()): town_dict[far[3].lower()].add(far[4])
        else: town_dict[far[3].lower()] = {far[4]}    #make a set to eliminate farms that share common town name
    fo.close()
    return zip_dict, town_dict

def formatAddr(state, name, address, town, zipco) -> str:   #format printing using str.format function
    format_str = (
    '''
    {5}
    {0:<}
    {1:<}
    {2:<}, {3} {4:0>5}
    {5}
    ''')
    return format_str.format(name, address, town, state, zipco, '=' * 75)

if  __name__ == '__main__':
    a, b = indexByziptown('markets.tsv')
    while True:
        cmmd = input('enter a zip code or a town name: (type quit to exit) \n')
        if cmmd.lower() == 'quit': break
        if a.get(cmmd):
            for each_market in a[cmmd]:
                print(formatAddr(*each_market[:5]))
        elif b.get(cmmd.lower()):
            for each_place in b[cmmd.lower()]:
                for each_market in a[each_place]:
                    print(formatAddr(*each_market[:5]))
        else:
            print('type the wrong zipcode or town name')

