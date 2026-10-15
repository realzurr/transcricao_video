from yt_dlp import YoutubeDL

def baixar_video(url, destino=r"videos", formato="mkv"):
    """
    Baixa o vídeo do YouTube na melhor qualidade disponível (vídeo + áudio).
    - url: link do vídeo do YouTube
    - destino: pasta onde será salvo
    - formato: "mkv" (recomendado) ou "mp4"
    """
    
    # Configurações do yt-dlp
    ydl_opts = {
        # Padrão do nome do arquivo: título + id
        "outtmpl": destino + r"\%(title).200B [%(id)s].%(ext)s",

        # Melhor vídeo + melhor áudio (se não, best único)
        "format": "bestvideo*+bestaudio/best",

        # Container final
        "merge_output_format": formato,

        # Pós-processamento (usa FFmpeg)
        "postprocessors": [
            {"key": "FFmpegVideoRemuxer", "preferedformat": formato}
        ],

        # Exibir progresso
        "progress_hooks": [lambda d: print(
            f"{d.get('_percent_str','')} {d.get('status')} {d.get('filename','')}"
        )],

        # Retentativas e retomada
        "retries": 10,
        "fragment_retries": 10,
        "continuedl": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"\n✅ Download concluído! Arquivo salvo em {destino}")


# ============================
# Exemplo de uso:
# ============================

#url = "https://www.youtube.com/watch?v=U-5LnRi0n7k"  # substitua pelo link do vídeo
url = "http://url/glyunfry/147973.mp4"
baixar_video(url, destino=r"videos", formato="mkv")  # ou formato="mp4"
