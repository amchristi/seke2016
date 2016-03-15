import sys

infile = sys.argv[1]

instart = infile.split(".")[0]

outbefore = open(instart + ".before.data",'w')
outafter = open(instart + ".after.data",'w')

bugs = []
bugData = {}

scores = ["Tarantula", "Ochaia", "Jaccard", "SBI", "Ample"]

fields = []

for l in open(infile):
    ls = l.split(",")
    if ls[0] == "":
        ls[0] = "Bug#"
        for f in ls:
            f = f.replace("Jacard","Jaccard")
            fields.append(f.replace("\r\n",""))
        continue
    if ls[1] == "":
        continue
    b = {}
    pos = 0
    for f in fields:
        b[f] = ls[pos].replace("\r\n","")
        pos += 1
    bugs.append((b["Bug#"]))
    bugData[(b["Bug#"])] = b

bugs = sorted(bugs)

print bugs

pos = 0
for b in bugs:
    pos += 1
    for s in scores:
        outbefore.write(str(pos) + " " + str(bugData[b][s+ "Full"]) + "\n")
        outafter.write(str(pos) + " " + str(bugData[b][s+"Reduced"]) + "\n")
        pos += 1

outbefore.close()
outafter.close()
