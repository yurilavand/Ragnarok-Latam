# Ragnarok-Latam

## PurePotter (ou Farmacêutico)

É o nome que se dá para a famosa construção de personagem (build) do Alquimista focada 100% em criar poções em vez de batalhar. No Ragnarok Online, esse tipo de personagem coloca quase todos os pontos em Destreza (DEX) e Sorte (LUK) para ter a maior taxa de sucesso possível na hora de fabricar os itens.

### Projetos

## Calculadoras
## 1.1-PurePot  

Calcula as quantidades corretas de itens para cada poção.


# 1.2 - Calculadora de Semijoias Ragnarok LATAM

Ferramenta em **Python (Tkinter)** para calcular automaticamente os insumos necessários na criação de **Semijoias** no servidor **Ragnarok LATAM**.  
O programa exibe os materiais, Sombridecons, Minérios de Sombridecon e custo total em Zeny, além de gerar relatórios automáticos em `.txt`.

---

## ⚙️ Funcionalidades

- Interface gráfica simples e intuitiva com **Tkinter**.  
- Seleção de tipo de semijoia (Inferior, Comum, Incomum, Superior).  
- Campo para definir a quantidade desejada.  
- Cálculo automático de:
  - Minérios de Sombridecon  
  - Sombridecons  
  - Semijoias Inferiores, Comuns e Incomuns  
  - Custo total em Zeny  
- Exportação automática do relatório em `.txt` na mesma pasta do script.



🚀 Roadmap de Longo Prazo — Calculadoras Ragnarok LATAM
📌 Fase 1 — Estrutura e Modularização
Separar lógica e interface: criar módulos Python só para cálculos e outro para Tkinter, facilitando manutenção.

Reutilização de código: funções comuns (ex.: exportar relatório) ficam em um módulo compartilhado.

Estrutura de pastas: cada calculadora em seu diretório, com README próprio.

📌 Fase 2 — Qualidade e Confiabilidade
Testes automatizados: garantir que os cálculos estejam corretos em diferentes cenários.

Validação de entradas: impedir erros quando o usuário digitar valores inválidos.

Documentação técnica: explicar como o código funciona, para você e outros devs.

📌 Fase 3 — Expansão de Funcionalidades
Coleção de calculadoras: reunir Semijoias, PurePotter e Farmacologia em um “kit de utilidades”.

Modo rápido: gerar relatórios para Arma, Armadura e Acessório de uma só vez.

Configurações personalizadas: permitir ajustar valores de Zeny e insumos conforme o servidor.

📌 Fase 4 — Integração e Aprendizado Avançado
Interface web: migrar para Flask ou Django, permitindo acesso via navegador.

Distribuição: gerar executáveis para Windows/Linux, sem precisar instalar Python.

Integração com guild: criar relatórios compartilhados para toda a guild.
