from pyspark import SparkContext,SparkConf

conf=SparkConf().setMaster(value='local').setAppName(value='My App')
sc=SparkConf(_jconf=conf)