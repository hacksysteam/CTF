import argparse

from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn
from SimpleHTTPServer import SimpleHTTPRequestHandler


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """
    Threaded HTTP Server
    
    https://stackoverflow.com/questions/14088294/multithreaded-web-server-in-python.
    """
    pass


class RequestHandler(SimpleHTTPRequestHandler):
    def send_nocache_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate, pre-check=0, post-check=0, max-age=0")
        self.send_header("Expires", "0")
        self.send_header("Pragma", "no-cache")

    def end_headers(self):
        self.send_nocache_headers()
        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Server")
    
    parser.add_argument("-i", "--ip", help="IP/Host", action="store", default="127.0.0.1")
    parser.add_argument("-p", "--port", help="Port", action="store", default=8000, type=int)

    args = parser.parse_args()

    print("Serving on {0}:{1}".format(args.ip, args.port))

    server = ThreadedHTTPServer((args.ip, args.port), RequestHandler)
    server.daemon_threads = True

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        print("Shutting down...")
