from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 添加跨域中间件，允许来自前端 http://localhost:3000 的请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "SpeakFlow AI Backend"}


@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    print("收到文件:", file.filename)

    content = await file.read()

    print("文件大小:", len(content))

    return {
        "filename": file.filename,
        "size": len(content),
    }