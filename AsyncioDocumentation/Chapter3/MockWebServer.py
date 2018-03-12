from http.server import BaseHTTPRequestHandler,HTTPServer
from socketserver import ThreadingMixIn
import time

ENCODING='utf-8'
class ThreadingHTTPServer(ThreadingMixIn,HTTPServer):
    pass
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            seconds=float(self.path[1:])
        except ValueError:
            seconds=0.0
        if seconds<0:
            seconds=0.0
        text="Wait for {:4.2f} seconds.\nThat's all.\n"
        msg=text.format(seconds).encode(ENCODING)
        time.sleep(seconds)
        self.send_response(200)
        self.send_header("Content-type",'text/plain;charset=utf-8')
        self.send_header("Content-length",str(len(msg)))
        self.end_headers()
        self.wfile.write(msg)