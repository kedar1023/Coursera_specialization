# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

fin=fh.read()
fin=fin.rstrip()
for i in fin:
    print(i.upper())
