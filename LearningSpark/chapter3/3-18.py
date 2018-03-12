from pyspark import SparkConf, SparkContext

sc = SparkContext("local", "Simple App")
inputRDD = sc.textFile('/home/salesmind/Github/PythonSpiders/BossZhipinSpider/ghostdriver.log')