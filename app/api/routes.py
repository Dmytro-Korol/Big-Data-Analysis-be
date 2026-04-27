from fastapi import APIRouter, HTTPException, status, UploadFile
from typing import List
from app.storage import minio_client as minio
from app.processing import spark_processor as spark

router = APIRouter(prefix="/api", tags=["api"])

@router.get("/", summary="Health check")
async def root():
    return {"message": "API is running"}

@router.get("/bigdata", summary="List big data items")
async def list_bigdata():
    files = minio.list_files_in_minio()
    return {"files": files}

@router.get("/bigdata/{filename}", summary="Get big data item")
async def get_bigdata(filename: str):
    file = spark.show_data_from_minio(filename)
    if file:
        return {"filename": filename, "content": file}
    else:
        raise HTTPException(status_code=404, detail="File not found")

@router.post("/bigdata", summary="Upload big data item", status_code=status.HTTP_201_CREATED)
async def upload_bigdata(file: UploadFile):
    if file and allowed_file(file.filename):
        minio.upload_file_to_minio(file.file, file.filename)
        return {"message": "Big data file uploaded successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid file type")

def allowed_file(filename):
    allowed_extensions = {'csv', 'json'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions