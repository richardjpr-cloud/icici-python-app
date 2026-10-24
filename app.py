from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class ICICIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy"
            }
        else:
            response = {
                "application": "ICICI Python Application",
                "status": "running",
                "message": "Application is working successfully!"
            }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 8000), ICICIHandler)

print("ICICI application running on port 8000", flush=True)

server.serve_forever()
