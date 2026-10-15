from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file)
    audio_clip.close()

if __name__ == "__main__":
    input_file = "musica.mp4"  # Substitua pelo nome do seu arquivo .mp4
    output_file = "musica.mp3"  # Nome do arquivo de saída .mp3

    convert_mp4_to_mp3(input_file, output_file)
