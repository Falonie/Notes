from pyspark import SparkConf,SparkContext

sc = SparkContext("local","Simple App")
inputRDD=sc.textFile('~/Github/PythonSpiders/BossZhipinSpider/ghostdriver.log')
errorsRDD=inputRDD.filter(lambda x:'info' in x)
print(errorsRDD)