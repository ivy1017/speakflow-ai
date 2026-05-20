"use client";

import { useRef, useState } from "react";

export default function Recorder() {
  const [isRecording, setIsRecording] = useState(false);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const startRecording = async () => {
    // 获取麦克风权限并开始录音
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true,
    });

    const mediaRecorder = new MediaRecorder(stream);

    mediaRecorderRef.current = mediaRecorder;

    chunksRef.current = [];

    mediaRecorder.ondataavailable = (event) => {
      chunksRef.current.push(event.data);
    };

    // 录音结束调用后端接口上传音频
    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(chunksRef.current, {
        type: "audio/webm",
      });

      // 本地播放
      const audioUrl = URL.createObjectURL(audioBlob);

      const audio = new Audio(audioUrl);

      audio.play();

      // 上传到 FastAPI 后端
      const formData = new FormData();

      formData.append("file", audioBlob, "recording.webm");

      const response = await fetch("http://127.0.0.1:8000/upload-audio", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      console.log("上传结果:", data);
    };

    mediaRecorder.start();

    setIsRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current?.stop();

    setIsRecording(false);
  };

  return (
    <div className="flex flex-col items-center gap-4">
      <button
        onClick={isRecording ? stopRecording : startRecording}
        className="rounded-xl bg-black px-6 py-3 text-white"
      >
        {isRecording ? "停止录音" : "开始录音"}
      </button>
    </div>
  );
}
