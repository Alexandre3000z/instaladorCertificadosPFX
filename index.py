from services.ipValidator import get_public_ip
from services.downloadPFX import download_pfx
from services.installPFX import install_pfx
from dotenv import load_dotenv
import os

# Carregando os dados referente ao IP FIXO DESEJADO
load_dotenv()
FIXED_IP = os.getenv("FIXED_IP")

# Validando se o colaborador está na empresa
if FIXED_IP == get_public_ip():

    url = "https://drive.google.com/file/d/1p8_nr7K0vsiuWqLXkNYinLwuGl4EWhoF/view?usp=sharing"
    download_pfx(url)
    install_pfx("123456")

else:
    print("Você não está na sua organização, falar com TI!")
