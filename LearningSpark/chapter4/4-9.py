from pyspark import SparkContext,SparkConf

# with open('/media/salesmind/Other/PycharmProjects/Despite Sanctions  South Korea Plans to Send Aid to North.txt','r') as f:
#     # print(f.readlines())
#     for line in f.readlines():
#         print(line.split(" "))

sc = SparkContext("local","4-9")
rdd=sc.textFile('/media/salesmind/Other/PycharmProjects/Despite Sanctions  South Korea Plans to Send Aid to North.txt')
words=rdd.flatMap(lambda x:x.split(" "))
result=words.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
print(result)