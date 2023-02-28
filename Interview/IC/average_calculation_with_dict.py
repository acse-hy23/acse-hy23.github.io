# file = open('test.txt', 'r')
# res = file.readlines()

# allGoods = dict()

# for line in res:
#     line = line.replace(" ","").replace("\n","")
#     line = line.split(",")
#     if(allGoods.get(line[2])==None):
#         allGoods[line[2]] = {"sumM": 0,"count": 0}
#     allGoods[line[2]]["sumM"]+=int(line[1])
#     allGoods[line[2]]["count"]+=float(line[0])

# for i in allGoods:
#     print(i, allGoods[i]["sumM"]/allGoods[i]["count"])

# Below is the optimized code
with open('test.txt', 'r') as file:
    allGoods = {}
    for line in file:
        line = line.strip().split(',')
        goods_name = line[2]
        price = int(line[1])
        count = int(line[0])
        if goods_name not in allGoods:
            allGoods[goods_name] = {"sum_price": price, "count": count}
        else:
            allGoods[goods_name]["sum_price"] += price
            allGoods[goods_name]["count"] += count

    for goods_name, data in allGoods.items():
        print(goods_name, data["sum_price"]/data["count"])
