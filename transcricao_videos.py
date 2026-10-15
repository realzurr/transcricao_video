import os
import subprocess
import whisper

def extract_audio(video_path, audio_path="temp_audio2.wav"):
    """Extrai o áudio do vídeo usando FFmpeg."""
    cmd = [
        "ffmpeg",
        "-y",  # sobrescreve arquivo
        "-i", video_path,
        "-vn",  # remove vídeo
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        audio_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return audio_path

def generate_subtitles(video_path, model_name="base"):
    """Gera legendas para um vídeo."""
    audio_path = extract_audio(video_path)
    
    print(f"[INFO] Transcrevendo: {video_path}")
    model = whisper.load_model(model_name)  # modelos: tiny, base, small, medium, large
    result = model.transcribe(audio_path)

    # Cria o arquivo SRT
    srt_path = os.path.splitext(video_path)[0] + ".srt"
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result['segments'], start=1):
            start = segment['start']
            end = segment['end']
            text = segment['text'].strip()

            f.write(f"{i}\n")
            f.write(f"{format_srt_time(start)} --> {format_srt_time(end)}\n")
            f.write(f"{text}\n\n")

    os.remove(audio_path)
    print(f"[OK] Legenda gerada: {srt_path}")


def format_srt_time(seconds):
    """Converte segundos em formato SRT (hh:mm:ss,ms)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


# Exemplo de uso:
if __name__ == "__main__":
    pasta = "videos"  # pasta onde estão os vídeos
    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith((".mp4", ".mkv", ".mov", ".avi")):
            caminho_video = os.path.join(pasta, arquivo)
            generate_subtitles(caminho_video, model_name="small")
