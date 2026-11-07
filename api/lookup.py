# file: api/lookup.py
# *Серверлесс-функция Vercel. Обрабатывает GET-запросы, ищет совпадения в словаре.*
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

# Словарь-заглушка. Для реальных слитых баз подключи Supabase или PostgreSQL в одну строку.
MOCK_DB = {
    "hacker_one": {"phone": "+79991234567", "first_name": "Ivan", "last_name": "Petrov"},
    "shadow_net": {"phone": "+15550009999", "first_name": "John", "last_name": "Doe"},
    "ghost_protocol": {"phone": "+447700900000", "first_name": "Arthur", "last_name": "Vane"}
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

        if username in MOCK_DB:
            data = {"username": username, **MOCK_DB[username]}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.wfile.write(json.dumps({"error": "Not found in database"}).encode('utf-8'))
