from pyspark import SparkConf, SparkContext

sc = SparkContext("local", "Simple App")
inputRDD = sc.textFile('/home/salesmind/Github/PythonSpiders/BossZhipinSpider/ghostdriver.log')
errorsRDD = inputRDD.filter(lambda x: "error" in x)
warningRDD = inputRDD.filter(lambda x: "warning" in x)
badLinesRDD = errorsRDD.union(warningRDD)
# print(badLinesRDD)
for line in badLinesRDD.take(num=10):
    print(line)