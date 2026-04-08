import random
from datetime import datetime, timedelta
from google.colab import files

# ==============================================================
# GERADOR DE DADOS FINANCEIROS (MOCK DATA) - 500 VENDAS
# Autor: Nicolas Oliveira / nickdead93 | Foco: Teste de Stress em Modelagem ERP
# ==============================================================

sql = "-- SCRIPT DE INSERÇÃO DE MOCK DATA (500 VENDAS FINANCEIRAS)\n\n"

# 1. PLANO DE CONTAS (A Base da DRE)
sql += "INSERT INTO Plano_Contas (codigo_conta, nome_conta, tipo_conta) VALUES\n"
sql += "('3.1.1.01', 'Receita Bruta de Vendas', 'Receita'),\n"
sql += "('4.1.1.01', 'Custo da Mercadoria Vendida (CMV)', 'Custo'),\n"
sql += "('5.1.1.01', 'Despesas com Adquirencia (Taxas)', 'Despesa');\n\n"

# 2. PRODUTOS E CUSTOS (Para Margem Bruta)
produtos = [
    (1, 'Licença ERP Standard', 500.00, 1500.00),
    (2, 'Consultoria Financeira', 100.00, 350.00),
    (3, 'Dashboard Power BI', 80.00, 120.00)
]
sql += "INSERT INTO Produto (nome_produto, custo_unitario_cmv, preco_venda_tabela) VALUES\n"
sql += ",\n".join([f"('{p[1]}', {p[2]}, {p[3]})" for p in produtos]) + ";\n\n"

# 3. CLIENTES (Gerando 50 Clientes B2B e B2C)
sql += "INSERT INTO Cliente (tipo_cliente, data_cadastro, limite_credito) VALUES\n"
clientes_sql = []
for i in range(1, 51):
    tipo = random.choice(['PF', 'PJ'])
    limite = random.choice([1000.00, 5000.00, 15000.00])
    clientes_sql.append(f"('{tipo}', '2023-01-15', {limite})")
sql += ",\n".join(clientes_sql) + ";\n\n"

# 4. PEDIDOS (O Motor das 500 Vendas)
sql += "INSERT INTO Pedido (id_cliente, data_emissao, valor_total_bruto, status_pedido) VALUES\n"
pedidos_sql = []
data_base = datetime(2023, 1, 1)

for i in range(1, 501):
    id_cliente = random.randint(1, 50)
    data_emissao = data_base + timedelta(days=random.randint(0, 365))
    produto = random.choice(produtos)
    qtd = random.randint(1, 3)
    valor_total = produto[3] * qtd
    pedidos_sql.append(f"({id_cliente}, '{data_emissao.strftime('%Y-%m-%d %H:%M:%S')}', {valor_total}, 'Faturado')")
    
sql += ",\n".join(pedidos_sql) + ";\n\n"

# 5. GERANDO E BAIXANDO O ARQUIVO SQL
nome_arquivo = 'mock_data_financeiro.sql'
with open(nome_arquivo, 'w', encoding='utf-8') as f:
    f.write(sql)

files.download(nome_arquivo)
print("✅ SUCESSO! O arquivo com 500 vendas financeiras foi gerado e o download começou.")
