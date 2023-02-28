# file = open('test.txt', 'r')
# res = file.readlines()

# class Goods():
#     sumMoney = 0
#     count = 0
#     def addData(self, money,amount):
#         self.sumMoney+=float(money)
#         self.count+=int(amount)
#     def getAverage(self):
#         return self.sumMoney/self.count

# allGoods = dict()

# for line in res:
#     line = line.replace(" ","").replace("\n","")
#     line = line.split(",")
#     if(allGoods.get(line[2])==None):
#         allGoods[line[2]] = Goods()
#     goods = allGoods.get(line[2])
#     goods.addData(line[1],line[0])

# for i in allGoods:
#     print(i, allGoods[i].getAverage())

# Below is the optimized code
class Goods():
    def __init__(self):
        self.sum_money = 0
        self.count = 0

    def add_data(self, money, amount):
        self.sum_money += float(money)
        self.count += int(amount)

    def get_average(self):
        return self.sum_money / self.count

all_goods = {}

with open('test.txt', 'r') as file:
    for line in file:
        line = line.strip().split(',')
        goods_name, money, amount = line[2], line[1], line[0]
        goods = all_goods.setdefault(goods_name, Goods())
        goods.add_data(money, amount)

for goods_name, goods in all_goods.items():
    print(goods_name, goods.get_average())
