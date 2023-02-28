file = open('test.txt', 'r')
res = file.readlines()

allGoods = dict()

for line in res:
    line = line.replace(" ","").replace("\n","")
    line = line.split(",")
    if(allGoods.get(line[2])==None):
        allGoods[line[2]] = {"sumM": 0,"count": 0}
    allGoods[line[2]]["sumM"]+=int(line[1])
    allGoods[line[2]]["count"]+=float(line[0])

for i in allGoods:
    print(i, allGoods[i]["sumM"]/allGoods[i]["count"])

    