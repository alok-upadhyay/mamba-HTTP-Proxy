import SimpleHTTPServer
import SocketServer
import BaseHTTPServer
import httplib2


PORT = 8004

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
	print s.command
	print s.path
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

	h = httplib2.Http(".cache")
	resp, content = h.request(s.path, "GET")	

	s.wfile.write(content)
        #s.wfile.write("<html><head><title>Title goes here.</title></head>")
        #s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        #s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        #s.wfile.write("</body></html>")


Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "serving at port", PORT

sa = httpd.socket.getsockname()
print sa

httpd.serve_forever()
