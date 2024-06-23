import os

from flask import Flask, request

from resources import EntryManager, Entry

app = Flask(__name__)
FOLDER = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def hello_test():
    return "<p>Hello, test!</p>"


@app.route("/api/entries/")
def get_entries():
    entry_manager = EntryManager(FOLDER)
    entry_manager.load()
    entries_list = [entry.json() for entry in entry_manager.entries]
    return entries_list

@app.route('/api/save_entries/', methods=['POST'])
def save_entries():
    entry_manager = EntryManager(FOLDER)
    json_data = request.get_json()

    for entry_data in json_data:
        entry = Entry.from_json(entry_data)
        entry_manager.entries.append(entry)

    entry_manager.save()

    return {'status': 'success'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
