import boto3
from dotenv import load_dotenv
import os

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url='http://127.0.0.1:9000',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def upload_file_to_minio(file, filename):
    try:
        s3.upload_fileobj(file, "big-data", filename)
        print(f"File {filename} uploaded to bucket 'big-data'")
    except Exception as e:
        print(f"Error uploading file: {e}")