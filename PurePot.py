import tkinter as tk
from tkinter import ttk

# ==========================
# RECEITAS
# ==========================

receitas = {
    "Garrafa de Veneno": {
        "Garrafa Vazia": 1,
        "Esporo Venenoso": 1,
        "Espinho de Cacto": 1,
        "Ferrão de Abelha": 1,
        "Karvodailnirol": 1,
        "Poção de Fúria Selvagem": 1,

    },
    "Poção Branca Especial": {
        "Tubo de Ensaio": 10,
        "Poção Branca": 20,
        "Erva Branca": 10,
        "Álcool": 1,
        },

    "Poção Vitata 500": {
        "Tubo de Ensaio": 10,
        "Uva": 10,
        "Mel": 10,
        "Erva Azul": 10
    },

    "Suco Celular Enriquecido": {
        "Tubo de Ensaio": 10,
        "Molho Picante": 5,
        "Poção do Despertar": 5,
        "Poção da Concentração": 5
    },

    "Poção de Recuperação": {
        "Tubo de Ensaio": 10,
        "Folha de Yggdrasil": 1,
        "Erva Verde": 20,
        "Mastela": 1,
        "Panaceia": 5
    },

    "Elixir Vermelho": {
        "Garrafa Vazia": 10,
        "Garrafa de Poção": 5,
        "Xarope Vermelho": 15
    },

    "Elixir Azul": {
        "Garrafa Vazia": 10,
        "Garrafa de Poção": 5,
        "Xarope Azul": 15
    },

    "Elixir Dourado": {
        "Garrafa Vazia": 10,
        "Garrafa de Poção": 5,
        "Xarope Branco": 10,
        "Xarope Amarelo": 10
    },

    "Poção X": {
        "Tubo de Ensaio": 10,
        "Fruto de Yggdrasil": 10,
        "Ouro": 5
    },

    "Energético Físico": {
        "Tubo de Ensaio": 10,
        "Erva Vermelha": 45,
        "Semente de Yggdrasil": 5
    },

    "Energético Mágico": {
        "Tubo de Ensaio": 10,
        "Erva Azul": 15,
        "Semente de Yggdrasil": 5
    },

    "Semente de Planta Selvagem": {
        "Fruta Espinhosa": 10
    },

    "Semente de Planta Sanguessuga": {
        "Raiz de Planta Carnívora": 10
    },

    "Esporo de Cogumelo Explosivo": {
        "Esporo": 10,
        "Esporo Venenoso": 5,
        "Mistura de Pólvora": 2
    },

    "Poção Pequena HP": {
        "Garrafa Vazia": 10,
        "Erva Branca": 10,
        "Molho Picante": 1,
        "Ração para Monstros": 5
    },

    "Poção Média HP": {
        "Garrafa Vazia": 10,
        "Erva Branca": 10,
        "Erva Amarela": 10,
        "Molho Picante": 1
    },

    "Poção Grande HP": {
        "Garrafa Vazia": 10,
        "Erva Branca": 15,
        "Mastela": 3,
        "Água Benta": 1,
        "Molho Picante": 1
    },

    "Poção Pequena SP": {
        "Garrafa Vazia": 10,
        "Limão": 10,
        "Uva": 10,
        "Molho Doce": 1
    },

    "Poção Média SP": {
        "Garrafa Vazia": 10,
        "Mel": 10,
        "Erva Azul": 10,
        "Molho Doce": 1
    },

    "Poção Grande SP": {
        "Garrafa Vazia": 10,
        "Geleia Real": 10,
        "Erva Azul": 15,
        "Molho Doce": 1
    }
}

# ==========================
# JANELA
# ==========================

janela = tk.Tk()
janela.title("Calculadora de Farmacologia")
janela.geometry("700x600")

tk.Label(janela, text="Poção").pack()

combo = ttk.Combobox(
    janela,
    values=list(receitas.keys()),
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

def calcular():

    texto.delete("1.0", tk.END)

    pocao = combo.get()

    try:
        qtd = int(quantidade.get())
    except:
        qtd = 1

    texto.insert(tk.END, f"Produção: {qtd}x {pocao}\n")
    texto.insert(tk.END, "-"*45 + "\n\n")

    total = {}

    for item, valor in receitas[pocao].items():
        total[item] = valor * qtd

    for item in sorted(total):
        texto.insert(
            tk.END,
            f"{item:<30} {total[item]}\n"
        )

ttk.Button(
    janela,
    text="Calcular",
    command=calcular
).pack(pady=10)

calcular()

janela.mainloop()