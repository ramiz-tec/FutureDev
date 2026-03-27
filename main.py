#!/usr/bin/env python3
"""
Main script to serve the FutureDev website.
This script starts a simple HTTP server to serve all the HTML files and assets.
"""

import http.server
import socketserver
import os
from urllib.parse import urlparse
from http.server import SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # Default to index.html if root is requested
        if path == '/':
            path = '/index.html'

        # Check if the file exists
        file_path = os.path.join(os.getcwd(), path.lstrip('/'))
        if os.path.isfile(file_path):
            return super().do_GET()
        else:
            # If file doesn't exist, serve index.html (SPA-like behavior)
            self.path = '/index.html'
            return super().do_GET()

def main():
    PORT = 8000
    Handler = CustomHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving FutureDev website at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()