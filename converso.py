from PIL import Image
import os

def convert_webp_to_png(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.webp'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

            try:
                with Image.open(input_path) as img:
                    img.save(output_path, 'PNG')
                print(f"Conversão de '{filename}' concluída.")
            except Exception as e:
                print(f"Erro ao converter '{filename}': {e}")

if __name__ == "__main__":
    input_folder = "/webp"  # Substitua pelo caminho da pasta com os arquivos WebP
    output_folder = "/png"     # Substitua pelo caminho da pasta de destino para os arquivos
    convert_webp_to_png(input_folder, output_folder)