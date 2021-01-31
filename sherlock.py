lst1, dct1 = [], {}
fhand = open("ipaddress.txt")
for line in fhand:
    pos1 = line.find("M,") #start index for extracting the ip address
    pos2 = line.find(",", pos1+2) #end index for extracting the ip address
    lst1.append(line[pos1+2 : pos2])

    pos1 = line.find("(") #start index for extracting the machine used
    pos2 = line.find(";", pos1+2) #end index for extracting the machine used
    dct1[line[pos1+1 : pos2]] = dct1.get(line[pos1+1 : pos2], 0) + 1

print(*lst1, sep="\n", end="\n\n\n")
print("Number of unique IP Addresses used : ", len(set(lst1)), end="\n\n\n")
print(*dct1.items(), sep="\n", end="\n\n\n")
print("Times accessed from an iPad :", dct1["iPad"])
