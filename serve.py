import http.server, os, sys

port = int(os.environ.get("PORT", 3456))
directory = "/Users/honzakohoutek/Documents/Claude_coding/honzikovic-cesta"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)
    def log_message(self, format, *args):
        pass

with http.server.HTTPServer(("", port), Handler) as httpd:
    sys.stderr.write(f"Serving on http://localhost:{port}\n")
    sys.stderr.flush()
    httpd.serve_forever()
