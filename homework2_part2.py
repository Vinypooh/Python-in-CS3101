#Part3
#Functions, Files, and String Processing
##########################################

def indexByziptown(filename):
    fo = open(filename, 'r', encoding = 'ISO-8859-1')   #be careful of the encoding issue
    zip_index_dict, town_index_dict = {}, {}
    for market in fo:
        tmpl = market.split('\t')
        farm_tuple = tuple(tmpl)
        if zip_index_dict.get(farm_tuple[4]): zip_index_dict[farm_tuple[4]].append(farm_tuple)
        else: zip_index_dict[farm_tuple[4]] = [farm_tuple]
        if town_index_dict.get(farm_tuple[3].lower()): town_index_dict[farm_tuple[3].lower()].add(farm_tuple[4])
        else: town_index_dict[farm_tuple[3].lower()] = {farm_tuple[4]}
    fo.close()
    return zip_index_dict, town_index_dict

def formatAddr(state, name, address, town, zipco):
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

