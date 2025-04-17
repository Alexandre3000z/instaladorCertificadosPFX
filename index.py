from services.ipValidator import get_public_ip
import os
from dotenv import load_dotenv

# Verificação de local empresa.

    # Carrega as variáveis do .env
load_dotenv()
    # Dados sendo puxado da .env IP FIXO
FIXED_IP = os.getenv("FIXED_IP")

if FIXED_IP == get_public_ip():
    print("Você está na office")

    


else:
    print("Você não está na office!")



