from pyspark.sql import SparkSession
import sys

spark = SparkSession.builder\
    .appName("Read_ANEEL")\
    .config("spark.jars","gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.23.2.jar")\
    .config("spark.files.fetchTimeout", "10m")\
    .getOrCreate()

csv_name = sys.argv[1]
table = sys.argv[2]

bucket_file = f"gs://lemon-project-393220-csv-files/{csv_name}"

df = spark.read.csv(bucket_file, header=True
                    , sep=";", encoding='iso-8859-1'
                    , inferSchema=True)

df.printSchema()

df.write\
    .format("bigquery")\
    .mode('overwrite')\
    .option('enableModeCheckForSchemaFields', False)\
    .option("writeMethod", "direct")\
    .option("table", table)\
    .save()
