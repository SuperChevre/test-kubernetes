import urllib.request

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)


#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        fp = urllib.request.urlopen("http://127.0.0.1:8080")
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        if ( mystr == "version: 1.0" ):
            message = "OK - "
        else:
            message = "NOT OK -"
        message += mystr

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 


def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('0.0.0.0', 80)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()