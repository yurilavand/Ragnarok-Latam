import tkinter as tk
from tkinter import ttk
import os

# ==========================
# RECEITAS DE SEMIJOIAS
# ==========================

semijoias = {
    "Inferior de Arma": {"Sombridecon": 1, "Zeny": 10000},
    "Inferior de Armadura": {"Sombridecon": 1, "Zeny": 10000},
    "Inferior de Acessório": {"Sombridecon": 1, "Zeny": 10000},

    "Comum de Arma": {"Semijoia Inferior de Arma": 3, "Zeny": 10000},
    "Comum de Armadura": {"Semijoia Inferior de Armadura": 3, "Zeny": 10000},
    "Comum de Acessório": {"Semijoia Inferior de Acessório": 3, "Zeny": 10000},

    "Incomum de Arma": {"Semijoia Comum de Arma": 3, "Zeny": 20000},
    "Incomum de Armadura": {"Semijoia Comum de Armadura": 3, "Zeny": 20000},
    "Incomum de Acessório": {"Semijoia Comum de Acessório": 3, "Zeny": 20000},

    "Superior de Arma": {"Semijoia Incomum de Arma": 3, "Zeny": 50000},
    "Superior de Armadura": {"Semijoia Incomum de Armadura": 3, "Zeny": 50000},
    "Superior de Acessório": {"Semijoia Incomum de Acessório": 3, "Zeny": 50000},
}

# ==========================
# JANELA
# ==========================

janela = tk.Tk()
janela.title("Calculadora de Semijoias Ragnarok LATAM")
janela.geometry("700x600")

tk.Label(janela, text="Tipo de Semijoia").pack()

combo = ttk.Combobox(
    janela,
    values=list(semijoias.keys()),
    width=50
)
combo.pack()
combo.current(0)

tk.Label(janela, text="Quantidade para criar").pack()

quantidade = tk.Entry(janela)
quantidade.insert(0, "1")
quantidade.pack()

texto = tk.Text(janela, width=70, height=25)
texto.pack(pady=10)

def gerar_relatorio(item, qtd):
    relatorio = []
    relatorio.append(f"Produção: {qtd}x {item}")
    relatorio.append("-"*45)

    if "Inferior" in item:
        sombridecons = qtd
        minerios = sombridecons * 5
        zeny = qtd * semijoias[item]["Zeny"]

        relatorio += [
            f"Minérios de Sombridecon: {minerios}",
            f"Sombridecons: {sombridecons}",
            f"Zeny: {zeny:,}"
        ]

    elif "Comum" in item:
        inferiores = qtd * 3
        sombridecons = inferiores
        minerios = sombridecons * 5
        zeny = qtd * semijoias[item]["Zeny"] + inferiores * 10000

        relatorio += [
            f"Minérios de Sombridecon: {minerios}",
            f"Sombridecons: {sombridecons}",
            f"Semijoias Inferiores: {inferiores}",
            f"Zeny: {zeny:,}"
        ]

    elif "Incomum" in item:
        comuns = qtd * 3
        inferiores = comuns * 3
        sombridecons = inferiores
        minerios = sombridecons * 5
        zeny = qtd * semijoias[item]["Zeny"] + comuns * 10000 + inferiores * 10000

        relatorio += [
            f"Minérios de Sombridecon: {minerios}",
            f"Sombridecons: {sombridecons}",
            f"Semijoias Inferiores: {inferiores}",
            f"Semijoias Comuns: {comuns}",
            f"Zeny: {zeny:,}"
        ]

    elif "Superior" in item:
        incomuns = qtd * 3
        comuns = incomuns * 3
        inferiores = comuns * 3
        sombridecons = inferiores
        minerios = sombridecons * 5
        zeny = qtd * semijoias[item]["Zeny"] + incomuns * 20000 + comuns * 10000 + inferiores * 10000

        relatorio += [
            f"Minérios de Sombridecon: {minerios}",
            f"Sombridecons: {sombridecons}",
            f"Semijoias Inferiores: {inferiores}",
            f"Semijoias Comuns: {comuns}",
            f"Semijoias Incomuns: {incomuns}",
            f"Zeny: {zeny:,}"
        ]

    return "\n".join(relatorio)

def calcular():
    texto.delete("1.0", tk.END)
    item = combo.get()

    try:
        qtd = int(quantidade.get())
    except:
        qtd = 1

    relatorio = gerar_relatorio(item, qtd)
    texto.insert(tk.END, relatorio)

    # Exportação automática
    nome_arquivo = f"Relatorio_{item.replace(' ', '_')}_{qtd}.txt"
    caminho = os.path.join(os.getcwd(), nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(relatorio)

    texto.insert(tk.END, f"\n\nRelatório salvo em: {caminho}")

ttk.Button(
    janela,
    text="Calcular e Exportar",
    command=calcular
).pack(pady=10)

calcular()

janela.mainloop()
