def load_markets(filename):
    """
    Load in a TSV file containing farmers markets in the US.
    """

    zip_to_markets = {}
    towns_to_zip = {}

    tsv_file = open(filename,'r', encoding="ISO-8859-1")
    for line in tsv_file:
        parts = line.strip().split("\t") # Split of line termination symbol,
                                         # split at tabs

        # No check if we have enough cells per row
        if len(parts) == 7: 
            state, name, address, town, zip_code, longitude, latitude = parts
            if not zip_code in zip_to_markets: 
                zip_to_markets[zip_code] = [] 
            zip_to_markets[zip_code].append((state,name, address, town, 
                                             zip_code, longitude, latitude))   
            if not town in towns_to_zip: 
                towns_to_zip[town] = set()
            towns_to_zip[town].add(zip_code)   
        else: 
            print("Invalid row format {0}".format(line))

    return zip_to_markets, towns_to_zip


def format_market(state, name, address, town, zip_code):
    return "{name}\n{address}\n{town}, {state} {zip_code}".format(name=name,
                   address=address, town=town, state=state, zip_code=zip_code)


def print_markets_for_zip(zip_code):
    if zip_code in zip_to_markets: 
        for state, name, address, town, zip_code,longitute, latitude in zip_to_markets[zip_code]:
            print(format_market(state,name, address, town, zip_code))
            print()
    else:     
            print("No markets found in this zip code.")


zip_to_markets, towns_to_zip = load_markets("markets.tsv")

while True:
    query = input()
    if query == "quit":
        break
    if query.isdigit(): # this is a zip code
        print_markets_for_zip(query)
    else: #assume this is a town
        if query in towns_to_zip:  
            for zip_code in towns_to_zip[query]: 
                print_markets_for_zip(zip_code)

                
