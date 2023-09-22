import json
import sqlite3

from flask import Flask, Response, jsonify

app = Flask(__name__)

def conn_init():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/names/")
def get_unique_names():
    conn = conn_init()
    query = "SELECT COUNT(DISTINCT first_name) FROM customers"
    count = conn.execute(query).fetchone()[0]
    conn.close()

    return jsonify({
        "Кількість унікальних імен": count
    })


@app.route("/tracks/")
def tracks_count():
    conn = conn_init()
    query = "SELECT COUNT(id) FROM tracks"
    count = conn.execute(query).fetchone()[0]
    conn.close()

    return jsonify({
        "Кількість треків": count
    })


@app.route("/tracks-sec/")
def get_all_tracks():
    conn = conn_init()

    query = "SELECT id, duration FROM tracks ORDER BY id ASC"
    tracks = conn.execute(query).fetchall()
    conn.close()

    json_data = json.dumps([
        {
            'id': track[0],
            'duration': track[1]
        }
        for track in tracks
    ], sort_keys=False)

    return Response(
        json_data, 
        content_type='application/json'
    ) 
