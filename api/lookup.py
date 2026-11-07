# file: api/lookup.py
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PRANK_DB = {
    "onf1ow": {"phone": "+927825595", "first_name": "Усмонов", "last_name": "Ибодулло"},
    "azizhxn": {"phone": "+926100574", "first_name": "Азизхон", "last_name": "Фаттидинов"},
    "rembx_7": {"phone": "+928305666", "first_name": "Мухаммадхуча", "last_name": "Рустамов"},
    "mansur_4800": {"phone": "+935754521", "first_name": "Мансур", "last_name": "Пулотов"},
    "abdugsw": {"phone": "+782020707", "first_name": "Абдуазиз", "last_name": "Абдуманнонов"},
    "ssalimovv8": {"phone": "+928470001", "first_name": "Мухаммад", "last_name": "Салимов"},
    "sholk1313": {"phone": "+501009560", "first_name": "Муртазо", "last_name": "Байзоев"}
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        username = params.get('username', [''])[0].strip().lstrip('@').lower()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if not username:
            self.wfile.write(json.dumps({"error": "Username required"}).encode())
            return

        if username in PRANK_DB:
            data = {"username": username, **PRANK_DB[username]}
            self.wfile.write(json.dumps(data).encode())
        else:
            self.wfile.write(json.dumps({"error": "Not found in prank database"}).encode())
