from fastapi import APIRouter, HTTPException, status, UploadFile
from typing import List
from app.storage import minio_client as minio

router = APIRouter(prefix="/api", tags=["api"])

@router.get("/", summary="Health check")
async def root():
    return {"message": "API is running"}

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