from http.server import BaseHTTPRequestHandler, HTTPServer


class App(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(200)
       self.send_header("Content-type", "text/html")
       self.end_headers()

       self.wfile.write(b"""
       <h1>Notes App</h1>
       <p>First pet project</p>
       """)


server = HTTPServer(("127.0.0.1", 8001), App)
server.serve_forever()
