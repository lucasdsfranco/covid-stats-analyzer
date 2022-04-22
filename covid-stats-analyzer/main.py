from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("covid-stats-analyzer").getOrCreate()

data2020pt1 = spark.read.csv("./data/HIST_PAINEL_COVIDBR_2020_Parte1_06jul2021.csv")
data2020pt2 = spark.read.csv("./data/HIST_PAINEL_COVIDBR_2020_Parte2_06jul2021.csv")
data2021pt1 = spark.read.csv("./data/HIST_PAINEL_COVIDBR_2021_Parte1_06jul2021.csv")
data2021pt2 = spark.read.csv("./data/HIST_PAINEL_COVIDBR_2021_Parte2_06jul2021.csv")

spark.stop()
