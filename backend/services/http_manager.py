import os
from http.server import BaseHTTPRequestHandler
class HTTPManager(BaseHTTPRequestHandler):

    # Override
    def do_GET(self):

        frontend_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            "../../",
            "frontend")
        )

        request_path = self.path.lstrip("/")

        if request_path == "":
            request_path = "index.html"

        file_path = os.path.join(frontend_path, request_path)

        mime_types = {
                ".html": "text/html",
                ".css": "text/css",
                ".js": "application/javascript",
                ".png": "image/png"
            }

        if os.path.exists(file_path) and os.path.isfile(file_path):
            ext = os.path.splitext(file_path)[1]
            self.send_response(200)
            self.send_header("Content-type", mime_types.get(ext))
            self.end_headers()

            with open(file_path, "rb") as f:
                self.wfile.write(f.read())

        elif os.path.exists(file_path + ".js") and os.path.isfile(file_path + ".js"):
            file_path += ".js"
            ext = ".js"
            self.send_response(200)
            self.send_header("Content-type", mime_types.get(ext))
            self.end_headers()

            with open(file_path, "rb") as f:
                self.wfile.write(f.read())

        else:
            self.send_error(404)
        # Fine do_GET(): Server chiude automaticamente la connessione
        # - istanza distrutta --> garbage collection