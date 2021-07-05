from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from os import path
import json
import re
import base64

hostName = "0.0.0.0"
serverPort = 3000
storagePath = '/app/images/'

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _json_response(self, data, error = None, status = 200):
        self._set_headers(status)
        response_template = {
            'status': status,
            'data': data,
            'error': error
        }
        data = json.dumps(response_template)
        self.wfile.write(bytes(data, "utf-8"))
    
    def _router(self, path):
        if path == '/':
            self.do_welcome()
        elif path == '/urls':
            self.do_urls()
        elif re.search('^/find', path):
            self.do_find(path=path)
        else:
            self.do_not_found()
    
    def _exist(self, name):
        return path.exists(storagePath + name)

    def do_GET(self):
        self._router(self.path)

    def do_welcome(self):
        self._json_response('Welcome to my server!', status=200)

    def do_urls(self):
        urls = [
            {
                'type': 'GET',
                'path': '/urls',
                'params': None
            },
            {
                'type': 'GET',
                'path': '/find',
                'params': {
                    'name': 'image_name [String]'
                }
            },
        ]
        self._json_response(urls, status=200)


    def do_find(self, path):
        parsed = urlparse(path)
        result = parse_qs(parsed.query)
        if 'name' in result.keys():
            name = result['name'][0]

            is_exist = self._exist(name)
            
            if is_exist:
                image = None
                with open(storagePath + name, "rb") as imageFile:
                    image = base64.b64encode(imageFile.read()).decode('utf-8')
                response = {'image_name': name, 'is_exist': is_exist, 'image_data': image}
            else:
                response = {'image_name': name, 'is_exist': is_exist}
            self._json_response(response, status=200)
        else:
            self._json_response(None, error='please insert image name!', status=400)

    def do_not_found(self):
        self._json_response(None, error='Page Not Found', status=404)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
