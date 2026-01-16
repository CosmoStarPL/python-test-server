from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"yooo 67 shit. brain is not braining. yooo lil pump on shhiiii shneee watafaaaa faaa..........ulug lox :(\n")
        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
