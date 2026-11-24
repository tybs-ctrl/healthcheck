from flask import Flask, jsonify
import socket
import json


app = Flask(__name__)

def read_healthchecks(file_path='/healthchecks'):
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/', methods=['GET'])
def healthcheck():
    healthchecks = read_healthchecks()
    results = []
    for check in healthchecks:
        host = check['host']
        port = check['port']
        try:
            socket.create_connection((host, port), timeout=1)
            status = 'OK'
        except (socket.timeout, OSError):
            status = 'FAILED'

        results.append({
            'host': host,
            'port': port,
            'status': status
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6789)