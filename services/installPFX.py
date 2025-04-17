import subprocess
import os

def install_pfx(cert_password):
    try:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        pfx_path = os.path.join(downloads_path, "arquivo_baixado.pfx")

        if not os.path.exists(pfx_path):
            print(f"❌ Arquivo PFX não encontrado em: {pfx_path}")
            return

        # Comando PowerShell para importar certificado no CurrentUser
        powershell_command = f"""
        $pwd = ConvertTo-SecureString "{cert_password}" -AsPlainText -Force
        Import-PfxCertificate -FilePath "{pfx_path}" -CertStoreLocation "Cert:\\CurrentUser\\My" -Password $pwd
        """

        # Executa o PowerShell
        result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Certificado instalado com sucesso no repositório do usuário!")
        else:
            print("❌ Erro ao instalar certificado:")
            print(result.stderr)
    except Exception as e:
        print(f"⚠️ Erro durante o processo: {e}")
