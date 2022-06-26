import sqlite3
from flask import Flask, request, json, jsonify

app = Flask(__name__)
banco = sqlite3.connect('chinook.db', check_same_thread=False)
cursor = banco.cursor()


@app.route('/create', methods=["POST"])
def create():

    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    company = request.json.get('company')
    address = request.json.get('address')
    city = request.json.get('city')
    state = request.json.get('state')
    country = request.json.get('country')
    postal_code = request.json.get('postal_code')
    phone = request.json.get('phone')
    email = request.json.get('email')
    fax = request.json.get('fax')

    user = (first_name, last_name, company, address, city, state, country, postal_code, phone, email, fax)

    print(user)

    stmt_insert = """INSERT INTO customers (
    FIRSTNAME, LASTNAME, ADDRESS, company, CITY, STATE, COUNTRY, POSTALCODE, PHONE, EMAIL, Fax)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.executemany(stmt_insert, (user,))
    banco.commit()
    return jsonify(request.json)


@app.route('/read', methods=["GET"])
def read():
    def row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
        data = {}
        for idx, col in enumerate(cursor.description):
            data[col[0]] = row[idx]
        return data

    cursor.row_factory = row_to_dict
    cursor.execute('SELECT * FROM customers')
    records = cursor.fetchall()
    return jsonify(records)


@app.route('/update/<int:id>', methods=["PATCH"])
def update(id):
    print('Em Breve...')
    return 'Em Breve...', id


@app.route('/delete/<id>', methods=["DELETE"])
def delete(id: int):
    sql = 'DELETE FROM customers WHERE CustomerId=?'
    cursor.execute(sql, (id,))
    return 'Sucesso'


app.run()
