#!/usr/bin/env python3
"""Local Community-CRM server with session-backed donation/task role checks.

The app retains its existing browser storage and record/history format. The
server authenticates the selected coursework demo role, issues an HttpOnly
session cookie, and authorizes donation/task writes before the browser commits
those changes to localStorage. This is a local coursework authorization layer,
not production authentication or a shared server database.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from http.cookies import SimpleCookie
import json
import secrets
import threading

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8765
DEMO_PASSWORD = "demo123"
SESSIONS = {}
SESSION_LOCK = threading.Lock()
WRITE_ROUTES = {
    "/api/donation-write": {"admin", "staff"},
    "/api/donation-void": {"admin", "staff"},
    "/api/task-write": {"admin", "staff"},
    "/api/task-complete": {"admin", "staff"},
}


class CRMHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def _json(self, status, payload, extra_headers=None):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        if extra_headers:
            for name, value in extra_headers:
                self.send_header(name, value)
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0 or length > 1_000_000:
            raise ValueError("Invalid request size.")
        value = json.loads(self.rfile.read(length).decode("utf-8"))
        if not isinstance(value, dict):
            raise ValueError("A JSON object is required.")
        return value

    def _session_role(self):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get("Cookie", ""))
            token = cookie["crm_session"].value
        except (KeyError, ValueError):
            return None
        with SESSION_LOCK:
            return SESSIONS.get(token)

    def do_POST(self):
        try:
            if self.path == "/api/login":
                data = self._body()
                role = str(data.get("role", "")).lower()
                if data.get("password") != DEMO_PASSWORD or role not in {"admin", "staff", "viewer"}:
                    self._json(401, {"ok": False, "error": "Sign-in failed."})
                    return
                token = secrets.token_urlsafe(32)
                with SESSION_LOCK:
                    SESSIONS[token] = role
                self._json(200, {"ok": True, "role": role}, [
                    ("Set-Cookie", f"crm_session={token}; HttpOnly; SameSite=Strict; Path=/")
                ])
                return

            if self.path == "/api/logout":
                cookie = SimpleCookie()
                cookie.load(self.headers.get("Cookie", ""))
                token = cookie["crm_session"].value if "crm_session" in cookie else None
                if token:
                    with SESSION_LOCK:
                        SESSIONS.pop(token, None)
                self._json(200, {"ok": True}, [
                    ("Set-Cookie", "crm_session=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0")
                ])
                return

            if self.path in WRITE_ROUTES:
                data = self._body()
                if not self._session_role() in WRITE_ROUTES[self.path]:
                    self._json(403, {"ok": False, "error": "Server permission denied. Sign in as Admin or Staff to change donations and tasks."})
                    return
                self._json(200, {"ok": True, "authorized": True})
                return

            if self.path not in ("/api/contact-save", "/api/household-save"):
                self._json(404, {"ok": False, "error": "Unknown save route."})
                return

            record = self._body()
            if self.path == "/api/contact-save":
                first = str(record.get("firstName", "")).strip()
                last = str(record.get("lastName", "")).strip()
                if not first or not last:
                    self._json(422, {"ok": False, "error": "First and last name are required. Names cannot be blank or spaces only."})
                    return
                record["firstName"], record["lastName"] = first, last
            else:
                name = str(record.get("name", "")).strip()
                if not name:
                    self._json(422, {"ok": False, "error": "Household name is required and cannot be blank or spaces only."})
                    return
                record["name"] = name
            self._json(200, {"ok": True, "record": record})
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            self._json(400, {"ok": False, "error": str(exc) or "Invalid request."})


if __name__ == "__main__":
    print(f"Community-CRM server running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.")
    ThreadingHTTPServer((HOST, PORT), CRMHandler).serve_forever()
