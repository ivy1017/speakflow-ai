from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from app.services.whisper_service import transcribe_audio
from app.services.chat_service import generate_reply

router = APIRouter()


@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    # 保存临时文件
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".webm"
    ) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Whisper 识别
    text = transcribe_audio(tmp_path)

    # 删除临时文件
    os.unlink(tmp_path)

    # AI 回复
    reply = generate_reply(text)

    return {
        "text": text,
        "reply": reply
    }