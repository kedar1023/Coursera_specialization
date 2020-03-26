fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for i in fh:
    if i.startswith('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'):
        	
        

print("There were", count, "lines in the file with From as the first word")
