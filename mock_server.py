import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MockAIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        fake_metrics = {
            "model_status": "active",
            "gpu_temp": 68,
            "accuracy": 0.94
        }
        self.wfile.write(json.dumps(fake_metrics).encode('utf-8'))


if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8000), MockAIHandler)
    print("Local Mock Server running on http://127.0.0.1:8000 ...")
    server.serve_forever()





