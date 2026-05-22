import whisper
import os

# 强制指定 ffmpeg 路径
os.environ["PATH"] = r"D:\soft\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin" + ";" + os.environ["PATH"]

# 加载模型
model = whisper.load_model("small")

# 同步函数
def transcribe_audio(file_path: str):
    result = model.transcribe(
        file_path,
        language="zh",
        fp16=False
    )
    return result["text"]