from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Главная страница
        elif self.path == '/contacts':
            self.path = 'contacts.html'  # Страница контактов
        return super().do_GET()

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    server = HTTPServer((host, port), MyHandler)
    print(f"Сервер запущен на http://{host}:{port}")
    server.serve_forever()