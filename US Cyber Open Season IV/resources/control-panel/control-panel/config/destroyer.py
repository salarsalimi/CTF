#!/usr/bin/env python3
import subprocess, json
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_json(content):
	return json.dumps(content).encode()

def http_server(host_port,content_type="application/json"):
	class CustomHandler(SimpleHTTPRequestHandler):
		def do_GET(self) -> None:
			def resp_ok():
				self.send_response(200)
				self.send_header("Content-type", content_type)
				self.end_headers()
			if self.path == '/status':
				resp_ok()
				self.wfile.write(get_json({'status': 'ready to destroy'}))
				return
			elif self.path == "/destroy":
				resp_ok()
				self.wfile.write(get_json({'status': "destruction complete!"}))
				return
			elif self.path == '/shutdown':
				resp_ok()
				self.wfile.write(get_json({'status': 'shutting down...'}))
				self.wfile.write(get_json({'status': 'SIVBGR{no-flag-4-u}'}))
				return
			self.send_error(404, '404 not found')
		def log_message(self, format, *args):
			pass
	class _TCPServer(TCPServer):
		allow_reuse_address = True
	httpd = _TCPServer(host_port, CustomHandler)
	httpd.serve_forever()

http_server(('127.0.0.1',3000))