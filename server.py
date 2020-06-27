from http.server import HTTPServer, BaseHTTPRequestHandler
import controller

class Serv (BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello":
            self.path = "/index.html"
        try:
            controller.save_objects()
            controller.read_objects()
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


http = HTTPServer(('localhost', 8080), Serv)
http.serve_forever()