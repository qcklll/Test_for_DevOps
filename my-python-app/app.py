from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Kubernetes!"
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f'Listening on {host}:{port}')
    httpd.serve_forever()
