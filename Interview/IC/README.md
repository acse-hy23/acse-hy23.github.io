# 求取平均数

在基于类的实现方法中，我们定义了一个Goods类来表示商品数据，使用类的实例来保存商品数据，并使用类的方法来计算平均值。这种方法使代码更加模块化和易于理解。

而基于字典的实现方法则更加直接和简单，但它可能难以扩展和修改，因为它将所有的数据和计算都放在一个字典中。

从性能方面来看，两种实现方法的效率应该是相似的。这是因为它们都遍历了相同的文件内容，并将数据存储在类实例或字典中，然后进行相同的计算。因此，性能的差异应该很小。

在数据量为百万级的情况下，基于类的实现方法会消耗额外的大约30%的时间。

```
num_lines = 1000000
[Done] exited with code=0 in 0.946 seconds //dict
[Done] exited with code=0 in 1.178 seconds //class
num_lines = 10000000
[Done] exited with code=0 in 8.337 seconds //dict
[Done] exited with code=0 in 11.239 seconds //class
```

