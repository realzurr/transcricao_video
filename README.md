# Conversor de Mídias

Este repositório reúne scripts em Python para manipular imagens, vídeos, áudio e PDFs de forma prática.

## Funcionalidades

- Conversão de arquivos EPS para PNG
- Conversão de vídeos em MP3
- Conversão de PDF em sequência de imagens e depois em vídeo
- Download de vídeos do YouTube
- Geração de legendas SRT a partir de vídeos usando Whisper
- Processamento de arquivos de mídia em pastas organizadas

## Estrutura do projeto

- `converte_imagens.py` — converte arquivo EPS para PNG
- `convert_mp4_mp3.py` — converte vídeo MP4 para MP3
- `convert_pdf_mp4.py` — transforma PDF em vídeo
- `downVideo.py` — baixa vídeos do YouTube
- `transcricao_videos.py` — extrai áudio e gera legenda em SRT
- `transcricao_videos_gui.py` — versão com interface gráfica
- `png/` e `webp/` — pastas de saída para imagens

## Requisitos

- Python 3.10+
- FFmpeg instalado e acessível no PATH
- Bibliotecas Python:

```bash
pip install matplotlib moviepy pdf2image yt-dlp openai-whisper
```

## Configuração do ambiente

1. Crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Copie o arquivo de exemplo para o ambiente local:

```bash
cp .env.example .env
```

3. Ajuste os valores em `.env` conforme o projeto e a máquina local.

## Execução

### Converter EPS para PNG

```bash
python converte_imagens.py
```

### Converter MP4 para MP3

```bash
python convert_mp4_mp3.py
```

### Download de vídeo

```bash
python downVideo.py
```

### Gerar legendas de vídeo

```bash
python transcricao_videos.py
```

> Importante: a pasta `videos` deve existir antes de executar a transcrição.

## Variáveis de ambiente

O arquivo `.env` pode ser usado para configurar caminhos e parâmetros gerais do projeto, como:

- pasta de entrada de vídeo
- pasta de saída
- formato de download
- nome do modelo de transcrição

## Observações

- Os arquivos gerados por conversão e download podem ser grandes e não devem ser enviados para o Git.
- O projeto foi montado para uso local e estudo de automação de mídia.

## Licença

Este projeto é destinado ao uso pessoal e educacional.
