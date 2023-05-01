data_a = [2,3,4,5,6]
data_b = [data_a, 3,5,6,8,9]
print(f'''
Data a = {data_a}
Data b = {data_b} <- Nested data a in list data b
''')

customer01 = ['John Wick', 35, "London"]
customer02 = ['Blondie', 32, 'Los Angeles']
customer03 = ['Tarantino', 38, 'Las Vegas']

customers = [customer01, customer02, customer03]
print(customers)

for customer in customers:
    print(f'''
    Customer Data
    Name  : {customer[0]}
    Age   : {customer[1]}
    Adress: {customer[2]}
    ''')

customer_copy = customers.copy()
customer02[0]= "Rhed Bustamante"
print(f'''
{customers}

{customer_copy}
''')