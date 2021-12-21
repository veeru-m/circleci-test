from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import logging
import socket

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<p>---  %s</p>" % self.path, "utf-8"))

        logging.info("the name entered is---%s" % self.path)


if __name__ == "__main__":

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    logging.basicConfig(level=logging.INFO,
        format="{} - - %(asctime)s %(levelname)s %(message)s".format(local_ip),datefmt='[%d-%b-%Y %H:%M:%S]')

    port = os.environ.get('PORT')
    port = int(port)


    webServer = HTTPServer(('', port), MyServer)
    logging.error("Server started http://localhost:%s" % port)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

