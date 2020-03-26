import json
import xml.etree.ElementTree as ET

import urllib.request
count = 0
url = "http://py4e-data.dr-chuck.net/comments_384110.xml"
print( "retrieving URL. Stand by.")
with urllib.request.urlopen(url) as uh:
    data= uh.read()
    total=0
    print(data.decode())
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    print('Comment count:', len(lst))
    for item in lst:
        print('Name', item.find('name').text)
        total=total+int(item.find('count').text)
        print('Count', item.find('count').text)
    print('Total',total)
    

    
# import urllib.request

# with urllib.request.urlopen("http://www.python.org") as url:
#     s = url.read()
#     # I'm guessing this would output the html source code ?
#     print(s)
