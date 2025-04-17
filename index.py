from services.ipValidator import get_public_ip
from services.downloadPFX import download_pfx
from services.installPFX import install_pfx
from services.sheetReader import read_google_sheets
from dotenv import load_dotenv
import os

# Carregando os dados referente ao IP FIXO DESEJADO
load_dotenv()
FIXED_IP = os.getenv("FIXED_IP")

# Validando se o colaborador está na empresa
if FIXED_IP == get_public_ip():

    url = "https://drive.google.com/file/d/1p8_nr7K0vsiuWqLXkNYinLwuGl4EWhoF/view?usp=sharing"
    urlSheets = "https://docs.google.com/spreadsheets/d/1uaQCpft_pyLkOYkpT48ZQgoMvXwBwlXcn9AKxDMBgH8/edit?usp=sharing"
    # download_pfx(url)
    # install_pfx("123456")
    df = read_google_sheets(urlSheets)
    print(df)
else:
    print("Você não está na sua organização, falar com TI!")
