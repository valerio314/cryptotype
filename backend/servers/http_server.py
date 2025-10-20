from http.server import HTTPServer
from backend.services.http_manager import HTTPManager

def run_http(ip:str, port:int):

    # Avvia il server
    socket = (ip, port)
    httpd = HTTPServer(socket, HTTPManager)

    print(f"Server Online: {socket}")
    print(f"Visit http://{ip}:{port}")
    print("Stop Server: Ctrl+C")

    # Connessione persistente
    httpd.serve_forever()