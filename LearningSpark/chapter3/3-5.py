from pyspark import SparkConf,SparkContext

logFile = "/media/salesmind/Other/Softwares/Linux softwares/spark-2.2.0-bin-hadoop2.7/README.md"
sc = SparkContext("local","Simple App")
lines=sc.parallelize(['pandas','i like pandas'])
print(lines)