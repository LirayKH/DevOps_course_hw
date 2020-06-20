import http.server
import socketserver
import sys

PORT = int((sys.argv[1]) or "7001")

print (sys.argv[1])

PORT = int(sys.argv[1])

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()