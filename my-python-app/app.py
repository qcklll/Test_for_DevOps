from http.server import HTTPServer, BaseHTTPRequestHandler

def handle_request(request):
    request.send_response(200)
    request.end_headers()
    message = b'Hello, Kubernetes!'
    request.wfile.write(message)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    server_address = (host, port)
    httpd = HTTPServer(server_address, BaseHTTPRequestHandler)
    print(f'Listening on {host}:{port}')
    httpd.serve_forever()

