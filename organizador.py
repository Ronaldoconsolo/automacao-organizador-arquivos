import os
import shutil

# Defina a pasta que você quer organizar (Ex: sua pasta de Downloads bagunçada)
pasta_para_organizar = "./minha_pasta_baguncada"

# Dicionário mapeando os tipos de arquivos para suas respectivas pastas
formatos = {
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Documentos_PDF": [".pdf"],
    "Documentos_Texto": [".docx", ".doc", ".txt"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"]
}

def organizar_pasta(caminho):
    # Garante que a pasta existe
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"Pasta criada: {caminho}. Coloque arquivos nela para testar!")
        return

    # Varre todos os arquivos da pasta
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        
        # Ignora se for uma pasta interna
        if os.path.isdir(caminho_completo):
            continue
            
        # Pega a extensão do arquivo (.pdf, .xlsx, etc)
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        # Move o arquivo para a pasta correta baseada na extensão
        movido = False
        for pasta_destino, extensoes_validas in formatos.items():
            if extensao in extensoes_validas:
                pasta_final = os.path.join(caminho, pasta_destino)
                
                # Cria a subpasta se ela não existir
                if not os.path.exists(pasta_final):
                    os.makedirs(pasta_final)
                    
                shutil.move(caminho_completo, os.path.join(pasta_final, arquivo))
                print(f"📁 Arquivo [{arquivo}] movido para a pasta [{pasta_destino}]")
                movido = True
                break
                
        if not movido and extensao != "":
            # Cria uma pasta genérica para itens não mapeados
            pasta_outros = os.path.join(caminho, "Outros_Arquivos")
            if not os.path.exists(pasta_outros):
                os.makedirs(pasta_outros)
            shutil.move(caminho_completo, os.path.join(pasta_outros, arquivo))
            print(f"📦 Arquivo desconhecido [{arquivo}] movido para [Outros_Arquivos]")

if __name__ == "__main__":
    print("🚀 Iniciando o robô organizador de arquivos...")
    organizar_pasta(pasta_para_organizar)
    print("✨ Organização concluída com sucesso!")
