import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


port = int(os.environ.get("CONDUCTOR_PORT", "8000"))
server = ThreadingHTTPServer(("127.0.0.1", port), NoCacheHandler)
print(f"Serving Custom AI Systems at http://127.0.0.1:{port}", flush=True)
server.serve_forever()
