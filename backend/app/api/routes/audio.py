from fastapi import FastAPI, UploadFile, File

app = FastAPI()



@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    print("收到文件:", file.filename)

    content = await file.read()

    print("文件大小:", len(content))

    return {
        "filename": file.filename,
        "size": len(content),
    }