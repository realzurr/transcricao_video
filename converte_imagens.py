import matplotlib.pyplot as plt

# Caminho para o arquivo EPS
caminho_arquivo_eps = 'imagem.eps'

# Carregar o arquivo EPS usando o matplotlib
img = plt.imread(caminho_arquivo_eps)

# Caminho para salvar o arquivo PNG
caminho_arquivo_png = 'imagem.png'

# Salvar a imagem como PNG
plt.imsave(caminho_arquivo_png, img)
