import random
import numpy as np
import pandas as pd

random.seed(42)
np.random.seed(42)

total_customers = 1000
total_products = 50
total_orders = 5000


# CADASTRO DE CLIENTES

states = ['SP', 'RJ', 'MG', 'RS', 'PR', 'BA', 'SC', 'PE', 'CE', 'GO']
state_weights = [35, 15, 12, 8, 8, 6, 5, 4, 4, 3]

first_names = ['Ana', 'Bruno', 'Carla', 'Diego', 'Elisa', 'Felipe', 'Gabriela', 'Hugo', 'Isabela', 'João',
               'Karina', 'Lucas', 'Mariana', 'Nicolas', 'Olivia', 'Paulo', 'Rafaela', 'Sérgio', 'Tatiana', 'Vinícius']
last_names = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Lima', 'Pereira', 'Costa', 'Ribeiro', 'Almeida', 'Carvalho']

customers = pd.DataFrame({
    'customer_id': range(1, total_customers + 1),
    'customer_name': [f'{random.choice(first_names)} {random.choice(last_names)}' for _ in range(total_customers)],
    'state': random.choices(states, weights=state_weights, k=total_customers),
    'signup_date': pd.to_datetime('2022-01-01') + pd.to_timedelta(np.random.randint(0, 1096, total_customers), unit='D')
})

customers.to_csv('customers.csv', index=False)
print('customers.csv created:', customers.shape)


# PRODUTOS POR CATEGORIA

categories = {
    'Eletrônicos': {
        'min_price': 50, 'max_price': 1500,
        'items': ['Fone de Ouvido Bluetooth', 'Carregador Portátil', 'Smartwatch', 'Caixa de Som', 'Mouse Sem Fio',
                  'Teclado Gamer', 'Webcam Full HD', 'Cabo USB-C', 'Smart TV 43', 'Tablet 10 Polegadas']
    },
    'Casa': {
        'min_price': 30, 'max_price': 600,
        'items': ['Air Fryer', 'Jogo de Panelas', 'Jogo de Lençol', 'Cafeteira Elétrica', 'Liquidificador',
                  'Ventilador de Mesa', 'Toalha de Banho', 'Organizador Multiuso', 'Luminária de Mesa', 'Garrafa Térmica']
    },
    'Moda': {
        'min_price': 25, 'max_price': 350,
        'items': ['Camiseta Básica', 'Calça Jeans', 'Jaqueta Corta-Vento', 'Tênis Casual', 'Vestido Midi',
                  'Bermuda de Sarja', 'Bolsa de Ombro', 'Mochila Urbana', 'Boné Aba Curva', 'Kit 6 Pares de Meias']
    },
    'Esporte': {
        'min_price': 20, 'max_price': 800,
        'items': ['Tênis de Corrida', 'Bola de Futebol', 'Halteres 5kg', 'Tapete de Yoga', 'Corda de Pular',
                  'Garrafa Esportiva', 'Camisa Dry Fit', 'Luva de Treino', 'Kit Faixas Elásticas', 'Bicicleta Ergométrica']
    },
    'Beleza': {
        'min_price': 15, 'max_price': 400,
        'items': ['Perfume Importado', 'Kit Shampoo e Condicionador', 'Hidratante Corporal', 'Protetor Solar FPS 50', 'Base Líquida',
                  'Batom Matte', 'Secador de Cabelo', 'Chapinha', 'Paleta de Sombras', 'Sérum Facial']
    }
}

products_list = []
product_id = 1

for category, info in categories.items():
    for product_name in info['items']:
        unit_price = round(random.uniform(info['min_price'], info['max_price']), 2)
        products_list.append({
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'unit_price': unit_price
        })
        product_id += 1

products = pd.DataFrame(products_list)

products.to_csv('products.csv', index=False)
print('products.csv created:', products.shape)


# PEDIDOS

month_weights = [7, 6, 7, 7, 8, 8, 7, 7, 8, 9, 14, 13]
customer_weights = np.random.exponential(scale=1, size=total_customers)

months = random.choices(range(1, 13), weights=month_weights, k=total_orders)
days = np.random.randint(1, 29, total_orders)

orders = pd.DataFrame({
    'customer_id': random.choices(customers['customer_id'], weights=customer_weights, k=total_orders),
    'order_date': pd.to_datetime(pd.DataFrame({'year': 2025, 'month': months, 'day': days})),
    'status': random.choices(['Entregue', 'Cancelado', 'Devolvido'], weights=[88, 8, 4], k=total_orders)
})

orders = orders.sort_values('order_date').reset_index(drop=True)
orders.insert(0, 'order_id', range(1, total_orders + 1))

orders.to_csv('orders.csv', index=False)
print('orders.csv created:', orders.shape)


# ITENS DO PEDIDO

product_weights = np.random.exponential(scale=1, size=len(products))
product_probs = product_weights / product_weights.sum()

items_list = []

for order_id in orders['order_id']:
    items_count = random.choices([1, 2, 3, 4], weights=[50, 30, 15, 5])[0]
    chosen_products = np.random.choice(products['product_id'], size=items_count, replace=False, p=product_probs)

    for chosen_id in chosen_products:
        items_list.append({
            'order_id': order_id,
            'product_id': chosen_id,
            'quantity': random.choices([1, 2, 3], weights=[70, 22, 8])[0]
        })

order_items = pd.DataFrame(items_list)

order_items.to_csv('order_items.csv', index=False)
print('order_items.csv created:', order_items.shape)


# SUJANDO OS DADOS

# customers: states with null, states in lowercase and duplicated rows
null_idx = customers.sample(frac=0.03, random_state=1).index
customers.loc[null_idx, 'state'] = np.nan

lower_idx = customers.sample(frac=0.05, random_state=2).index
customers.loc[lower_idx, 'state'] = customers.loc[lower_idx, 'state'].str.lower()

customers = pd.concat([customers, customers.sample(n=20, random_state=3)], ignore_index=True)

# products: categories written in different ways
dirty_idx = products.sample(n=8, random_state=4).index
products.loc[dirty_idx[:4], 'category'] = products.loc[dirty_idx[:4], 'category'].str.upper()
products.loc[dirty_idx[4:], 'category'] = products.loc[dirty_idx[4:], 'category'] + ' '

# orders: null status, wrong dates and duplicated rows
status_idx = orders.sample(frac=0.02, random_state=5).index
orders.loc[status_idx, 'status'] = np.nan

date_idx = orders.sample(n=15, random_state=6).index
orders.loc[date_idx, 'order_date'] = orders.loc[date_idx, 'order_date'] + pd.Timedelta(days=3650)

orders = pd.concat([orders, orders.sample(n=30, random_state=7)], ignore_index=True)

# saving the dirty files (overwrites the clean ones)
customers.to_csv('customers.csv', index=False)
products.to_csv('products.csv', index=False)
orders.to_csv('orders.csv', index=False)

print('dirty customers.csv:', customers.shape)
print('dirty products.csv:', products.shape)
print('dirty orders.csv:', orders.shape)
