from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_contacts(path):
    # Возвращаем файл 'contacts.html' на любой запрос
    return send_file('contacts.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)