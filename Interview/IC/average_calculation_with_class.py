file = open('test.txt', 'r')
res = file.readlines()

class Goods():
    sumMoney = 0
    count = 0
    def addData(self, money,amount):
        self.sumMoney+=float(money)
        self.count+=int(amount)
    def getAverage(self):
        return self.sumMoney/self.count

allGoods = dict()

for line in res:
    line = line.replace(" ","").replace("\n","")
    line = line.split(",")
    if(allGoods.get(line[2])==None):
        allGoods[line[2]] = Goods()
    goods = allGoods.get(line[2])
    goods.addData(line[1],line[0])

for i in allGoods:
    print(i, allGoods[i].getAverage())
