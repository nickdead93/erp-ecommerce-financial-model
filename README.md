# 🛒 Modelagem de Banco de Dados: ERP E-commerce & Visão Financeira

Este repositório contém a resolução do desafio de Projeto Conceitual de Banco de Dados da DIO, expandido e adaptado para a realidade de **Controladoria, FP&A e Engenharia de Dados Financeiros**.

## 🎯 Objetivo de Negócio
O objetivo não foi apenas desenhar um esquema de E-commerce genérico, mas sim estruturar a base de dados de um ERP para que a equipe financeira consiga extrair relatórios precisos de DRE, Fluxo de Caixa e Custos Logísticos.

## 🛠️ Refinamentos Aplicados (Regras de Negócio Financeiras):

1. **Separação Exclusiva PF e PJ (B2C vs B2B):**
   - **Por que isso importa:** Clientes Pessoa Física (PF) e Pessoa Jurídica (PJ) possuem cargas tributárias diferentes (ICMS, IPI, Substituição Tributária). A modelagem utiliza o conceito de especialização exclusiva para garantir que o Power BI do departamento fiscal calcule a margem líquida corretamente.

2. **Múltiplos Meios de Pagamento por Pedido:**
   - **Por que isso importa:** Permite o *Split Payment* (ex: pagou metade no PIX, metade no Cartão). No modelo, incluí o campo `taxa_adquirencia`, vital para a **Conciliação Bancária** e cálculo exato das despesas financeiras no Fluxo de Caixa Diário.

3. **Logística, Status e Rastreio:**
   - **Por que isso importa:** Para conformidade com as normas contábeis (ex: IFRS 15), o Reconhecimento da Receita só ocorre quando o controle do bem é transferido. O `status_entrega = 'Entregue'` serve como o gatilho automatizado para a contabilização da receita, além de permitir auditar o `custo_frete` (Despesa com Vendas).

## 📊 Arquivos
* `README.md`: Documentação executiva das regras de negócio.
* `schema_financeiro.sql`: DDL com a estrutura das tabelas simulando o ERP.
* *Diagrama.drawio.png*
