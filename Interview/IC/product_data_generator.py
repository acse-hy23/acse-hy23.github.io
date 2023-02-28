import random

# 指定要生成的文件名和行数
filename = "test.txt"
num_lines = 1000000

# 定义商品名称列表
product_names = ["apple", "orange", "banana", "pear", "grape", "watermelon"]

# 打开文件并写入数据
with open(filename, 'w') as f:
    for i in range(num_lines):
        # 生成三个随机值
        val1 = random.randint(1, 5) # amount
        val2 = random.randint(5, 20) # money
        val3 = random.choice(product_names) # product name
        
        # 将随机值写入文件
        f.write("{}, {}, {}\n".format(val1, val2, val3))
