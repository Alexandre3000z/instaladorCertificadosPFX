import gdown
import os


def download_pfx(url):
    try:
        # Extrai o ID do link
        file_id = url.split("/d/")[1].split("/")[0]
        download_url = f"https://drive.google.com/uc?id={file_id}"

        # Caminho padrão para a pasta Downloads
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        output = os.path.join(downloads_path, "arquivo_baixado.pfx")

        # Faz o download
        gdown.download(download_url, output, quiet=False)
        print(f"Arquivo salvo em: {output}")
    except Exception as e:
        print(f"Erro ao baixar: {e}")


