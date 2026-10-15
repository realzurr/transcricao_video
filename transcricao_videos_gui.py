import os
import subprocess
import whisper
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_audio(video_path, audio_path="temp_audio.wav"):
    """Extrai o áudio do vídeo usando FFmpeg."""
    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        audio_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return audio_path

def format_srt_time(seconds):
    """Converte segundos em formato SRT (hh:mm:ss,ms)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def generate_subtitles(video_path, model_name="small"):
    """Gera legendas para um vídeo."""
    audio_path = extract_audio(video_path)
    
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)

    srt_path = os.path.splitext(video_path)[0] + ".srt"
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result['segments'], start=1):
            f.write(f"{i}\n")
            f.write(f"{format_srt_time(segment['start'])} --> {format_srt_time(segment['end'])}\n")
            f.write(f"{segment['text'].strip()}\n\n")

    os.remove(audio_path)
    return srt_path

def select_videos():
    """Abre o seletor de arquivos e processa os vídeos."""
    files = filedialog.askopenfilenames(
        title="Selecione os vídeos",
        filetypes=[("Arquivos de vídeo", "*.mp4 *.mkv *.mov *.avi")]
    )
    if files:
        for video in files:
            try:
                output = generate_subtitles(video)
                messagebox.showinfo("Sucesso", f"Legenda gerada: {output}")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao processar {video}.\nErro: {e}")

# Interface gráfica
root = tk.Tk()
root.title("Gerador de Legendas Automáticas")
root.geometry("400x200")

label = tk.Label(root, text="Clique no botão para selecionar os vídeos", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="Selecionar Vídeos", font=("Arial", 12), command=select_videos)
btn.pack(pady=20)

root.mainloop()
