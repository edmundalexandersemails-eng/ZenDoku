from http.server import SimpleHTTPRequestHandler, HTTPServer

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), CORSRequestHandler)
    print('CORS-enabled server serving on http://0.0.0.0:8000')
    server.serve_forever()
