from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

load_dotenv()

spark = SparkSession.builder \
    .appName("MinIO Test") \
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262"
    ) \
    .config("spark.hadoop.fs.s3a.endpoint", "http://127.0.0.1:9000") \
    .config("spark.hadoop.fs.s3a.access.key", os.getenv("AWS_ACCESS_KEY_ID")) \
    .config("spark.hadoop.fs.s3a.secret.key", os.getenv("AWS_SECRET_ACCESS_KEY")) \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()

def show_data_from_minio(filename):
    df = spark.read.csv(f"s3a://big-data/{filename}", header=True)
    df = df.limit(30)
    
    result = df.toPandas().to_dict(orient='records')
    spark.stop()

    return result


