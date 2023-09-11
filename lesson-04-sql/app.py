import sqlite3
from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

def conn_init():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_customers_json(customers):
    return json.dumps([
        {
            'id': customer[0],
            'first_name': customer[1],
            'last_name': customer[2]
        }
        for customer in customers
    ], sort_keys=False)


@app.route("/names/")
def get_unique_names():
    conn = conn_init()

    query = "SELECT * FROM customers GROUP BY first_name ORDER BY id ASC"
    customers = conn.execute(query).fetchall()
    conn.close()

    return Response(
        get_customers_json(customers), 
        content_type='application/json'
    )


# /customers/?first_name=Олена&id=9&last_name=Остапчук
@app.route("/customers/")
def get_customers():
    query = ""
    conn = conn_init()

    for key in request.args.keys():
        value = request.args.get(key)
        if not value:
            continue

        if query == "":
            query = "SELECT * FROM customers WHERE {} = '{}'".format(key, value)
        else: 
            query += " AND {} = '{}'".format(key, value)

    if not query:
        query = "SELECT * FROM customers"

    customers = conn.execute(query).fetchall()
    conn.close()

    return Response(
        get_customers_json(customers), 
        content_type='application/json'
    )


@app.route("/tracks/count")
def tracks_count():
    conn = conn_init()
    query = "SELECT COUNT(id) FROM tracks"
    count = conn.execute(query).fetchone()[0]
    conn.close()

    return jsonify({
        "Кількість треків": count
    })


@app.route("/tracks/duration")
def get_all_tracks():
    conn = conn_init()

    query = "SELECT name, duration FROM tracks ORDER BY id ASC"
    tracks = conn.execute(query).fetchall()
    conn.close()

    json_data = json.dumps([
        {
            'name': track[0],
            'duration': track[1]
        }
        for track in tracks
    ], sort_keys=False)

    return Response(
        json_data, 
        content_type='application/json'
    ) 
