\# 🛒 Análise de Vendas de um E-commerce



Estudo de caso de análise de dados com \*\*Python\*\* e \*\*SQL\*\*, seguindo a metodologia \*\*CRISP-DM\*\*.



\## Sobre o projeto



A \*\*Vitrine Brasil\*\* é uma loja online fictícia que vende produtos de cinco categorias. A diretoria quer decidir onde investir em marketing e estoque antes da Black Friday de 2026, e este projeto analisa os dados de vendas de 2025 para apoiar essa decisão.



\## Perguntas de negócio



1\. Quais categorias e produtos geram mais receita?

2\. Como as vendas variam mês a mês?

3\. Quais estados compram mais?

4\. Qual o ticket médio?

5\. Quantos clientes compram só uma vez e quantos voltam a comprar?



\## Principais resultados



\- \*\*Eletrônicos\*\* é a categoria que mais gera receita e \*\*Beleza\*\* a que menos gera.

\- \*\*Novembro\*\* é o mês de maior receita, com provável efeito da Black Friday.

\- \*\*São Paulo\*\* lidera as vendas por estado.

\- O ticket médio é de R$ 878,69 e o ticket mediano é de R$ 575,85.

\- \*\*82,4%\*\* dos clientes são recorrentes.



\## Ferramentas



Python (pandas, matplotlib e seaborn), SQL (SQLite), Jupyter Notebook e Git.



\## Como reproduzir



```bash

git clone https://github.com/ricardo-paganini/ecommerce-sales-analysis.git

cd ecommerce-sales-analysis

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

python -m ipykernel install --user --name=ecommerce-venv --display-name='Python (ecommerce)'

jupyter notebook

```



No Linux ou Mac, ative o ambiente com `source venv/bin/activate`. Depois, abra o `ecommerce\_analysis.ipynb`, escolha o kernel \*\*Python (ecommerce)\*\* e vá em \*\*Kernel > Restart \& Run All\*\*.



\## Arquivos



| Arquivo | Para que serve |

|---|---|

| `ecommerce\_analysis.ipynb` | Notebook com toda a análise |

| `generate\_data.py` | Gera as bases fictícias em CSV |

| `customers.csv`, `products.csv`, `orders.csv`, `order\_items.csv` | Dados do projeto |

| `requirements.txt` | Bibliotecas necessárias |



\## Observação



Os dados são \*\*fictícios\*\*, gerados com semente fixa para que os resultados sejam sempre os mesmos.

