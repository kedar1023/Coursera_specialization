import json
import urllib.request
count = 0
url = "http://py4e-data.dr-chuck.net/comments_384111.json"
print( "retrieving URL. Stand by.")
with urllib.request.urlopen(url) as uh:
    data= uh.read()

    info = json.loads(data)
    for item in info["comments"]:
	#print item["count"]
	    number = int(item["count"])
	    count = count + number
    print (count)
# import urllib.request

# with urllib.request.urlopen("http://www.python.org") as url:
#     s = url.read()
#     # I'm guessing this would output the html source code ?
#     print(s)
