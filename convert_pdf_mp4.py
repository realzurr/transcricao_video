import os
from pdf2image import convert_from_path
from moviepy.editor import ImageSequenceClip

def pdf_to_images(pdf_path, interval):
    # Conversão de cada página do PDF para uma imagem
    images = convert_from_path(pdf_path, dpi=300)

    # Criação de uma pasta temporária para armazenar as imagens
    temp_folder = 'temp_images'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    # Salvando as imagens no diretório temporário
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(temp_folder, f"page_{i}.jpg")
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)

    # Criação do arquivo de vídeo
    clip = ImageSequenceClip(image_paths, fps=1/interval)
    clip.write_videofile('output.mp4')

    # Limpeza da pasta temporária
    for image_path in image_paths:
        os.remove(image_path)
    os.rmdir(temp_folder)

# Chame a função com o intervalo desejado (em segundos)
pdf_to_images('opudim_delicia.pdf', interval=5)
