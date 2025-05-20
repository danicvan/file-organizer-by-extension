import os
import shutil
from tkinter import Tk, filedialog
from datetime import datetime

Tk().withdraw()
print("Selecione a pasta que deseja organizar por extensão (busca recursiva):")
PASTA_BASE = filedialog.askdirectory(title="Selecione a pasta-alvo")

if not PASTA_BASE:
    print("Nenhuma pasta selecionada. Encerrando script.")
    exit()

log = []
pastas_removidas = []
data_execucao = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_PATH = os.path.join(PASTA_BASE, f"_log_extensoes_{data_execucao}.txt")

arquivos_encontrados = []
for raiz, _, arquivos in os.walk(PASTA_BASE):
    for nome in arquivos:
        caminho_absoluto = os.path.join(raiz, nome)
        if "_log_extensoes" in nome:
            continue
        arquivos_encontrados.append(caminho_absoluto)

total = len(arquivos_encontrados)
print(f"\n📦 {total} arquivos encontrados para organizar por extensão.")

for index, caminho in enumerate(arquivos_encontrados, start=1):
    nome = os.path.basename(caminho)
    extensao = os.path.splitext(nome)[1].lower().strip(".")
    extensao = extensao if extensao else "sem_extensao"

    pasta_destino = os.path.join(PASTA_BASE, extensao)
    os.makedirs(pasta_destino, exist_ok=True)

    destino_final = os.path.join(pasta_destino, nome)

    contador = 1
    while os.path.exists(destino_final):
        destino_final = os.path.join(pasta_destino, f"{os.path.splitext(nome)[0]}_{contador}.{extensao}")
        contador += 1

    try:
        shutil.move(caminho, destino_final)
        print(f"[{index}/{total}] {nome} → /{extensao}")
        log.append(f"[OK] {nome} → /{extensao}")
    except Exception as e:
        print(f"[ERRO] {nome}: {e}")
        log.append(f"[ERRO] {nome}: {e}")

print("\n🧹 Verificando e removendo pastas vazias...")
for raiz, dirs, _ in os.walk(PASTA_BASE, topdown=False):
    for d in dirs:
        caminho_pasta = os.path.join(raiz, d)
        if not os.listdir(caminho_pasta):
            try:
                os.rmdir(caminho_pasta)
                pastas_removidas.append(caminho_pasta)
                print(f"Removida: {caminho_pasta}")
            except Exception as e:
                print(f"Erro ao remover {caminho_pasta}: {e}")

log.append("\nPASTAS REMOVIDAS:")
log.extend(pastas_removidas if pastas_removidas else ["Nenhuma."])

with open(LOG_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(log))

print(f"\n✅ Organização concluída. Log salvo em: {LOG_PATH}")
