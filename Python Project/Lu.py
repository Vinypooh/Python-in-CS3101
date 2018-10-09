#test git
#Data extracting model from url
import xml.etree.ElementTree as ET
tree = ET.parse("http://www.careerbuilder.com/RTQ/rss20.aspx?rssid=RSS_PD&num=1000&kw=")
root = tree.getroot()
mtitle = list()


for child in root:
    for job in child.findall('item'):
        title = job.find('title').text
        mtitle.append(title)        
print(mtitle)


import re
wtitle = []
for string in mtitle:
    wtitle+=filter(None, re.split("[ -/:,()!.]+", string.lower()))
print(wtitle)



from collections import Counter
counts = Counter(wtitle)
print(counts)
print(counts.most_common(3))


