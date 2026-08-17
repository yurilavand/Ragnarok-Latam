# ⚔️ Ragnarok-Latam

Coleção de ferramentas e calculadoras para auxiliar jogadores do servidor **Ragnarok LATAM**.

---

## 📂 Projetos

### 1.1 — PurePot
Calculadora que determina as quantidades corretas de itens para cada tipo de poção.

---

### 1.2 — Calculadora de Semijoias Ragnarok LATAM
Ferramenta em **Python (Tkinter)** para calcular automaticamente os insumos necessários na criação de **Semijoias**.

#### ⚙️ Funcionalidades
- Interface gráfica simples e intuitiva com **Tkinter**.  
- Seleção do tipo de semijoia (Inferior, Comum, Incomum, Superior).  
- Campo para definir a quantidade desejada.  
- Cálculo automático de:
  - Minérios de Sombridecon  
  - Sombridecons  
  - Semijoias Inferiores, Comuns e Incomuns  
  - Custo total em Zeny  
- Exportação automática de relatório em `.txt` na mesma pasta do script.

---

## 🚀 Roadmap de Longo Prazo — Calculadoras Ragnarok LATAM

### 📌 Fase 1 — Estrutura e Modularização
- Separar lógica e interface: criar módulos Python só para cálculos e outro para Tkinter.  
- Reutilização de código: funções comuns (ex.: exportar relatório) em módulo compartilhado.  
- Estrutura de pastas: cada calculadora em seu diretório, com README próprio.  

### 📌 Fase 2 — Qualidade e Confiabilidade
- Testes automatizados para validar cálculos em diferentes cenários.  
- Validação de entradas para evitar erros com valores inválidos.  
- Documentação técnica detalhada.  

### 📌 Fase 3 — Expansão de Funcionalidades
- Coleção de calculadoras: Semijoias, PurePotter e Farmacologia em um “kit de utilidades”.  
- Modo rápido: relatórios para Arma, Armadura e Acessório de uma só vez.  
- Configurações personalizadas: ajustar valores de Zeny e insumos conforme servidor.  

### 📌 Fase 4 — Integração e Aprendizado Avançado
- Interface web com Flask ou Django.  
- Distribuição em executáveis para Windows/Linux.  
- Integração com guild: relatórios compartilhados para toda a guild.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**  
- **Tkinter** (interface gráfica)  
- **Automação de relatórios em `.txt`**

---

## 📜 Licença
Este projeto é open-source e distribuído sob a licença MIT.
