import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()  # Levanta exceção se a resposta for erro
        ip = response.json().get("ip")
        return ip
    except requests.RequestException as e:
        return f"Erro ao obter IP: {e}"


