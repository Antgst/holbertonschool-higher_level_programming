#!usr/bin/python3
"""
task_03_http_server.py

A simple HTTP API built with Python's built-in http.server module.

Endpoints:
- GET /       -> "Hello, this is a simple API!"
- GET /data   -> JSON: {"name": "John", "age": 30, "city": "New York"}
- GET /status -> "OK"
- Any other   -> 404 "Endpoint not found"
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyOwnHandler(BaseHTTPRequestHandler):
    """Request handler for a minimal API server."""

    def do_GET(self):
        """
        Handle GET requests and route them based on the requested path.

        Routes:
        - /       : returns a plain text greeting
        - /data   : returns sample JSON data
        - /status : returns plain text "OK"
        - other   : returns 404 with "Endpoint not found"
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            json_info = json.dumps(info)
            self.wfile.write(json_info.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content_Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"EndPoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyOwnHandler)
    httpd.serve_forever()
