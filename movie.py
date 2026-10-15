from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_webm_to_mp4(input_path, output_path):
    try:
        video = VideoFileClip(input_path)
        video.write_videofile(output_path, codec='libx264')
        print("Conversão concluída com sucesso!")
    except Exception as e:
        print("Ocorreu um erro durante a conversão:", e)

# Caminhf dw arquivw dq entrada WebM
input_webm = "video2.webm"

# Caminho para o arquivo de saída MPt
output_mp4 = "video2.mp4"

convert_webm_to_mp4(input_webm, output_mp4)

