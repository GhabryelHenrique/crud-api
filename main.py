import sqlite3
from flask import Flask, request, json, jsonify

app = Flask(__name__)
banco = sqlite3.connect('chinook.db', check_same_thread=False)
cursor = banco.cursor()

def get_db_connection():
    conn = sqlite3.connect('chinook.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Inicializa o banco de dados. Cria a tabela 'customers' se ela não existir.
    Esta função é chamada antes de a aplicação iniciar.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verifica se a tabela 'customers' já existe no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='customers'")
    table_exists = cursor.fetchone()
    
    # Se a tabela não existe (fetchone() retornou None), cria a tabela
    if table_exists is None:
        print(f"Tabela 'customers' não encontrada. Criando tabela...")
        cursor.execute("""
            CREATE TABLE customers (
                CustomerId INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName NVARCHAR(40) NOT NULL,
                LastName NVARCHAR(20) NOT NULL,
                Company NVARCHAR(80),
                Address NVARCHAR(70),
                City NVARCHAR(40),
                State NVARCHAR(40),
                Country NVARCHAR(40),
                PostalCode NVARCHAR(10),
                Phone NVARCHAR(24),
                Fax NVARCHAR(24),
                Email NVARCHAR(60) NOT NULL UNIQUE
            );
        """)
        conn.commit()
        print("Tabela 'customers' criada com sucesso.")
    else:
        print("Tabela 'customers' já existe.")
        
    conn.close()


@app.route('/customers', methods=["POST"])
def create_customer():
    data = request.get_json()
    # Pega todos os campos possíveis do JSON
    first_name = data.get('FirstName')
    last_name = data.get('LastName')
    email = data.get('Email')
    # ... outros campos são opcionais
    company = data.get('Company')
    address = data.get('Address')
    city = data.get('City')
    state = data.get('State')
    country = data.get('Country')
    postal_code = data.get('PostalCode')
    phone = data.get('Phone')
    fax = data.get('Fax')


    if not all([first_name, last_name, email]):
        return jsonify({'error': 'FirstName, LastName, e Email são campos obrigatórios'}), 400

    try:
        conn = get_db_connection()
        stmt_insert = """
            INSERT INTO customers (FirstName, LastName, Email, Company, Address, City, State, Country, PostalCode, Phone, Fax)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(stmt_insert, (first_name, last_name, email, company, address, city, state, country, postal_code, phone, fax))
        conn.commit()
        customer_id = cursor.lastrowid
        conn.close()
        
        return jsonify({'CustomerId': customer_id, **data}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': f'Email "{email}" já existe.'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/customers', methods=["GET"])
def get_all_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    records = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(records)


@app.route('/customers/<int:id>', methods=["PATCH"])
def update_customer(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers WHERE CustomerId = ?", (id,))
    customer = cursor.fetchone()
    if customer is None:
        conn.close()
        return jsonify({"error": "Cliente não encontrado"}), 404

    data = request.get_json()
    if not data:
        conn.close()
        return jsonify({"error": "Corpo da requisição não pode ser vazio"}), 400

    fields = []
    values = []
    # Usamos customer.keys() para garantir que a chave do JSON existe como coluna no BD
    for key, value in data.items():
        if key in customer.keys():
            fields.append(f"{key} = ?")
            values.append(value)

    if not fields:
        conn.close()
        return jsonify({"error": "Nenhum campo válido para atualização foi fornecido"}), 400

    values.append(id)
    sql = f"UPDATE customers SET {', '.join(fields)} WHERE CustomerId = ?"

    try:
        cursor.execute(sql, tuple(values))
        conn.commit()
        conn.close()
        return jsonify({"message": f"Cliente {id} atualizado com sucesso."})
    except sqlite3.Error as e:
        conn.close()
        return jsonify({"error": f"Erro no banco de dados: {e}"}), 500


@app.route('/customers/<int:id>', methods=["DELETE"])
def delete_customer(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'DELETE FROM customers WHERE CustomerId=?'
    cursor.execute(sql, (id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({'error': 'Cliente não encontrado'}), 404

    conn.close()
    return jsonify({'message': f'Cliente {id} deletado com sucesso.'})



init_db()

if __name__ == '__main__':
    app.run(debug=True)
