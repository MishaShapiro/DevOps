from http.server import BaseHTTPRequestHandler, HTTPServer


class App(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(200)
       self.send_header("Content-type", "text/html")
       self.end_headers()

       self.wfile.write(b"""
       <h1>Shop App</h1>
       <p>Second pet project</p>
       """)


server = HTTPServer(("127.0.0.1", 8002), App)
server.serve_forever()
