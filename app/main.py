from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello gitops ci/cd with python v1")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("server started on :8080")
    server.serve_forever()
