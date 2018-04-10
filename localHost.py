import http.server
import socketserver
# run in background in terminal
# python3 -m http.server 8000 &
# disconnect with disown
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
