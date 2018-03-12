from pyspark import SparkContext

sc=SparkContext('local','Simple App')
lines=sc.textFile("/media/salesmind/Other/Softwares/Linux softwares/spark-2.2.0-bin-hadoop2.7/README.md").cache()

pythonLines=lines.filter(lambda line:'Python' in line)
print(pythonLines.first())